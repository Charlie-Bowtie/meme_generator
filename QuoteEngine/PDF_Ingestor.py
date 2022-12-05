"""Parse text from PDF files and return a list of Quote objects."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class PDFIngestor(IngestorInterface):
    """PDF file Ingestor."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parse text from PDF file.

        Parses text from PDF file and transforms text
        into Quote class objects.

        :param path: Path to a PDF file.
        :return: List of Quote objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Invalid file type')

        tmp = f'.{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', '-raw', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = Quote(parse[0], parse[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
