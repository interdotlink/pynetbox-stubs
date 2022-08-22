from typing import Optional

from pynetbox.core.app import App


class Api:
    def __init__(
        self,
        url: str,
        token: Optional[str]=None,
        private_key: Optional[str]=None,
        private_key_file: Optional[str]=None,
        threading: bool=False,
    ):
        self.dcim = App(self, "dcim")
        self.ipam = App(self, "ipam")
        self.circuits = App(self, "circuits")
        self.secrets = App(self, "secrets")
        self.tenancy = App(self, "tenancy")
        self.extras = App(self, "extras")
        self.virtualization = App(self, "virtualization")
        self.users = App(self, "users")
        self.wireless = App(self, "wireless")
        self.plugins = PluginsApp(self)

    @property
    def version(self) -> str: ...
    def openapi(self) -> dict: ...
    def status(self) -> dict: ...
    def create_token(self, username: str, password: str) -> str: ...
