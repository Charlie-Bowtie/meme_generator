"""
Generate Quote object from a variety of file formats.

This package parses text from a variety of file formats and
returns a list of Quote objects. The correct ingestor class
is automatically selected based on the file path given.
"""

from .DOCX_Ingestor import DocxIngestor
from .CSV_Ingestor import CSVIngestor
from .PDF_Ingestor import PDFIngestor
from .TXT_Ingestor import TextIngestor
from .Ingestor import Ingestor
from .Quote import Quote