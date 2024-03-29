from pynetbox.core.endpoint import DetailEndpoint
from pynetbox.core.response import Record

class IpAddresses(Record): ...

class IpRanges(Record):
    @property
    def available_ips(self) -> DetailEndpoint: ...

class Prefixes(Record):
    @property
    def available_ips(self) -> DetailEndpoint: ...
    @property
    def available_prefixes(self) -> DetailEndpoint: ...

class Aggregates(Record): ...
class Vlans(Record): ...

class VlanGroups(Record):
    @property
    def available_vlans(self) -> DetailEndpoint: ...
