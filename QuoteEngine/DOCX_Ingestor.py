"""Parses text from Docx files and returns a list of Quote objects."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .Quote import Quote


class DocxIngestor(IngestorInterface):
    """Docx file ingestor."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parse text from Docx file.

        Parses text from docx file and transforms text
        into Quote class objects.

        :param path: Path to a Docx file.
        :return: List of Quote objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Invalid file type')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split('-')
                new_quote = Quote(parsed[0], parsed[1])
                quotes.append(new_quote)

        return quotes
