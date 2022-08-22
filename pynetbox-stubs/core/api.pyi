from typing import Optional

from pynetbox._gen.circuits import CircuitsApp
from pynetbox._gen.dcim import DcimApp
from pynetbox._gen.extras import ExtrasApp
from pynetbox._gen.ipam import IpamApp
from pynetbox._gen.tenancy import TenancyApp
from pynetbox._gen.users import UsersApp
from pynetbox._gen.virtualization import VirtualizationApp
from pynetbox._gen.wireless import WirelessApp
from pynetbox.core.app import App


class PluginsApp:
    pass


class Api:
    def __init__(
        self,
        url: str,
        token: Optional[str]=None,
        private_key: Optional[str]=None,
        private_key_file: Optional[str]=None,
        threading: bool=False,
    ):
        self.dcim = DcimApp(self, "dcim")
        self.ipam = IpamApp(self, "ipam")
        self.circuits = CircuitsApp(self, "circuits")
        self.secrets = App(self, "secrets")
        self.tenancy = TenancyApp(self, "tenancy")
        self.extras = ExtrasApp(self, "extras")
        self.virtualization = VirtualizationApp(self, "virtualization")
        self.users = UsersApp(self, "users")
        self.wireless = WirelessApp(self, "wireless")
        self.plugins = PluginsApp(self)

    @property
    def version(self) -> str: ...
    def openapi(self) -> dict: ...
    def status(self) -> dict: ...
    def create_token(self, username: str, password: str) -> str: ...
