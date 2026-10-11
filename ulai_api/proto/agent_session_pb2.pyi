from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Speaker(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPEAKER_UNSPECIFIED: _ClassVar[Speaker]
    SPEAKER_CALLER: _ClassVar[Speaker]
    SPEAKER_AGENT: _ClassVar[Speaker]

class AgentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_STATE_UNSPECIFIED: _ClassVar[AgentState]
    AGENT_STATE_LISTENING: _ClassVar[AgentState]
    AGENT_STATE_THINKING: _ClassVar[AgentState]
    AGENT_STATE_SPEAKING: _ClassVar[AgentState]

class Pipeline(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PIPELINE_UNSPECIFIED: _ClassVar[Pipeline]
    PIPELINE_REALTIME: _ClassVar[Pipeline]
    PIPELINE_SEMI_CASCADE: _ClassVar[Pipeline]
    PIPELINE_CASCADE: _ClassVar[Pipeline]

class OpeningTurn(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPENING_TURN_UNSPECIFIED: _ClassVar[OpeningTurn]
    OPENING_TURN_AGENT: _ClassVar[OpeningTurn]
    OPENING_TURN_CALLER: _ClassVar[OpeningTurn]

class TurnDetection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TURN_DETECTION_UNSPECIFIED: _ClassVar[TurnDetection]
    TURN_DETECTION_SERVER: _ClassVar[TurnDetection]
    TURN_DETECTION_CLIENT: _ClassVar[TurnDetection]
SPEAKER_UNSPECIFIED: Speaker
SPEAKER_CALLER: Speaker
SPEAKER_AGENT: Speaker
AGENT_STATE_UNSPECIFIED: AgentState
AGENT_STATE_LISTENING: AgentState
AGENT_STATE_THINKING: AgentState
AGENT_STATE_SPEAKING: AgentState
PIPELINE_UNSPECIFIED: Pipeline
PIPELINE_REALTIME: Pipeline
PIPELINE_SEMI_CASCADE: Pipeline
PIPELINE_CASCADE: Pipeline
OPENING_TURN_UNSPECIFIED: OpeningTurn
OPENING_TURN_AGENT: OpeningTurn
OPENING_TURN_CALLER: OpeningTurn
TURN_DETECTION_UNSPECIFIED: TurnDetection
TURN_DETECTION_SERVER: TurnDetection
TURN_DETECTION_CLIENT: TurnDetection

class JoinBridgeRequest(_message.Message):
    __slots__ = ("agent_id", "bridge_id", "participant_id", "custom_fields_json", "opening", "control_plane_url", "control_plane_api_key", "profile")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_JSON_FIELD_NUMBER: _ClassVar[int]
    OPENING_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_URL_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_API_KEY_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    bridge_id: str
    participant_id: str
    custom_fields_json: str
    opening: OpeningTurn
    control_plane_url: str
    control_plane_api_key: str
    profile: AgentProfile
    def __init__(self, agent_id: _Optional[str] = ..., bridge_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., custom_fields_json: _Optional[str] = ..., opening: _Optional[_Union[OpeningTurn, str]] = ..., control_plane_url: _Optional[str] = ..., control_plane_api_key: _Optional[str] = ..., profile: _Optional[_Union[AgentProfile, _Mapping]] = ...) -> None: ...

class JoinBridgeResponse(_message.Message):
    __slots__ = ("bridge_id", "agent_id", "participant_id", "connection_id", "node_address")
    BRIDGE_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    bridge_id: str
    agent_id: str
    participant_id: str
    connection_id: str
    node_address: str
    def __init__(self, bridge_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., connection_id: _Optional[str] = ..., node_address: _Optional[str] = ...) -> None: ...

class DisconnectRequest(_message.Message):
    __slots__ = ("bridge_id", "participant_id", "reason", "force")
    BRIDGE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    bridge_id: str
    participant_id: str
    reason: str
    force: bool
    def __init__(self, bridge_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., reason: _Optional[str] = ..., force: bool = ...) -> None: ...

class DisconnectResponse(_message.Message):
    __slots__ = ("was_connected", "duration_ms", "played_ms")
    WAS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYED_MS_FIELD_NUMBER: _ClassVar[int]
    was_connected: bool
    duration_ms: int
    played_ms: int
    def __init__(self, was_connected: bool = ..., duration_ms: _Optional[int] = ..., played_ms: _Optional[int] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ("agent_ids", "client_name")
    AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    agent_ids: _containers.RepeatedScalarFieldContainer[str]
    client_name: str
    def __init__(self, agent_ids: _Optional[_Iterable[str]] = ..., client_name: _Optional[str] = ...) -> None: ...

class Assignment(_message.Message):
    __slots__ = ("session_id", "call", "attach_deadline_ms")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    ATTACH_DEADLINE_MS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    call: CallInfo
    attach_deadline_ms: int
    def __init__(self, session_id: _Optional[str] = ..., call: _Optional[_Union[CallInfo, _Mapping]] = ..., attach_deadline_ms: _Optional[int] = ...) -> None: ...

class ClientEvent(_message.Message):
    __slots__ = ("attach", "say", "generate_reply", "inject_context", "tool_result", "interrupt", "hangup", "handled_tools")
    ATTACH_FIELD_NUMBER: _ClassVar[int]
    SAY_FIELD_NUMBER: _ClassVar[int]
    GENERATE_REPLY_FIELD_NUMBER: _ClassVar[int]
    INJECT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TOOL_RESULT_FIELD_NUMBER: _ClassVar[int]
    INTERRUPT_FIELD_NUMBER: _ClassVar[int]
    HANGUP_FIELD_NUMBER: _ClassVar[int]
    HANDLED_TOOLS_FIELD_NUMBER: _ClassVar[int]
    attach: Attach
    say: Say
    generate_reply: GenerateReply
    inject_context: InjectContext
    tool_result: ToolResult
    interrupt: Interrupt
    hangup: Hangup
    handled_tools: HandledTools
    def __init__(self, attach: _Optional[_Union[Attach, _Mapping]] = ..., say: _Optional[_Union[Say, _Mapping]] = ..., generate_reply: _Optional[_Union[GenerateReply, _Mapping]] = ..., inject_context: _Optional[_Union[InjectContext, _Mapping]] = ..., tool_result: _Optional[_Union[ToolResult, _Mapping]] = ..., interrupt: _Optional[_Union[Interrupt, _Mapping]] = ..., hangup: _Optional[_Union[Hangup, _Mapping]] = ..., handled_tools: _Optional[_Union[HandledTools, _Mapping]] = ...) -> None: ...

class HandledTools(_message.Message):
    __slots__ = ("names",)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...

class Attach(_message.Message):
    __slots__ = ("session_id", "profile", "replay_history")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    REPLAY_HISTORY_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    profile: AgentProfile
    replay_history: bool
    def __init__(self, session_id: _Optional[str] = ..., profile: _Optional[_Union[AgentProfile, _Mapping]] = ..., replay_history: bool = ...) -> None: ...

class Say(_message.Message):
    __slots__ = ("text", "allow_interruptions")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_INTERRUPTIONS_FIELD_NUMBER: _ClassVar[int]
    text: str
    allow_interruptions: bool
    def __init__(self, text: _Optional[str] = ..., allow_interruptions: bool = ...) -> None: ...

class GenerateReply(_message.Message):
    __slots__ = ("instructions",)
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    instructions: str
    def __init__(self, instructions: _Optional[str] = ...) -> None: ...

class InjectContext(_message.Message):
    __slots__ = ("text", "role")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    text: str
    role: str
    def __init__(self, text: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class ToolResult(_message.Message):
    __slots__ = ("id", "name", "result_json")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    result_json: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., result_json: _Optional[str] = ...) -> None: ...

class Interrupt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Hangup(_message.Message):
    __slots__ = ("reason", "speak_closing")
    REASON_FIELD_NUMBER: _ClassVar[int]
    SPEAK_CLOSING_FIELD_NUMBER: _ClassVar[int]
    reason: str
    speak_closing: bool
    def __init__(self, reason: _Optional[str] = ..., speak_closing: bool = ...) -> None: ...

class ServerEvent(_message.Message):
    __slots__ = ("sequence", "elapsed_ms", "session_started", "transcript", "turn_started", "turn_ended", "agent_state", "tool_call", "usage", "session_ended", "error")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_MS_FIELD_NUMBER: _ClassVar[int]
    SESSION_STARTED_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    TURN_STARTED_FIELD_NUMBER: _ClassVar[int]
    TURN_ENDED_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATE_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENDED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    elapsed_ms: int
    session_started: SessionStarted
    transcript: Transcript
    turn_started: TurnStarted
    turn_ended: TurnEnded
    agent_state: AgentStateChanged
    tool_call: ToolCall
    usage: UsageReport
    session_ended: SessionEnded
    error: ClientError
    def __init__(self, sequence: _Optional[int] = ..., elapsed_ms: _Optional[int] = ..., session_started: _Optional[_Union[SessionStarted, _Mapping]] = ..., transcript: _Optional[_Union[Transcript, _Mapping]] = ..., turn_started: _Optional[_Union[TurnStarted, _Mapping]] = ..., turn_ended: _Optional[_Union[TurnEnded, _Mapping]] = ..., agent_state: _Optional[_Union[AgentStateChanged, _Mapping]] = ..., tool_call: _Optional[_Union[ToolCall, _Mapping]] = ..., usage: _Optional[_Union[UsageReport, _Mapping]] = ..., session_ended: _Optional[_Union[SessionEnded, _Mapping]] = ..., error: _Optional[_Union[ClientError, _Mapping]] = ...) -> None: ...

class SessionStarted(_message.Message):
    __slots__ = ("session_id", "call", "backend", "profile")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    call: CallInfo
    backend: BackendInfo
    profile: AgentProfile
    def __init__(self, session_id: _Optional[str] = ..., call: _Optional[_Union[CallInfo, _Mapping]] = ..., backend: _Optional[_Union[BackendInfo, _Mapping]] = ..., profile: _Optional[_Union[AgentProfile, _Mapping]] = ...) -> None: ...

class Transcript(_message.Message):
    __slots__ = ("speaker", "text", "final")
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FINAL_FIELD_NUMBER: _ClassVar[int]
    speaker: Speaker
    text: str
    final: bool
    def __init__(self, speaker: _Optional[_Union[Speaker, str]] = ..., text: _Optional[str] = ..., final: bool = ...) -> None: ...

class TurnStarted(_message.Message):
    __slots__ = ("speaker", "turn_id")
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    speaker: Speaker
    turn_id: str
    def __init__(self, speaker: _Optional[_Union[Speaker, str]] = ..., turn_id: _Optional[str] = ...) -> None: ...

class TurnEnded(_message.Message):
    __slots__ = ("speaker", "turn_id", "duration_ms", "transcript", "interrupted", "heard_ms")
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    INTERRUPTED_FIELD_NUMBER: _ClassVar[int]
    HEARD_MS_FIELD_NUMBER: _ClassVar[int]
    speaker: Speaker
    turn_id: str
    duration_ms: int
    transcript: str
    interrupted: bool
    heard_ms: int
    def __init__(self, speaker: _Optional[_Union[Speaker, str]] = ..., turn_id: _Optional[str] = ..., duration_ms: _Optional[int] = ..., transcript: _Optional[str] = ..., interrupted: bool = ..., heard_ms: _Optional[int] = ...) -> None: ...

class AgentStateChanged(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: AgentState
    def __init__(self, state: _Optional[_Union[AgentState, str]] = ...) -> None: ...

class ToolCall(_message.Message):
    __slots__ = ("id", "name", "args_json")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_JSON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    args_json: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., args_json: _Optional[str] = ...) -> None: ...

class UsageReport(_message.Message):
    __slots__ = ("prompt_total", "prompt_cached", "response_total", "prompt", "response")
    PROMPT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_CACHED_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    prompt_total: int
    prompt_cached: int
    response_total: int
    prompt: _containers.RepeatedCompositeFieldContainer[ModalityTokens]
    response: _containers.RepeatedCompositeFieldContainer[ModalityTokens]
    def __init__(self, prompt_total: _Optional[int] = ..., prompt_cached: _Optional[int] = ..., response_total: _Optional[int] = ..., prompt: _Optional[_Iterable[_Union[ModalityTokens, _Mapping]]] = ..., response: _Optional[_Iterable[_Union[ModalityTokens, _Mapping]]] = ...) -> None: ...

class ModalityTokens(_message.Message):
    __slots__ = ("modality", "tokens")
    MODALITY_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    modality: str
    tokens: int
    def __init__(self, modality: _Optional[str] = ..., tokens: _Optional[int] = ...) -> None: ...

class SessionEnded(_message.Message):
    __slots__ = ("reason", "disposition", "duration_ms", "played_ms")
    REASON_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYED_MS_FIELD_NUMBER: _ClassVar[int]
    reason: str
    disposition: str
    duration_ms: int
    played_ms: int
    def __init__(self, reason: _Optional[str] = ..., disposition: _Optional[str] = ..., duration_ms: _Optional[int] = ..., played_ms: _Optional[int] = ...) -> None: ...

class ClientError(_message.Message):
    __slots__ = ("sequence_ref", "message")
    SEQUENCE_REF_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sequence_ref: int
    message: str
    def __init__(self, sequence_ref: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class CallInfo(_message.Message):
    __slots__ = ("call_id", "agent_id", "direction", "from_number", "to_number", "custom_fields_json")
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    FROM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TO_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_JSON_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    agent_id: str
    direction: str
    from_number: str
    to_number: str
    custom_fields_json: str
    def __init__(self, call_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., direction: _Optional[str] = ..., from_number: _Optional[str] = ..., to_number: _Optional[str] = ..., custom_fields_json: _Optional[str] = ...) -> None: ...

class BackendInfo(_message.Message):
    __slots__ = ("provider", "model", "pipeline", "turn_detection")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    TURN_DETECTION_FIELD_NUMBER: _ClassVar[int]
    provider: str
    model: str
    pipeline: Pipeline
    turn_detection: TurnDetection
    def __init__(self, provider: _Optional[str] = ..., model: _Optional[str] = ..., pipeline: _Optional[_Union[Pipeline, str]] = ..., turn_detection: _Optional[_Union[TurnDetection, str]] = ...) -> None: ...

class AgentProfile(_message.Message):
    __slots__ = ("prompt", "greeting", "closing", "voice", "model", "language", "temperature", "tools", "allow_interruptions", "greeting_interruptible", "max_call_duration_seconds", "persona_text", "opening", "backchannel_gate", "silence_monitor", "initial_engagement_deadline_ms", "background_noise", "workspace_id", "live_transcription", "ai_backend", "ai_classify_backend", "ai_transcribe_model", "gemini_project_id", "gemini_location", "google_credentials_json", "amd_enabled", "audio_nothing", "lost_utterance_replay")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    GREETING_FIELD_NUMBER: _ClassVar[int]
    CLOSING_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_INTERRUPTIONS_FIELD_NUMBER: _ClassVar[int]
    GREETING_INTERRUPTIBLE_FIELD_NUMBER: _ClassVar[int]
    MAX_CALL_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PERSONA_TEXT_FIELD_NUMBER: _ClassVar[int]
    OPENING_FIELD_NUMBER: _ClassVar[int]
    BACKCHANNEL_GATE_FIELD_NUMBER: _ClassVar[int]
    SILENCE_MONITOR_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ENGAGEMENT_DEADLINE_MS_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_NOISE_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_TRANSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AI_BACKEND_FIELD_NUMBER: _ClassVar[int]
    AI_CLASSIFY_BACKEND_FIELD_NUMBER: _ClassVar[int]
    AI_TRANSCRIBE_MODEL_FIELD_NUMBER: _ClassVar[int]
    GEMINI_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    GEMINI_LOCATION_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CREDENTIALS_JSON_FIELD_NUMBER: _ClassVar[int]
    AMD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUDIO_NOTHING_FIELD_NUMBER: _ClassVar[int]
    LOST_UTTERANCE_REPLAY_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    greeting: str
    closing: str
    voice: str
    model: str
    language: str
    temperature: float
    tools: _containers.RepeatedCompositeFieldContainer[ToolSpec]
    allow_interruptions: bool
    greeting_interruptible: bool
    max_call_duration_seconds: int
    persona_text: str
    opening: OpeningTurn
    backchannel_gate: bool
    silence_monitor: bool
    initial_engagement_deadline_ms: int
    background_noise: bool
    workspace_id: str
    live_transcription: bool
    ai_backend: str
    ai_classify_backend: str
    ai_transcribe_model: str
    gemini_project_id: str
    gemini_location: str
    google_credentials_json: str
    amd_enabled: bool
    audio_nothing: bool
    lost_utterance_replay: bool
    def __init__(self, prompt: _Optional[str] = ..., greeting: _Optional[str] = ..., closing: _Optional[str] = ..., voice: _Optional[str] = ..., model: _Optional[str] = ..., language: _Optional[str] = ..., temperature: _Optional[float] = ..., tools: _Optional[_Iterable[_Union[ToolSpec, _Mapping]]] = ..., allow_interruptions: bool = ..., greeting_interruptible: bool = ..., max_call_duration_seconds: _Optional[int] = ..., persona_text: _Optional[str] = ..., opening: _Optional[_Union[OpeningTurn, str]] = ..., backchannel_gate: bool = ..., silence_monitor: bool = ..., initial_engagement_deadline_ms: _Optional[int] = ..., background_noise: bool = ..., workspace_id: _Optional[str] = ..., live_transcription: bool = ..., ai_backend: _Optional[str] = ..., ai_classify_backend: _Optional[str] = ..., ai_transcribe_model: _Optional[str] = ..., gemini_project_id: _Optional[str] = ..., gemini_location: _Optional[str] = ..., google_credentials_json: _Optional[str] = ..., amd_enabled: bool = ..., audio_nothing: bool = ..., lost_utterance_replay: bool = ...) -> None: ...

class ToolSpec(_message.Message):
    __slots__ = ("name", "description", "parameters", "required")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ToolParam
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ToolParam, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters: _containers.MessageMap[str, ToolParam]
    required: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., parameters: _Optional[_Mapping[str, ToolParam]] = ..., required: _Optional[_Iterable[str]] = ...) -> None: ...

class ToolParam(_message.Message):
    __slots__ = ("type", "description", "enum")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    type: str
    description: str
    enum: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., description: _Optional[str] = ..., enum: _Optional[_Iterable[str]] = ...) -> None: ...
