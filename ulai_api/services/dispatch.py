from typing import Any, Dict, List, Optional, Union
from uuid import UUID
import httpx

from ..models.dispatch import (
    DispatcherRule,
    CreateDispatcherRuleRequest,
    RuleType,
)


class DispatchService:
    """Manages Dispatcher Rules against Ulai Cloud Backend."""

    def __init__(self, client: httpx.AsyncClient, project_id: str):
        self._client = client
        self._project_id = project_id

    async def create_rule(
        self,
        name: str,
        rule_type: RuleType = RuleType.INDIVIDUAL,
        agent_name: Optional[str] = None,
        dispatch_metadata: Optional[Dict[str, Any]] = None,
        trunk_ids: Optional[List[str]] = None,
        phone_numbers: Optional[List[str]] = None,
    ) -> DispatcherRule:
        """
        Creates a new dispatcher rule. 
        If trunk_ids and phone_numbers are omitted, it acts as the fallback rule.
        """
        payload = CreateDispatcherRuleRequest(
            name=name,
            rule_type=rule_type,
            agent_name=agent_name,
            dispatch_metadata=dispatch_metadata,
            trunk_ids=trunk_ids,
            phone_numbers=phone_numbers,
        ).model_dump(exclude_none=True)

        resp = await self._client.post(
            f"/api/v1/projects/{self._project_id}/dispatcher-rules",
            json=payload,
        )
        resp.raise_for_status()
        return DispatcherRule.model_validate(resp.json())

    async def list_rules(self) -> List[DispatcherRule]:
        """Lists all dispatcher rules for the project."""
        resp = await self._client.get(
            f"/api/v1/projects/{self._project_id}/dispatcher-rules"
        )
        resp.raise_for_status()
        return [DispatcherRule.model_validate(r) for r in resp.json()]

    async def update_rule(
        self,
        rule_id: Union[str, UUID],
        name: Optional[str] = None,
        agent_name: Optional[str] = None,
        trunk_ids: Optional[List[str]] = None,
        phone_numbers: Optional[List[str]] = None,
    ) -> DispatcherRule:
        """Updates an existing dispatcher rule dynamically."""
        
        payload = {
            k: v for k, v in {
                "name": name,
                "agent_name": agent_name,
                "trunk_ids": trunk_ids,
                "phone_numbers": phone_numbers,
            }.items() if v is not None
        }

        resp = await self._client.patch(
            f"/api/v1/projects/{self._project_id}/dispatcher-rules/{rule_id}",
            json=payload,
        )
        resp.raise_for_status()
        return DispatcherRule.model_validate(resp.json())    

    async def delete_rule(self, rule_id: Union[str, UUID]) -> None:
        """Deletes a dispatcher rule and cleans up O(1) routing."""
        resp = await self._client.delete(
            f"/api/v1/projects/{self._project_id}/dispatcher-rules/{rule_id}"
        )
        resp.raise_for_status()