"""Automatically selects correct ingestor class for file type."""

from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import Quote
from .DOCX_Ingestor import DocxIngestor
from .CSV_Ingestor import CSVIngestor
from .PDF_Ingestor import PDFIngestor
from .TXT_Ingestor import TextIngestor


class Ingestor(IngestorInterface):
    """Strategy object for ingestor classes."""

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parse text from file.

        The method checks which ingestor class can ingest the file.
        It then uses the valid ingestor class parse method to
        parse text from the file and transform the text
        into Quote class objects.

        :param path: Path to a txt object.
        :return: List of Quote objects.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
