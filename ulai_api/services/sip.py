from typing import List, Optional, Union
from uuid import UUID
import httpx

from ..models.sip import (
    SIPInboundTrunk,
    CreateInboundTrunkRequest,
    SIPOutboundTrunk,
    CreateOutboundTrunkRequest,
    SIPTransport,
)



class SIPService:
    """Manages Inbound and Outbound SIP Trunks against Ulai Cloud Backend."""

    def __init__(self, client: httpx.AsyncClient, project_id: str):
        self._client = client
        self._project_id = project_id

    # ── Inbound Trunks ────────────────────────────────────────────────────────

    async def create_inbound_trunk(
        self,
        name: str,
        numbers: Optional[List[str]] = None,
        allowed_addresses: Optional[List[str]] = None,
    ) -> SIPInboundTrunk:
        """Provisions an inbound SIP Trunk (IP ACL & Phone Number whitelist)."""
        payload = CreateInboundTrunkRequest(
            name=name,
            numbers=numbers,
            allowed_addresses=allowed_addresses,
        ).model_dump(exclude_none=True)

        resp = await self._client.post(
            f"/api/v1/projects/{self._project_id}/sip-inbound-trunks",
            json=payload,
        )
        resp.raise_for_status()
        return SIPInboundTrunk.model_validate(resp.json())

    async def list_inbound_trunks(self) -> List[SIPInboundTrunk]:
        """Lists all inbound trunks for the project."""
        resp = await self._client.get(
            f"/api/v1/projects/{self._project_id}/sip-inbound-trunks"
        )
        resp.raise_for_status()
        return [SIPInboundTrunk.model_validate(t) for t in resp.json()]

    async def set_inbound_trunk_enabled(
        self, trunk_id: Union[str, UUID], enabled: bool
    ) -> SIPInboundTrunk:
        """Enables or disables an inbound trunk."""
        resp = await self._client.patch(
            f"/api/v1/projects/{self._project_id}/sip-inbound-trunks/{trunk_id}/enabled",
            params={"enabled": enabled},
        )
        resp.raise_for_status()
        return SIPInboundTrunk.model_validate(resp.json())
    
    async def update_inbound_trunk(
        self,
        trunk_id: Union[str, UUID],
        name: Optional[str] = None,
        numbers: Optional[List[str]] = None,
        allowed_addresses: Optional[List[str]] = None,
    ) -> SIPInboundTrunk:
        """Updates an existing inbound trunk."""
        payload = {
            k: v for k, v in {
                "name": name,
                "numbers": numbers,
                "allowed_addresses": allowed_addresses,
            }.items() if v is not None
        }

        resp = await self._client.patch(
            f"/api/v1/projects/{self._project_id}/sip-inbound-trunks/{trunk_id}",
            json=payload,
        )
        resp.raise_for_status()
        return SIPInboundTrunk.model_validate(resp.json())

    async def delete_inbound_trunk(self, trunk_id: Union[str, UUID]) -> None:
        """Deletes an inbound trunk and cleans up O(1) routing."""
        resp = await self._client.delete(
            f"/api/v1/projects/{self._project_id}/sip-inbound-trunks/{trunk_id}"
        )
        resp.raise_for_status()

    # ── Outbound Trunks ───────────────────────────────────────────────────────

    async def create_outbound_trunk(
        self,
        name: str,
        address: str,
        transport: SIPTransport = SIPTransport.AUTO,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> SIPOutboundTrunk:
        """Registers an outbound SIP Trunk with credentials for PSTN termination."""
        payload = CreateOutboundTrunkRequest(
            name=name,
            address=address,
            transport=transport,
            username=username,
            password=password,
        ).model_dump(exclude_none=True)

        resp = await self._client.post(
            f"/api/v1/projects/{self._project_id}/sip-outbound-trunks",
            json=payload,
        )
        resp.raise_for_status()
        return SIPOutboundTrunk.model_validate(resp.json())

    async def list_outbound_trunks(self) -> List[SIPOutboundTrunk]:
        """Lists all outbound trunks for the project."""
        resp = await self._client.get(
            f"/api/v1/projects/{self._project_id}/sip-outbound-trunks"
        )
        resp.raise_for_status()
        return [SIPOutboundTrunk.model_validate(t) for t in resp.json()]

    async def set_outbound_trunk_enabled(
        self, trunk_id: Union[str, UUID], enabled: bool
    ) -> SIPOutboundTrunk:
        """Enables or disables an outbound trunk."""
        resp = await self._client.patch(
            f"/api/v1/projects/{self._project_id}/sip-outbound-trunks/{trunk_id}/enabled",
            params={"enabled": enabled},
        )
        resp.raise_for_status()
        return SIPOutboundTrunk.model_validate(resp.json())
    
    async def update_outbound_trunk(
        self,
        trunk_id: Union[str, UUID],
        name: Optional[str] = None,
        address: Optional[str] = None,
        transport: Optional[SIPTransport] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> SIPOutboundTrunk:
        """Updates an existing outbound trunk."""
        payload = {
            k: v for k, v in {
                "name": name,
                "address": address,
                "transport": transport,
                "username": username,
                "password": password,
            }.items() if v is not None
        }

        resp = await self._client.patch(
            f"/api/v1/projects/{self._project_id}/sip-outbound-trunks/{trunk_id}",
            json=payload,
        )
        resp.raise_for_status()
        return SIPOutboundTrunk.model_validate(resp.json())

    async def delete_outbound_trunk(self, trunk_id: Union[str, UUID]) -> None:
        """Deletes an outbound trunk."""
        resp = await self._client.delete(
            f"/api/v1/projects/{self._project_id}/sip-outbound-trunks/{trunk_id}"
        )
        resp.raise_for_status()