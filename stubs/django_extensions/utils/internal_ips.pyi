from collections.abc import Container
from typing import Any

class InternalIPS(Container):
    def __init__(self, iterable: Any, sort_by_size: bool = ...) -> None: ...
    def __contains__(self, address: Any): ...
    def __hash__(self) -> Any: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def iter_cidrs(self): ...
