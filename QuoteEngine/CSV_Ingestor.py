"""Parses text from CSV files and returns a list of Quote objects."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class CSVIngestor(IngestorInterface):
    """CSV file Ingestor."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parse text from CSV file.

        Parses text from CSV file and transforms text
        into Quote class objects.

        :param path: Path to a CSV file.
        :return: List of Quote objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Invalid file type')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = Quote(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
