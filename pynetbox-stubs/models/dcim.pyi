from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import Record
from typing import Any, Sequence, Type

class TraceableRecord(Record):
    def trace(self) -> Sequence[Sequence[Record]]: ...

class Devices(Record):
    has_details: bool
    device_type: Any
    primary_ip: Any
    primary_ip4: Any
    primary_ip6: Any
    local_context_data: Any
    config_context: Any
    @property
    def napalm(self): ...

class ConnectedEndpoint(Record):
    device: Any

class Interfaces(TraceableRecord):
    interface_connection: Type[Record]
    connected_endpoint: Type[ConnectedEndpoint]

class PowerOutlets(TraceableRecord):
    device: Any

class PowerPorts(TraceableRecord):
    device: Any

class ConsolePorts(TraceableRecord):
    device: Any

class ConsoleServerPorts(TraceableRecord):
    device: Any

class VirtualChassis(Record):
    master: Any

class RUs(Record):
    device: Any

class FrontPorts(TraceableRecord):
    device: Any

class RearPorts(TraceableRecord):
    device: Any

class Racks(Record):
    @property
    def units(self) -> Endpoint: ...
    @property
    def elevation(self) -> Endpoint: ...

class Termination(Record):
    device: Any
    circuit: Any

class Cables(Record):
    termination_a: Any
    termination_b: Any
