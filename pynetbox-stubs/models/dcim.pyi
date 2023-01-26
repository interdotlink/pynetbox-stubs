from typing import Any, List, Sequence, Type

from pynetbox.core.endpoint import RODetailEndpoint
from pynetbox.core.response import JsonField, Record
from pynetbox.models.circuits import Circuits
from pynetbox.models.ipam import IpAddresses

class TraceableRecord(Record):
    def trace(self) -> Sequence[Sequence[Record]]: ...

class DeviceTypes(Record): ...

class Devices(Record):
    has_details: bool
    device_type: DeviceTypes
    primary_ip: IpAddresses
    primary_ip4: IpAddresses
    primary_ip6: IpAddresses
    local_context_data: JsonField
    config_context: JsonField
    @property
    def napalm(self) -> RODetailEndpoint: ...

class InterfaceConnections(Record): ...
class InterfaceConnection(Record): ...

class ConnectedEndpoint(Record):
    device: Any

class Interfaces(TraceableRecord):
    id: int
    interface_connection: Type[Record]
    connected_endpoint: Type[ConnectedEndpoint]
    enabled: bool
    mac_address: str
    mtu: int
    mode: str
    parent: int
    bridge: int
    vdcs: List
    lag: int
    type: str
    mgmt_only: bool
    speed: int
    duplex: str
    wwn: str
    rf_role: str
    rf_channel: str
    rf_channel_frequency: float
    rf_channel_width: float
    tx_power: int
    poe_mode: str
    poe_type: str
    wireless_link: int
    wireless_lans: List
    untagged_vlan: int
    tagged_vlans: List
    vrf: int
    ip_addresses: IpAddresses
    fhrp_group_assignments: Any
    l2vpn_terminations: Any

class PowerOutlets(TraceableRecord):
    device: Any

class PowerPorts(TraceableRecord):
    device: Any

class ConsolePorts(TraceableRecord):
    device: Any

class ConsoleServerPorts(TraceableRecord):
    device: Any

class RackReservations(Record): ...

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
    def units(self) -> RODetailEndpoint: ...
    @property
    def elevation(self) -> RODetailEndpoint: ...

class Termination(Record):
    device: Devices
    circuit: Circuits

class Cables(Record):
    termination_a: Any
    termination_b: Any
