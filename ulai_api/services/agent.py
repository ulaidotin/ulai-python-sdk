import grpc
import urllib.parse
from typing import Optional

# These will be generated when you compile agent-session.proto
try:
    from ..proto import agent_session_pb2
    from ..proto import agent_session_pb2_grpc
except ImportError:
    # Handle the case where the proto files haven't been compiled yet
    agent_session_pb2 = None
    agent_session_pb2_grpc = None


class AgentService:
    def __init__(self, control_plane_url: str, api_key: Optional[str] = None):
        """
        Initializes the AgentService using the control plane address.
        """
        self.control_plane_url = control_plane_url
        self.api_key = api_key
        
        # Parse the host:port from the url
        parsed = urllib.parse.urlparse(control_plane_url)
        host = parsed.hostname or control_plane_url
        port = parsed.port or (443 if parsed.scheme == "https" else 80)
        self.channel_addr = f"{host}:{port}"

        # Assuming secure channel if https, otherwise insecure
        if parsed.scheme == "https":
            credentials = grpc.ssl_channel_credentials()
            self.channel = grpc.aio.secure_channel(self.channel_addr, credentials)
        else:
            self.channel = grpc.aio.insecure_channel(self.channel_addr)
            
        if agent_session_pb2_grpc:
            # According to the porting guide, there are three services:
            # AgentBridge, AgentSession, AgentDispatch
            # We initialize stubs for them if the generated files exist
            self.bridge_stub = agent_session_pb2_grpc.AgentBridgeStub(self.channel)
            self.session_stub = agent_session_pb2_grpc.AgentSessionStub(self.channel)
            self.dispatch_stub = agent_session_pb2_grpc.AgentDispatchStub(self.channel)
        else:
            self.bridge_stub = None
            self.session_stub = None
            self.dispatch_stub = None

    def _get_metadata(self):
        metadata = ()
        if self.api_key:
            metadata = (("x-api-key", self.api_key),)
        return metadata

    async def join_bridge(self, room: str, agent_id: str, participant_id: str):
        """
        Client.Join returning a Seat
        """
        if not self.bridge_stub:
            raise NotImplementedError("gRPC stubs not found. Please compile agent-session.proto.")
            
        req = agent_session_pb2.JoinBridgeRequest(
            bridge_id=room,
            agent_id=agent_id,
            participant_id=participant_id,
            control_plane_url=self.control_plane_url,
            control_plane_api_key=self.api_key or ""
        )
        return await self.bridge_stub.Join(req, metadata=self._get_metadata())

    async def leave_bridge(self, room: str, participant_id: str):
        """
        Client.Leave
        """
        if not self.bridge_stub:
            raise NotImplementedError("gRPC stubs not found. Please compile agent-session.proto.")

        req = agent_session_pb2.DisconnectRequest(
            bridge_id=room,
            participant_id=participant_id
        )
        return await self.bridge_stub.Disconnect(req, metadata=self._get_metadata())
    
    def subscribe(self, agent_ids: list, client_name: str):
        """
        Client.Assignments returning a stream of Assignment
        """
        if not self.dispatch_stub:
            raise NotImplementedError("gRPC stubs not found. Please compile agent-session.proto.")
            
        req = agent_session_pb2.SubscribeRequest(
            agent_ids=agent_ids,
            client_name=client_name
        )
        return self.dispatch_stub.Subscribe(req, metadata=self._get_metadata())

    def run(self, request_iterator):
        """
        Client.Attach returning a bidirectional stream (Session)
        Pass an async generator yielding ClientEvent objects.
        """
        if not self.session_stub:
            raise NotImplementedError("gRPC stubs not found. Please compile agent-session.proto.")
            
        return self.session_stub.Run(request_iterator, metadata=self._get_metadata())

    async def close(self):
        await self.channel.close()
