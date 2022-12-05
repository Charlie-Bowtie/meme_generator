"""Parent class of Ingestor objects."""

from abc import ABC, abstractmethod
from typing import List
from .Quote import Quote


class IngestorInterface(ABC):
    """Abstract Ingestor class.

    Serves as an abstact parent class for ingestors of
    content from various file formats.

    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Check if file can be ingested.

        Parses file extension from end of file and checks
        if it is in the allowed_extensions list.

        :param path: Path to a file.
        :return: Boolean representing whether file can be ingested.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parse text from file.

        Concrete subclasses must overide this method to parse
        text from the supplied file type

        :param path: Path to a file object.
        :return: List of Quote objects.
        """
        pass
