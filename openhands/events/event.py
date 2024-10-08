import datetime
from dataclasses import dataclass
from enum import Enum


class EventSource(str, Enum):
    AGENT = 'agent'
    USER = 'user'


@dataclass
class Event:
    @property
    def message(self) -> str | None:
        if hasattr(self, '_message'):
            return self._message  # type: ignore[attr-defined]
        return ''

    @property
    def id(self) -> int:
        if hasattr(self, '_id'):
            return self._id  # type: ignore[attr-defined]
        return -1

    @property
    def timestamp(self) -> datetime.datetime | None:
        if hasattr(self, '_timestamp'):
            return self._timestamp  # type: ignore[attr-defined]
        return None

    @property
    def source(self) -> EventSource | None:
        if hasattr(self, '_source'):
            return self._source  # type: ignore[attr-defined]
        return None

    @property
    def cause(self) -> int | None:
        if hasattr(self, '_cause'):
            return self._cause  # type: ignore[attr-defined]
        return None

    @property
    def timeout(self) -> int | None:
        if hasattr(self, '_timeout'):
            return self._timeout  # type: ignore[attr-defined]
        return None

    @timeout.setter
    def timeout(self, value: int | None) -> None:
        self._timeout = value

        # Check if .blocking is an attribute of the event
        if hasattr(self, 'blocking'):
            # .blocking needs to be set to True if .timeout is set
            self.blocking = True
