from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pynetbox.api import Api

class App:
    def __init__(self, api: 'Api', name):
        self.api = api
        self.name = name
