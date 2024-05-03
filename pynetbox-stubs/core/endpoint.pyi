from typing import Any, Dict, Iterable, Optional, Tuple

from pynetbox.core.response import Record, RecordSet

RESERVED_KWARGS: Tuple[Any]

class Endpoint:
    def __init__(self, api, app, name, model=None):
        self.name = name.replace("_", "-")
        self.api = api
        self.base_url = api.base_url
        self.token = api.token
        self.session_key = api.session_key
        self.url: str

    def all(self, limit=0, offset=None) -> RecordSet: ...
    def get(self, *args, **kwargs: Optional[Any]) -> Record: ...
    def filter(self, *args, **kwargs: Optional[Any]) -> RecordSet: ...
    def create(self, *args, **kwargs: Optional[Any]) -> Record: ...
    def update(self, objects: Iterable[Record]) -> RecordSet: ...
    def delete(self, objects: Iterable[Record]) -> bool: ...
    def choices(self) -> dict: ...
    def count(self, *args, **kwargs: Optional[Any]) -> int: ...

class DetailEndpoint:
    parent_obj: Optional[Any]
    custom_return: Optional[Record]
    url: Optional[str]
    request_kwargs: Optional[Any]
    def __init__(
        self,
        parent_obj: Optional[Any],
        name: Optional[str],
        custom_return: Optional[Record],
    ) -> None: ...
    def list(self, **kwargs) -> Record | RecordSet: ...
    def create(self, data: Optional[Dict]) -> Record | RecordSet: ...

class RODetailEndpoint(DetailEndpoint):
    def create(self, data: Optional[Any]) -> None: ...
