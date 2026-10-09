import httpx
from typing import Dict, Optional
from ..models.sessions import Session, JoinInfo, ParticipantKind, SIPDirection

class SessionService:
    def __init__(self, client: httpx.AsyncClient):
        self._client = client

    async def create(self, max_participants: int = 8, metadata: Optional[Dict[str, str]] = None) -> str:
        """Provisions a new room and returns its session ID."""
        payload = {"max_participants": max_participants}
        if metadata:
            payload["metadata"] = metadata
            
        resp = await self._client.post("/api/v1/sessions", json=payload)
        resp.raise_for_status()
        return resp.json()["session_id"]

    async def get(self, session_id: str) -> Session:
        """Fetches the current state of a session."""
        resp = await self._client.get(f"/api/v1/sessions/{session_id}")
        resp.raise_for_status()
        return Session(**resp.json())

    async def join(
        self, 
        session_id: str, 
        participant_id: str = "", 
        kind: Optional[ParticipantKind] = None,
        sub_kind: Optional[str] = None,
        sip_direction: Optional[SIPDirection] = None,
        can_publish: Optional[bool] = None,
        can_subscribe: Optional[bool] = None,
        metadata: Optional[Dict[str, str]] = None
    ) -> JoinInfo:
        """Joins an existing session and returns connection tickets."""
        
        # SIP EXCLUSIVITY LOGIC
        if kind == ParticipantKind.SIP and not sip_direction:
            raise ValueError("sip_direction is strictly required when kind is SIP")
        if kind != ParticipantKind.SIP and sip_direction:
            raise ValueError("sip_direction can only be provided when kind is SIP")

        payload = {}
        if participant_id:
            payload["participant_id"] = participant_id
        if kind is not None:
            payload["kind"] = kind.value
        if sub_kind is not None:
            payload["sub_kind"] = sub_kind
        if sip_direction is not None:
            payload["sip_direction"] = sip_direction.value
        if can_publish is not None:
            payload["can_publish"] = can_publish
        if can_subscribe is not None:
            payload["can_subscribe"] = can_subscribe
        if metadata:
            payload["metadata"] = metadata
            
        resp = await self._client.post(f"/api/v1/sessions/{session_id}/join", json=payload)
        resp.raise_for_status()
        return JoinInfo(**resp.json())

    async def terminate(self, session_id: str) -> None:
        """Authoritatively ends a session for all participants."""
        resp = await self._client.delete(f"/api/v1/sessions/{session_id}")
        resp.raise_for_status()

    async def watch(self, session_id: str) -> str:
        """Mints an events token for a pure observer."""
        resp = await self._client.post(f"/api/v1/sessions/{session_id}/watch")
        resp.raise_for_status()
        return resp.json()["events_token"]