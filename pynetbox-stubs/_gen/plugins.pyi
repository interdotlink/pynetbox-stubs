from typing import Any, Dict, Iterable, List, Optional, Union, overload

from pynetbox._gen import definitions
from pynetbox.core.api import Api
from pynetbox.core.app import App
from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import Record, RecordSet

class Bgp_bgppeergroupEndpoint(Endpoint):
    def all(
        self, limit=0, offset=None
    ) -> RecordSet[definitions.BGPPeerGroup]: ...
    def get(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.BGPPeerGroup]: ...
    def filter(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.BGPPeerGroup]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.BGPPeerGroup: ...
    @overload
    def create(
        self,
        name: str,
        description: str,
        id: Optional[int | int] = None,
        tags: Optional[List[Any]] = None,
        custom_fields: Optional[Any] = None,
        display: Optional[str] = None,
        import_policies: Optional[List[Any]] = None,
        export_policies: Optional[List[Any]] = None,
        created: Optional[str] = None,
        last_updated: Optional[str] = None,
        custom_field_data: Optional[Any] = None,
    ) -> definitions.BGPPeerGroup: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.BGPPeerGroup: ...
    def update(
        self, objects: Iterable[definitions.BGPPeerGroup]
    ) -> RecordSet[definitions.BGPPeerGroup]: ...
    def delete(self, objects: Iterable[definitions.BGPPeerGroup]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class Bgp_bgpsessionEndpoint(Endpoint):
    def all(
        self, limit=0, offset=None
    ) -> RecordSet[definitions.BGPSession]: ...
    def get(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        tenant: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        remote_as: Optional[str] = None,
        remote_as_id: Optional[str | int] = None,
        local_as: Optional[str] = None,
        local_as_id: Optional[str | int] = None,
        peer_group: Optional[str] = None,
        import_policies: Optional[str] = None,
        export_policies: Optional[str] = None,
        local_address_id: Optional[str | int] = None,
        local_address: Optional[str] = None,
        remote_address_id: Optional[str | int] = None,
        remote_address: Optional[str] = None,
        device_id: Optional[str | int] = None,
        device: Optional[str] = None,
        by_remote_address: Optional[str] = None,
        by_local_address: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.BGPSession]: ...
    def filter(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        tenant: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        remote_as: Optional[str] = None,
        remote_as_id: Optional[str | int] = None,
        local_as: Optional[str] = None,
        local_as_id: Optional[str | int] = None,
        peer_group: Optional[str] = None,
        import_policies: Optional[str] = None,
        export_policies: Optional[str] = None,
        local_address_id: Optional[str | int] = None,
        local_address: Optional[str] = None,
        remote_address_id: Optional[str | int] = None,
        remote_address: Optional[str] = None,
        device_id: Optional[str | int] = None,
        device: Optional[str] = None,
        by_remote_address: Optional[str] = None,
        by_local_address: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.BGPSession]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.BGPSession: ...
    @overload
    def create(
        self,
        local_address: int,
        remote_address: int,
        local_as: int,
        remote_as: int,
        id: Optional[int | int] = None,
        tags: Optional[List[Any]] = None,
        custom_fields: Optional[Any] = None,
        display: Optional[str] = None,
        import_policies: Optional[List[Any]] = None,
        export_policies: Optional[List[Any]] = None,
        created: Optional[str] = None,
        last_updated: Optional[str] = None,
        custom_field_data: Optional[Any] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        description: Optional[str] = None,
        site: Optional[int] = None,
        tenant: Optional[int] = None,
        device: Optional[int] = None,
        peer_group: Optional[int] = None,
    ) -> definitions.BGPSession: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.BGPSession: ...
    def update(
        self, objects: Iterable[definitions.BGPSession]
    ) -> RecordSet[definitions.BGPSession]: ...
    def delete(self, objects: Iterable[definitions.BGPSession]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        tenant: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        remote_as: Optional[str] = None,
        remote_as_id: Optional[str | int] = None,
        local_as: Optional[str] = None,
        local_as_id: Optional[str | int] = None,
        peer_group: Optional[str] = None,
        import_policies: Optional[str] = None,
        export_policies: Optional[str] = None,
        local_address_id: Optional[str | int] = None,
        local_address: Optional[str] = None,
        remote_address_id: Optional[str | int] = None,
        remote_address: Optional[str] = None,
        device_id: Optional[str | int] = None,
        device: Optional[str] = None,
        by_remote_address: Optional[str] = None,
        by_local_address: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class Bgp_communityEndpoint(Endpoint):
    def all(
        self, limit=0, offset=None
    ) -> RecordSet[definitions.Community]: ...
    def get(
        self,
        value: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        tenant: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.Community]: ...
    def filter(
        self,
        value: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        tenant: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.Community]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.Community: ...
    @overload
    def create(
        self,
        value: str,
        id: Optional[int | int] = None,
        tags: Optional[List[Any]] = None,
        custom_fields: Optional[Any] = None,
        display: Optional[str] = None,
        created: Optional[str] = None,
        last_updated: Optional[str] = None,
        custom_field_data: Optional[Any] = None,
        status: Optional[str] = None,
        description: Optional[str] = None,
        site: Optional[int] = None,
        tenant: Optional[int] = None,
        role: Optional[int] = None,
    ) -> definitions.Community: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.Community: ...
    def update(
        self, objects: Iterable[definitions.Community]
    ) -> RecordSet[definitions.Community]: ...
    def delete(self, objects: Iterable[definitions.Community]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        value: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        tenant: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class Bgp_peer_groupEndpoint(Endpoint):
    def all(
        self, limit=0, offset=None
    ) -> RecordSet[definitions.BGPPeerGroup]: ...
    def get(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.BGPPeerGroup]: ...
    def filter(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.BGPPeerGroup]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.BGPPeerGroup: ...
    @overload
    def create(
        self,
        name: str,
        description: str,
        id: Optional[int | int] = None,
        tags: Optional[List[Any]] = None,
        custom_fields: Optional[Any] = None,
        display: Optional[str] = None,
        import_policies: Optional[List[Any]] = None,
        export_policies: Optional[List[Any]] = None,
        created: Optional[str] = None,
        last_updated: Optional[str] = None,
        custom_field_data: Optional[Any] = None,
    ) -> definitions.BGPPeerGroup: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.BGPPeerGroup: ...
    def update(
        self, objects: Iterable[definitions.BGPPeerGroup]
    ) -> RecordSet[definitions.BGPPeerGroup]: ...
    def delete(self, objects: Iterable[definitions.BGPPeerGroup]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class Bgp_prefix_listEndpoint(Endpoint):
    def all(
        self, limit=0, offset=None
    ) -> RecordSet[definitions.PrefixList]: ...
    def get(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.PrefixList]: ...
    def filter(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.PrefixList]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.PrefixList: ...
    @overload
    def create(
        self,
        name: str,
        description: str,
        family: str,
        id: Optional[int | int] = None,
        tags: Optional[List[Any]] = None,
        custom_fields: Optional[Any] = None,
        display: Optional[str] = None,
        created: Optional[str] = None,
        last_updated: Optional[str] = None,
        custom_field_data: Optional[Any] = None,
    ) -> definitions.PrefixList: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.PrefixList: ...
    def update(
        self, objects: Iterable[definitions.PrefixList]
    ) -> RecordSet[definitions.PrefixList]: ...
    def delete(self, objects: Iterable[definitions.PrefixList]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class Bgp_routing_policyEndpoint(Endpoint):
    def all(
        self, limit=0, offset=None
    ) -> RecordSet[definitions.RoutingPolicy]: ...
    def get(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.RoutingPolicy]: ...
    def filter(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.RoutingPolicy]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.RoutingPolicy: ...
    @overload
    def create(
        self,
        name: str,
        description: str,
        id: Optional[int | int] = None,
        tags: Optional[List[Any]] = None,
        custom_fields: Optional[Any] = None,
        display: Optional[str] = None,
        created: Optional[str] = None,
        last_updated: Optional[str] = None,
        custom_field_data: Optional[Any] = None,
    ) -> definitions.RoutingPolicy: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.RoutingPolicy: ...
    def update(
        self, objects: Iterable[definitions.RoutingPolicy]
    ) -> RecordSet[definitions.RoutingPolicy]: ...
    def delete(self, objects: Iterable[definitions.RoutingPolicy]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class Bgp_sessionEndpoint(Endpoint):
    def all(
        self, limit=0, offset=None
    ) -> RecordSet[definitions.BGPSession]: ...
    def get(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        tenant: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        remote_as: Optional[str] = None,
        remote_as_id: Optional[str | int] = None,
        local_as: Optional[str] = None,
        local_as_id: Optional[str | int] = None,
        peer_group: Optional[str] = None,
        import_policies: Optional[str] = None,
        export_policies: Optional[str] = None,
        local_address_id: Optional[str | int] = None,
        local_address: Optional[str] = None,
        remote_address_id: Optional[str | int] = None,
        remote_address: Optional[str] = None,
        device_id: Optional[str | int] = None,
        device: Optional[str] = None,
        by_remote_address: Optional[str] = None,
        by_local_address: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.BGPSession]: ...
    def filter(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        tenant: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        remote_as: Optional[str] = None,
        remote_as_id: Optional[str | int] = None,
        local_as: Optional[str] = None,
        local_as_id: Optional[str | int] = None,
        peer_group: Optional[str] = None,
        import_policies: Optional[str] = None,
        export_policies: Optional[str] = None,
        local_address_id: Optional[str | int] = None,
        local_address: Optional[str] = None,
        remote_address_id: Optional[str | int] = None,
        remote_address: Optional[str] = None,
        device_id: Optional[str | int] = None,
        device: Optional[str] = None,
        by_remote_address: Optional[str] = None,
        by_local_address: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.BGPSession]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.BGPSession: ...
    @overload
    def create(
        self,
        local_address: int,
        remote_address: int,
        local_as: int,
        remote_as: int,
        id: Optional[int | int] = None,
        tags: Optional[List[Any]] = None,
        custom_fields: Optional[Any] = None,
        display: Optional[str] = None,
        import_policies: Optional[List[Any]] = None,
        export_policies: Optional[List[Any]] = None,
        created: Optional[str] = None,
        last_updated: Optional[str] = None,
        custom_field_data: Optional[Any] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        description: Optional[str] = None,
        site: Optional[int] = None,
        tenant: Optional[int] = None,
        device: Optional[int] = None,
        peer_group: Optional[int] = None,
    ) -> definitions.BGPSession: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.BGPSession: ...
    def update(
        self, objects: Iterable[definitions.BGPSession]
    ) -> RecordSet[definitions.BGPSession]: ...
    def delete(self, objects: Iterable[definitions.BGPSession]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        tenant: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        remote_as: Optional[str] = None,
        remote_as_id: Optional[str | int] = None,
        local_as: Optional[str] = None,
        local_as_id: Optional[str | int] = None,
        peer_group: Optional[str] = None,
        import_policies: Optional[str] = None,
        export_policies: Optional[str] = None,
        local_address_id: Optional[str | int] = None,
        local_address: Optional[str] = None,
        remote_address_id: Optional[str | int] = None,
        remote_address: Optional[str] = None,
        device_id: Optional[str | int] = None,
        device: Optional[str] = None,
        by_remote_address: Optional[str] = None,
        by_local_address: Optional[str] = None,
        ordering: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class PluginsApp(App):
    def __init__(self, api: 'Api', name):
        self.bgp_bgppeergroup: Bgp_bgppeergroupEndpoint = ...
        self.bgp_bgpsession: Bgp_bgpsessionEndpoint = ...
        self.bgp_community: Bgp_communityEndpoint = ...
        self.bgp_peer_group: Bgp_peer_groupEndpoint = ...
        self.bgp_prefix_list: Bgp_prefix_listEndpoint = ...
        self.bgp_routing_policy: Bgp_routing_policyEndpoint = ...
        self.bgp_session: Bgp_sessionEndpoint = ...
