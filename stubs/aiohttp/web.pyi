from typing import Awaitable, Callable, AsyncIterable
from . import WSMessage

class HTTPNotFound(Exception): ...

class BaseRequest:
    path: str

class Response:
    def __init__(self, *, text: str = None, content_type: str = None) -> None: ...

class Server:
    def __init__(self, handler: Callable[[BaseRequest], Awaitable[Response]]) -> None: ...

class WebSocketResponse(Response, AsyncIterable[WSMessage]):
    def __init__(self, autoclose: bool = True) -> None: ...
    def __aiter__(self) -> 'WSMessage': ...  # type: ignore
    async def __anext__(self) -> WSMessage: ...
    async def prepare(self, request: BaseRequest) -> None: ...
    async def send_str(self, data: str): ...
