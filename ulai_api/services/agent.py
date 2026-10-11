import json
import urllib.parse
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

import grpc

from ..proto import agent_session_pb2
from ..proto import agent_session_pb2_grpc


@dataclass
class Seat:
    """Represents an agent seat in a room bridge."""
    room: str
    agent_id: str
    participant_id: str
    connection_id: str
    node_address: str
    raw_response: Optional[Any] = None


class AgentService:
    def __init__(
        self,
        agent_url: str,
        control_plane_url: Optional[str] = None,
        api_key: Optional[str] = None
    ):
        """
        Initializes the AgentService using the agent orchestrator gRPC address.
        """
        self.agent_url = agent_url
        self.control_plane_url = control_plane_url or ""
        self.api_key = api_key
        
        raw_url = agent_url.strip()
        is_http = raw_url.startswith("http://")
        if "://" in raw_url:
            parsed = urllib.parse.urlparse(raw_url)
            host = parsed.hostname or raw_url
            port = parsed.port or (80 if is_http else 443)
        elif ":" in raw_url:
            parts = raw_url.split(":")
            host = parts[0]
            port = int(parts[1])
        else:
            host = raw_url
            port = 443

        self.channel_addr = f"{host}:{port}"

        if is_http:
            self.channel = grpc.aio.insecure_channel(self.channel_addr)
        else:
            credentials = grpc.ssl_channel_credentials()
            self.channel = grpc.aio.secure_channel(self.channel_addr, credentials)
            
        self.bridge_stub = agent_session_pb2_grpc.AgentBridgeStub(self.channel)
        self.session_stub = agent_session_pb2_grpc.AgentSessionStub(self.channel)
        self.dispatch_stub = agent_session_pb2_grpc.AgentDispatchStub(self.channel)

    def _get_metadata(self):
        metadata = ()
        if self.api_key:
            metadata = (("x-api-key", self.api_key),)
        return metadata

    @staticmethod
    def _resolve_opening_turn(val: Any) -> int:
        if val is None:
            return agent_session_pb2.OpeningTurn.OPENING_TURN_UNSPECIFIED
        if isinstance(val, int):
            return val
        if isinstance(val, str):
            v = val.lower().strip()
            if v in ("agent", "model"):
                return agent_session_pb2.OpeningTurn.OPENING_TURN_AGENT
            if v in ("caller", "user"):
                return agent_session_pb2.OpeningTurn.OPENING_TURN_CALLER
            return agent_session_pb2.OpeningTurn.OPENING_TURN_UNSPECIFIED
        if isinstance(val, dict):
            role = str(val.get("role", "")).lower()
            if role in ("caller", "user"):
                return agent_session_pb2.OpeningTurn.OPENING_TURN_CALLER
            return agent_session_pb2.OpeningTurn.OPENING_TURN_AGENT
        return agent_session_pb2.OpeningTurn.OPENING_TURN_AGENT

    async def join_bridge(
        self,
        room: str,
        agent_id: str,
        participant_id: str,
        profile: Optional[Union[Dict[str, Any], Any]] = None,
        opening: Optional[Any] = None,
        custom_fields: Optional[Dict[str, Any]] = None,
    ) -> Seat:
        """
        Joins an agent to a room bridge and returns a Seat.
        Maps all AgentProfile fields from ulai-agent-sdk / agent-session.proto.
        """
        req = agent_session_pb2.JoinBridgeRequest(
            bridge_id=room,
            agent_id=agent_id,
            participant_id=participant_id,
            control_plane_url=self.control_plane_url,
            control_plane_api_key=self.api_key or "",
        )
        
        if custom_fields:
            req.custom_fields_json = json.dumps(custom_fields)
            
        if opening is not None:
            req.opening = self._resolve_opening_turn(opening)

        if profile:
            def get_val(key: str, default: Any = None) -> Any:
                if isinstance(profile, dict):
                    return profile.get(key, default)
                return getattr(profile, key, default)

            # String fields
            string_fields = [
                "prompt", "greeting", "closing", "voice", "model",
                "language", "persona_text", "workspace_id", "ai_backend",
                "ai_classify_backend", "ai_transcribe_model", "gemini_project_id",
                "gemini_location", "google_credentials_json"
            ]
            for field in string_fields:
                val = get_val(field)
                if val is not None:
                    setattr(req.profile, field, str(val))

            # Primitive optional scalars
            temp = get_val("temperature")
            if temp is not None:
                req.profile.temperature = float(temp)

            allow_int = get_val("allow_interruptions")
            if allow_int is not None:
                req.profile.allow_interruptions = bool(allow_int)

            greet_int = get_val("greeting_interruptible")
            if greet_int is not None:
                req.profile.greeting_interruptible = bool(greet_int)

            max_dur = get_val("max_call_duration_seconds")
            if max_dur is None:
                max_dur = get_val("max_call_duration")
            if max_dur is not None:
                req.profile.max_call_duration_seconds = int(max_dur)

            backchannel = get_val("backchannel_gate")
            if backchannel is not None:
                req.profile.backchannel_gate = bool(backchannel)

            silence = get_val("silence_monitor")
            if silence is not None:
                req.profile.silence_monitor = bool(silence)

            bg_noise = get_val("background_noise")
            if bg_noise is not None:
                req.profile.background_noise = bool(bg_noise)

            live_trans = get_val("live_transcription")
            if live_trans is not None:
                req.profile.live_transcription = bool(live_trans)

            amd = get_val("amd_enabled")
            if amd is not None:
                req.profile.amd_enabled = bool(amd)

            audio_noth = get_val("audio_nothing")
            if audio_noth is not None:
                req.profile.audio_nothing = bool(audio_noth)

            lost_replay = get_val("lost_utterance_replay")
            if lost_replay is not None:
                req.profile.lost_utterance_replay = bool(lost_replay)

            init_deadline = get_val("initial_engagement_deadline_ms")
            if init_deadline is None and get_val("initial_engagement_deadline") is not None:
                init_deadline = int(get_val("initial_engagement_deadline")) * 1000
            if init_deadline is not None:
                req.profile.initial_engagement_deadline_ms = int(init_deadline)

            prof_opening = get_val("opening")
            if prof_opening is not None:
                req.profile.opening = self._resolve_opening_turn(prof_opening)

            # Tools
            tools_list = get_val("tools")
            if tools_list:
                for tool_data in tools_list:
                    tool_spec = req.profile.tools.add()
                    tool_spec.name = tool_data.get("name", "")
                    tool_spec.description = tool_data.get("description", "")
                    for req_field in tool_data.get("required", []):
                        tool_spec.required.append(req_field)
                    for p_key, p_val in tool_data.get("parameters", {}).items():
                        param_obj = tool_spec.parameters[p_key]
                        param_obj.type = p_val.get("type", "")
                        param_obj.description = p_val.get("description", "")
                        for enum_item in p_val.get("enum", []):
                            param_obj.enum.append(str(enum_item))

        resp = await self.bridge_stub.Join(req, metadata=self._get_metadata())
        return Seat(
            room=resp.bridge_id,
            agent_id=resp.agent_id,
            participant_id=resp.participant_id,
            connection_id=resp.connection_id,
            node_address=resp.node_address,
            raw_response=resp,
        )

    async def leave_bridge(self, room: str, participant_id: str, reason: str = "", force: bool = False):
        """
        Disconnects the agent from the bridge.
        """
        req = agent_session_pb2.DisconnectRequest(
            bridge_id=room,
            participant_id=participant_id,
            reason=reason,
            force=force,
        )
        return await self.bridge_stub.Disconnect(req, metadata=self._get_metadata())
    
    def subscribe(self, agent_ids: list, client_name: str):
        """
        Subscribes to assignments stream for given agents.
        """
        req = agent_session_pb2.SubscribeRequest(
            agent_ids=agent_ids,
            client_name=client_name
        )
        return self.dispatch_stub.Subscribe(req, metadata=self._get_metadata())

    def run(self, request_iterator):
        """
        Runs a bidirectional session stream. Pass an async generator yielding ClientEvent objects.
        """
        return self.session_stub.Run(request_iterator, metadata=self._get_metadata())

    async def close(self):
        await self.channel.close()
