from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict


@dataclass
class BuilderApiKeyCreds:
    key: str
    secret: str
    passphrase: str


class BuilderType(Enum):
    UNAVAILABLE = "UNAVAILABLE"
    LOCAL = "LOCAL"
    REMOTE = "REMOTE"


@dataclass
class RemoteBuilderConfig:
    """Remote builder configuration"""

    url: str
    token: Optional[str] = None


@dataclass
class RemoteSignerPayload:
    """Remote signer payload"""

    method: str
    path: str
    body: Optional[str] = None
    timestamp: Optional[int] = None


@dataclass
class BuilderHeaderPayload:
    """Builder header payload"""

    KUEST_BUILDER_API_KEY: str
    KUEST_BUILDER_TIMESTAMP: str
    KUEST_BUILDER_PASSPHRASE: str
    KUEST_BUILDER_SIGNATURE: str

    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary for use as headers"""
        return {
            "KUEST_BUILDER_API_KEY": self.KUEST_BUILDER_API_KEY,
            "KUEST_BUILDER_TIMESTAMP": self.KUEST_BUILDER_TIMESTAMP,
            "KUEST_BUILDER_PASSPHRASE": self.KUEST_BUILDER_PASSPHRASE,
            "KUEST_BUILDER_SIGNATURE": self.KUEST_BUILDER_SIGNATURE,
        }
