from typing import Any, Dict, Iterator, Optional

from requests import Response

def calc_pages(limit: int, count: int) -> int: ...

class RequestError(Exception):
    message: str
    req: Response
    request_body: Response.request.body
    base: Response.url
    error: Response.text
    def __init__(self, req) -> None: ...

class AllocationError(Exception):
    req: Response
    request_body: Response.request.body
    base: Response.url
    error: str
    def __init__(self, req) -> None: ...

class ContentError(Exception):
    req: Response
    request_body: Response.request.body
    base: Response.url
    error: str
    def __init__(self, req) -> None: ...

class Request:
    def __init__(
        self,
        base: str,
        http_session: Any,
        filters: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        key: Optional[str] = None,
        token: Optional[str] = None,
        private_key: Optional[str] = None,
        session_key: Optional[str] = None,
        threading: bool = False,
    ):
        self.base = base
        self.filters = filters
        self.key = key
        self.token = token
        self.private_key = private_key
        self.session_key = session_key
        self.http_session = http_session
        self.url: str = ...
        self.threading = threading
        self.limit = limit
        self.offset = offset

    def get_openapi(self) -> dict: ...
    def get_version(self) -> str: ...
    def get_session_key(self) -> str: ...
    def get_status(self) -> dict: ...
    def normalize_url(self, url: str) -> str: ...
    def concurrent_get(
        self, ret: list, page_size: int, page_offsets: int
    ) -> None: ...
    def get(self, add_params: Optional[Dict[str, str]] = None) -> Iterator: ...
    def put(self, data: dict) -> bool: ...
    def post(self, data: dict) -> bool: ...
    def delete(self, data: Optional[dict] = None) -> bool: ...
    def patch(self, data: dict) -> bool: ...
    def options(self) -> bool: ...
    def get_count(self, *args: Any, **kwargs: Any) -> int: ...
