from pynetbox.core.response import JsonField, Record
from pynetbox.models.ipam import IpAddresses

class VirtualMachines(Record):
    primary_ip: IpAddresses
    primary_ip4: IpAddresses
    primary_ip6: IpAddresses
    config_context: JsonField
