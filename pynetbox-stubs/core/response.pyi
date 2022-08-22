from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from pynetbox.core.app import App


class JsonField(object):
    ...

class RecordSet(object):
    def __init__(self, endpoint: 'App', request: str, **kwargs):
        self.endpoint = endpoint
        self.request = request

    def __iter__(self): ...
    def __next__(self): ...
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

class Record:

    pass