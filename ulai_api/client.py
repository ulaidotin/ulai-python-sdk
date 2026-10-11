import os
import httpx
from typing import Optional, Any

from .services.sip import SIPService
from .services.dispatch import DispatchService
from .services.sessions import SessionService

class UlaiClient:
    def __init__(self, backend_url: Optional[str] = None, control_plane_url: Optional[str] = None, api_key: Optional[str] = None, system_secret: Optional[str] = None):
        self.backend_url = (backend_url or os.getenv("ULAI_API_URL", "https://backend.ulai.co.in")).rstrip("/")
        self.control_plane_url = (control_plane_url or os.getenv("ULAI_CP_URL", "https://cp.ulai.co.in")).rstrip("/")
        self.api_key = api_key or os.getenv("ULAI_API_KEY")
        self.system_secret = system_secret or os.getenv("ULAI_SYSTEM_SECRET")
        
        if not self.api_key and not self.system_secret:
            raise ValueError("ULAI_API_KEY or ULAI_SYSTEM_SECRET is required.")

        headers = {
            "Content-Type": "application/json"
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        if self.system_secret:
            headers["X-System-Secret"] = self.system_secret

        self._backend_client = httpx.AsyncClient(
            base_url=self.backend_url,
            headers=headers
        )
        self._cp_client = httpx.AsyncClient(
            base_url=self.control_plane_url,
            headers=headers
        )
        self.project_id: Optional[str] = None

    async def __aenter__(self):
        """Async initialization: Auto-discover the project_id."""
        
        # 1. Fetch the project ID bound to this API key
        resp = await self._backend_client.get("/api/v1/auth/me")
        resp.raise_for_status()
        self.project_id = resp.json()["project_id"]
        
        # 2. Inject the respective clients and project_id into the service namespaces
        self.sip = SIPService(self._backend_client, self.project_id)
        self.dispatch = DispatchService(self._backend_client, self.project_id)
        self.sessions = SessionService(self._cp_client)
        
        # Instantiate Agent gRPC service reusing cp url and api key
        from .services.agent import AgentService
        self.agent = AgentService(control_plane_url=self.control_plane_url, api_key=self.api_key)
        
        return self

    async def aclose(self) -> None:
        """Close underlying HTTP clients."""
        await self._backend_client.aclose()
        await self._cp_client.aclose()

    async def close(self) -> None:
        """Close underlying HTTP clients."""
        await self.aclose()

    async def __aexit__(
        self,
        exc_type: Optional[type] = None,
        exc_val: Optional[BaseException] = None,
        exc_tb: Optional[Any] = None
    ) -> None:
        await self.aclose()