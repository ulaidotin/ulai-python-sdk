from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel, ConfigDict
from enum import Enum


class ParticipantKind(str, Enum):
    STANDARD = "STANDARD"
    AGENT = "AGENT"
    SIP = "SIP"
    TRANSCRIBER = "TRANSCRIBER"
    RECORDER = "RECORDER"

class SIPDirection(str, Enum):
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"

class NodeInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    address: str


class JoinInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    session_id: str
    participant_id: str
    connection_id: str
    ticket: str
    node: NodeInfo
    webrtc_url: Optional[str] = None
    ws_url: Optional[str] = None
    events_token: Optional[str] = None


class Session(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    assigned_node: str
    assigned_node_id: str
    status: str
    created_at: datetime
    expires_at: datetime
    max_participants: int
    participant_count: int
    metadata: Optional[Dict[str, str]] = None