from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel, ConfigDict


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
    events_token: Optional[str] = None
    node: NodeInfo


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