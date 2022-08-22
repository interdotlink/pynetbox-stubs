from typing import Optional, TYPE_CHECKING, Generic, TypeVar, Self, Iterator

if TYPE_CHECKING:
    from pynetbox.core.app import App


class JsonField(object):
    ...

R = TypeVar('R', bound='Record')

class RecordSet(Iterator[R]):
    def __init__(self, endpoint: 'App', request: str, **kwargs):
        self.endpoint = endpoint
        self.request = request

    def __iter__(self) -> RecordSet[R]: ...
    def __next__(self) -> R: ...
    def __len__(self) -> int: ...
    def update(self, **kwargs) -> Optional[Record]: ...
    def delete(self):
        r"""Bulk deletes objects in a RecordSet.

        Allows for batch deletion of multiple objects in a RecordSet

        :returns: True if bulk DELETE operation was successful.

        :Examples:

        Deleting offline `devices` on site 1:

        >>> netbox.dcim.devices.filter(site_id=1, status="offline").delete()
        >>>
        """
        return self.endpoint.delete(self)

class Record(object):
    def __init__(self, values, api, endpoint):
        self.has_details = False
        self.api = api
        self.default_ret = Record
        self.endpoint: Endpoint
        self.url: Optional[str]

    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> str: ...
    def __eq__(self, other: Self) -> bool: ...
    def full_details(self) -> bool: ...
    def serialize(self, nested: bool, init: bool) -> dict: ...
    def updates(self) -> dict: ...
    def save(self) -> bool: ...
    def update(self, data: dict) -> bool: ...
    def delete(self) -> bool: ...
