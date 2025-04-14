from typing import TypeVar, Generic


K = TypeVar("K")
V = TypeVar("T")


class Mapper(Generic[K, V]):
    def __init__(self):
        self._mapping: dict[K, V] = {}

    def bind(self, k: K, v: V):
        self._mapping[k] = v

    def unbind(self, k: K):
        if self._mapping.get(k):
            self._mapping.pop(k)

    def get(self, k: K):
        return self._mapping.get(k)