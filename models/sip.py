from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class SIPTransport(str, Enum):
    AUTO = "auto"
    UDP = "udp"
    TCP = "tcp"
    TLS = "tls"


class SIPInboundTrunk(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    name: str
    enabled: bool
    numbers: Optional[List[str]] = None
    allowed_addresses: Optional[List[str]] = None


class CreateInboundTrunkRequest(BaseModel):
    name: str
    numbers: Optional[List[str]] = None
    allowed_addresses: Optional[List[str]] = None


class SIPOutboundTrunk(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    name: str
    enabled: bool
    address: str
    transport: SIPTransport
    username: Optional[str] = None


class CreateOutboundTrunkRequest(BaseModel):
    name: str
    address: str
    transport: SIPTransport = SIPTransport.AUTO
    username: Optional[str] = None
    password: Optional[str] = None