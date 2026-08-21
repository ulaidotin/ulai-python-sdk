import os
import httpx
from typing import Optional

from .services.sip import SIPService
from .services.dispatch import DispatchService
from .services.sessions import SessionService

class UlaiClient:
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None):
        self.base_url = (base_url or os.getenv("ULAI_API_URL", "https://console.ulai.co.in")).rstrip("/")
        self.api_key = api_key or os.getenv("ULAI_API_KEY")
        
        if not self.api_key:
            raise ValueError("ULAI_API_KEY is required.")

        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        )
        self.project_id: Optional[str] = None

    async def __aenter__(self):
        """Async initialization: Auto-discover the project_id."""
        
        # 1. Fetch the project ID bound to this API key
        resp = await self._client.get("/api/v1/auth/me") # Updated to match backend
        resp.raise_for_status()
        self.project_id = resp.json()["project_id"]
        
        # 2. Inject the project_id into the service namespaces!
        self.sip = SIPService(self._client, self.project_id)
        self.dispatch = DispatchService(self._client, self.project_id)
        # self.sessions = SessionService(self._client, self.project_id)
        
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._client.aclose()