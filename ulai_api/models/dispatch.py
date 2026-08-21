from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class RuleType(str, Enum):
    INDIVIDUAL = "individual"
    RANDOM = "random"


class DispatcherRule(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    name: str
    rule_type: RuleType
    agent_name: Optional[str] = None
    dispatch_metadata: Optional[Dict[str, Any]] = None
    trunk_ids: Optional[List[str]] = None
    phone_numbers: Optional[List[str]] = None
    enabled: bool


class CreateDispatcherRuleRequest(BaseModel):
    name: str
    rule_type: RuleType = RuleType.INDIVIDUAL
    agent_name: Optional[str] = None
    dispatch_metadata: Optional[Dict[str, Any]] = None
    trunk_ids: Optional[List[str]] = None
    phone_numbers: Optional[List[str]] = None