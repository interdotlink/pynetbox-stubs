from typing import TYPE_CHECKING, Dict, List

from pynetbox._gen.bgp import BgpApp
from pynetbox.core.endpoint import Endpoint

if TYPE_CHECKING:
    from pynetbox.core.api import Api

class App:
    api: "Api"
    name: str
    models: Dict
    def __init__(self, api: "Api", name: str):
        self.api = api
        self.name = name
    def __getattr__(self, name: str) -> Endpoint: ...
    def config(self) -> str: ...

class PluginsApp:
    def __init__(self, api: "Api"):
        self.api = api
        self.bgp = BgpApp(self.api, "bgp")
    def __getattr__(self, key) -> Endpoint: ...
    def installed_plugins(self) -> List: ...
