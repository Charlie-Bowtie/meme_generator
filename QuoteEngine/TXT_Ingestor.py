"""Extract text from txt file and return list of Quote object."""

from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class TextIngestor(IngestorInterface):
    """Txt file Ingestor."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parse text from txt file.

        Parses text from txt file and transforms text
        into Quote class objects.

        :param path: Path to a txt object.
        :return: List of Quote objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Invalid file type')

        quotes = []

        with open(path, encoding='utf-8-sig') as infile:
            contents = infile.readlines()

            for line in contents:
                lines = line.split('-')
                new_quote = Quote(lines[0], lines[1])
                quotes.append(new_quote)

        return quotes
