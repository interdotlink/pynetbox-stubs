from typing import TYPE_CHECKING

from pynetbox._gen.bgp import BgpApp
from pynetbox.core.endpoint import Endpoint

if TYPE_CHECKING:
    from pynetbox.core.api import Api

class App:
    def __init__(self, api: "Api", name: str):
        self.api = api
        self.name = name

class PluginsApp:
    def __init__(self, api: "Api"):
        self.api = api
        self.bgp = BgpApp(self.api, "bgp")
    def __getattr__(self, key) -> Endpoint: ...
