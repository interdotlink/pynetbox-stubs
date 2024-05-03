from typing import Any, Dict, Iterable, List, Optional, Union, overload

from pynetbox._gen import definitions
from pynetbox.core.api import Api
from pynetbox.core.app import App
from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import Record, RecordSet

class ConfigEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[Record]: ...
    def get(self, **kwargs: Optional[Any]) -> Optional[Record]: ...
    def filter(self, **kwargs: Optional[Any]) -> RecordSet[Record]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> Record: ...
    @overload
    def create(
        self,
    ) -> Record: ...
    def create(self, *args: Dict[str, Any], **kwargs: Any) -> Record: ...
    def update(self, objects: Iterable[Record]) -> RecordSet[Record]: ...
    def delete(self, objects: Iterable[Record]) -> bool: ...
    def choices(self) -> dict: ...
    def count(self, **kwargs: Optional[Any]) -> int: ...

class GroupsEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[definitions.Group]: ...
    def get(
        self,
        id: Optional[int] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.Group]: ...
    def filter(
        self,
        id: Optional[int] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.Group]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.Group: ...
    @overload
    def create(self, name: str) -> definitions.Group: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.Group: ...
    def update(
        self, objects: Iterable[definitions.Group]
    ) -> RecordSet[definitions.Group]: ...
    def delete(self, objects: Iterable[definitions.Group]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[int] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class PermissionsEndpoint(Endpoint):
    def all(
        self, limit=0, offset=None
    ) -> RecordSet[definitions.ObjectPermission]: ...
    def get(
        self,
        id: Optional[int] = None,
        can_add: Optional[bool] = None,
        can_change: Optional[bool] = None,
        can_delete: Optional[bool] = None,
        can_view: Optional[bool] = None,
        description: Optional[str] = None,
        description__empty: Optional[bool] = None,
        description__ic: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__n: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__nie: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__nisw: Optional[str] = None,
        enabled: Optional[bool] = None,
        group: Optional[str] = None,
        group__n: Optional[str] = None,
        group_id: Optional[int] = None,
        group_id__n: Optional[int] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        object_types: Optional[int] = None,
        object_types__n: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        user: Optional[str] = None,
        user__n: Optional[str] = None,
        user_id: Optional[int] = None,
        user_id__n: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.ObjectPermission]: ...
    def filter(
        self,
        id: Optional[int] = None,
        can_add: Optional[bool] = None,
        can_change: Optional[bool] = None,
        can_delete: Optional[bool] = None,
        can_view: Optional[bool] = None,
        description: Optional[str] = None,
        description__empty: Optional[bool] = None,
        description__ic: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__n: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__nie: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__nisw: Optional[str] = None,
        enabled: Optional[bool] = None,
        group: Optional[str] = None,
        group__n: Optional[str] = None,
        group_id: Optional[int] = None,
        group_id__n: Optional[int] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        object_types: Optional[int] = None,
        object_types__n: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        user: Optional[str] = None,
        user__n: Optional[str] = None,
        user_id: Optional[int] = None,
        user_id__n: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.ObjectPermission]: ...
    @overload
    def create(
        self, *args: Dict[str, Any]
    ) -> definitions.ObjectPermission: ...
    @overload
    def create(
        self,
        name: str,
        object_types: List[Any],
        actions: List[Any],
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        groups: Optional[List[Any]] = None,
        users: Optional[List[Any]] = None,
        constraints: Optional[Any] = None,
    ) -> definitions.ObjectPermission: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.ObjectPermission: ...
    def update(
        self, objects: Iterable[definitions.ObjectPermission]
    ) -> RecordSet[definitions.ObjectPermission]: ...
    def delete(
        self, objects: Iterable[definitions.ObjectPermission]
    ) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[int] = None,
        can_add: Optional[bool] = None,
        can_change: Optional[bool] = None,
        can_delete: Optional[bool] = None,
        can_view: Optional[bool] = None,
        description: Optional[str] = None,
        description__empty: Optional[bool] = None,
        description__ic: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__n: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__nie: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__nisw: Optional[str] = None,
        enabled: Optional[bool] = None,
        group: Optional[str] = None,
        group__n: Optional[str] = None,
        group_id: Optional[int] = None,
        group_id__n: Optional[int] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        object_types: Optional[int] = None,
        object_types__n: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        user: Optional[str] = None,
        user__n: Optional[str] = None,
        user_id: Optional[int] = None,
        user_id__n: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class TokensEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[definitions.Token]: ...
    def get(
        self,
        id: Optional[int] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        description: Optional[str] = None,
        description__empty: Optional[bool] = None,
        description__ic: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__n: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__nie: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__nisw: Optional[str] = None,
        expires: Optional[str] = None,
        expires__gte: Optional[str] = None,
        expires__lte: Optional[str] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        key: Optional[str] = None,
        key__empty: Optional[bool] = None,
        key__ic: Optional[str] = None,
        key__ie: Optional[str] = None,
        key__iew: Optional[str] = None,
        key__isw: Optional[str] = None,
        key__n: Optional[str] = None,
        key__nic: Optional[str] = None,
        key__nie: Optional[str] = None,
        key__niew: Optional[str] = None,
        key__nisw: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        user: Optional[str] = None,
        user__n: Optional[str] = None,
        user_id: Optional[int] = None,
        user_id__n: Optional[int] = None,
        write_enabled: Optional[bool] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.Token]: ...
    def filter(
        self,
        id: Optional[int] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        description: Optional[str] = None,
        description__empty: Optional[bool] = None,
        description__ic: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__n: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__nie: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__nisw: Optional[str] = None,
        expires: Optional[str] = None,
        expires__gte: Optional[str] = None,
        expires__lte: Optional[str] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        key: Optional[str] = None,
        key__empty: Optional[bool] = None,
        key__ic: Optional[str] = None,
        key__ie: Optional[str] = None,
        key__iew: Optional[str] = None,
        key__isw: Optional[str] = None,
        key__n: Optional[str] = None,
        key__nic: Optional[str] = None,
        key__nie: Optional[str] = None,
        key__niew: Optional[str] = None,
        key__nisw: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        user: Optional[str] = None,
        user__n: Optional[str] = None,
        user_id: Optional[int] = None,
        user_id__n: Optional[int] = None,
        write_enabled: Optional[bool] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.Token]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.Token: ...
    @overload
    def create(
        self,
        user: int,
        expires: Optional[str] = None,
        last_used: Optional[str] = None,
        key: Optional[str] = None,
        write_enabled: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> definitions.Token: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.Token: ...
    def update(
        self, objects: Iterable[definitions.Token]
    ) -> RecordSet[definitions.Token]: ...
    def delete(self, objects: Iterable[definitions.Token]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[int] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        description: Optional[str] = None,
        description__empty: Optional[bool] = None,
        description__ic: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__n: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__nie: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__nisw: Optional[str] = None,
        expires: Optional[str] = None,
        expires__gte: Optional[str] = None,
        expires__lte: Optional[str] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        key: Optional[str] = None,
        key__empty: Optional[bool] = None,
        key__ic: Optional[str] = None,
        key__ie: Optional[str] = None,
        key__iew: Optional[str] = None,
        key__isw: Optional[str] = None,
        key__n: Optional[str] = None,
        key__nic: Optional[str] = None,
        key__nie: Optional[str] = None,
        key__niew: Optional[str] = None,
        key__nisw: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        user: Optional[str] = None,
        user__n: Optional[str] = None,
        user_id: Optional[int] = None,
        user_id__n: Optional[int] = None,
        write_enabled: Optional[bool] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class Tokens_provisionEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[Record]: ...
    def get(self, **kwargs: Optional[Any]) -> Optional[Record]: ...
    def filter(self, **kwargs: Optional[Any]) -> RecordSet[Record]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> Record: ...
    @overload
    def create(
        self,
        username: str,
        password: str,
        expires: Optional[str] = None,
        write_enabled: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> Record: ...
    def create(self, *args: Dict[str, Any], **kwargs: Any) -> Record: ...
    def update(self, objects: Iterable[Record]) -> RecordSet[Record]: ...
    def delete(self, objects: Iterable[Record]) -> bool: ...
    def choices(self) -> dict: ...
    def count(self, **kwargs: Optional[Any]) -> int: ...

class UsersEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[definitions.User]: ...
    def get(
        self,
        id: Optional[int] = None,
        email: Optional[str] = None,
        email__empty: Optional[bool] = None,
        email__ic: Optional[str] = None,
        email__ie: Optional[str] = None,
        email__iew: Optional[str] = None,
        email__isw: Optional[str] = None,
        email__n: Optional[str] = None,
        email__nic: Optional[str] = None,
        email__nie: Optional[str] = None,
        email__niew: Optional[str] = None,
        email__nisw: Optional[str] = None,
        first_name: Optional[str] = None,
        first_name__empty: Optional[bool] = None,
        first_name__ic: Optional[str] = None,
        first_name__ie: Optional[str] = None,
        first_name__iew: Optional[str] = None,
        first_name__isw: Optional[str] = None,
        first_name__n: Optional[str] = None,
        first_name__nic: Optional[str] = None,
        first_name__nie: Optional[str] = None,
        first_name__niew: Optional[str] = None,
        first_name__nisw: Optional[str] = None,
        group: Optional[str] = None,
        group__n: Optional[str] = None,
        group_id: Optional[int] = None,
        group_id__n: Optional[int] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        is_active: Optional[bool] = None,
        is_staff: Optional[bool] = None,
        is_superuser: Optional[bool] = None,
        last_name: Optional[str] = None,
        last_name__empty: Optional[bool] = None,
        last_name__ic: Optional[str] = None,
        last_name__ie: Optional[str] = None,
        last_name__iew: Optional[str] = None,
        last_name__isw: Optional[str] = None,
        last_name__n: Optional[str] = None,
        last_name__nic: Optional[str] = None,
        last_name__nie: Optional[str] = None,
        last_name__niew: Optional[str] = None,
        last_name__nisw: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        username: Optional[str] = None,
        username__empty: Optional[bool] = None,
        username__ic: Optional[str] = None,
        username__ie: Optional[str] = None,
        username__iew: Optional[str] = None,
        username__isw: Optional[str] = None,
        username__n: Optional[str] = None,
        username__nic: Optional[str] = None,
        username__nie: Optional[str] = None,
        username__niew: Optional[str] = None,
        username__nisw: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.User]: ...
    def filter(
        self,
        id: Optional[int] = None,
        email: Optional[str] = None,
        email__empty: Optional[bool] = None,
        email__ic: Optional[str] = None,
        email__ie: Optional[str] = None,
        email__iew: Optional[str] = None,
        email__isw: Optional[str] = None,
        email__n: Optional[str] = None,
        email__nic: Optional[str] = None,
        email__nie: Optional[str] = None,
        email__niew: Optional[str] = None,
        email__nisw: Optional[str] = None,
        first_name: Optional[str] = None,
        first_name__empty: Optional[bool] = None,
        first_name__ic: Optional[str] = None,
        first_name__ie: Optional[str] = None,
        first_name__iew: Optional[str] = None,
        first_name__isw: Optional[str] = None,
        first_name__n: Optional[str] = None,
        first_name__nic: Optional[str] = None,
        first_name__nie: Optional[str] = None,
        first_name__niew: Optional[str] = None,
        first_name__nisw: Optional[str] = None,
        group: Optional[str] = None,
        group__n: Optional[str] = None,
        group_id: Optional[int] = None,
        group_id__n: Optional[int] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        is_active: Optional[bool] = None,
        is_staff: Optional[bool] = None,
        is_superuser: Optional[bool] = None,
        last_name: Optional[str] = None,
        last_name__empty: Optional[bool] = None,
        last_name__ic: Optional[str] = None,
        last_name__ie: Optional[str] = None,
        last_name__iew: Optional[str] = None,
        last_name__isw: Optional[str] = None,
        last_name__n: Optional[str] = None,
        last_name__nic: Optional[str] = None,
        last_name__nie: Optional[str] = None,
        last_name__niew: Optional[str] = None,
        last_name__nisw: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        username: Optional[str] = None,
        username__empty: Optional[bool] = None,
        username__ic: Optional[str] = None,
        username__ie: Optional[str] = None,
        username__iew: Optional[str] = None,
        username__isw: Optional[str] = None,
        username__n: Optional[str] = None,
        username__nic: Optional[str] = None,
        username__nie: Optional[str] = None,
        username__niew: Optional[str] = None,
        username__nisw: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.User]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.User: ...
    @overload
    def create(
        self,
        username: str,
        password: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        is_staff: Optional[bool] = None,
        is_active: Optional[bool] = None,
        date_joined: Optional[str] = None,
        last_login: Optional[str] = None,
        groups: Optional[List[Any]] = None,
    ) -> definitions.User: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.User: ...
    def update(
        self, objects: Iterable[definitions.User]
    ) -> RecordSet[definitions.User]: ...
    def delete(self, objects: Iterable[definitions.User]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[int] = None,
        email: Optional[str] = None,
        email__empty: Optional[bool] = None,
        email__ic: Optional[str] = None,
        email__ie: Optional[str] = None,
        email__iew: Optional[str] = None,
        email__isw: Optional[str] = None,
        email__n: Optional[str] = None,
        email__nic: Optional[str] = None,
        email__nie: Optional[str] = None,
        email__niew: Optional[str] = None,
        email__nisw: Optional[str] = None,
        first_name: Optional[str] = None,
        first_name__empty: Optional[bool] = None,
        first_name__ic: Optional[str] = None,
        first_name__ie: Optional[str] = None,
        first_name__iew: Optional[str] = None,
        first_name__isw: Optional[str] = None,
        first_name__n: Optional[str] = None,
        first_name__nic: Optional[str] = None,
        first_name__nie: Optional[str] = None,
        first_name__niew: Optional[str] = None,
        first_name__nisw: Optional[str] = None,
        group: Optional[str] = None,
        group__n: Optional[str] = None,
        group_id: Optional[int] = None,
        group_id__n: Optional[int] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        is_active: Optional[bool] = None,
        is_staff: Optional[bool] = None,
        is_superuser: Optional[bool] = None,
        last_name: Optional[str] = None,
        last_name__empty: Optional[bool] = None,
        last_name__ic: Optional[str] = None,
        last_name__ie: Optional[str] = None,
        last_name__iew: Optional[str] = None,
        last_name__isw: Optional[str] = None,
        last_name__n: Optional[str] = None,
        last_name__nic: Optional[str] = None,
        last_name__nie: Optional[str] = None,
        last_name__niew: Optional[str] = None,
        last_name__nisw: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        username: Optional[str] = None,
        username__empty: Optional[bool] = None,
        username__ic: Optional[str] = None,
        username__ie: Optional[str] = None,
        username__iew: Optional[str] = None,
        username__isw: Optional[str] = None,
        username__n: Optional[str] = None,
        username__nic: Optional[str] = None,
        username__nie: Optional[str] = None,
        username__niew: Optional[str] = None,
        username__nisw: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class UsersApp(App):
    def __init__(self, api: 'Api', name):
        self.config: ConfigEndpoint = ...
        self.groups: GroupsEndpoint = ...
        self.permissions: PermissionsEndpoint = ...
        self.tokens: TokensEndpoint = ...
        self.tokens_provision: Tokens_provisionEndpoint = ...
        self.users: UsersEndpoint = ...
