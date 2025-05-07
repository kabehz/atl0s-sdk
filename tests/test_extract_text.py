from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import pytesseract
import unittest
from pathlib import Path
from validador_service_v4 import extract_text

class TestExtractText(unittest.TestCase):

    def setUp(self):
        self.pdf_file = Path(__file__).parent / "sample.pdf"
        self.docx_file = Path(__file__).parent / "sample.docx"
        self.image_file = Path(__file__).parent / "sample.png"
        self.unsupported_file = Path(__file__).parent / "sample.xlsx"

        # Create dummy files for testing
        self.pdf_file.write_text("Dummy PDF content")
        self.docx_file.write_text("Dummy DOCX content")
        self.image_file.write_text("Dummy Image content")
        self.unsupported_file.write_text("Dummy Unsupported content")

    def tearDown(self):
        # Clean up dummy files
        self.pdf_file.unlink()
        self.docx_file.unlink()
        self.image_file.unlink()
        self.unsupported_file.unlink()

    def test_extract_text_pdf(self):
        text = extract_text(self.pdf_file)
        self.assertIn("Dummy PDF content", text)

    def test_extract_text_docx(self):
        text = extract_text(self.docx_file)
        self.assertIn("Dummy DOCX content", text)

    def test_extract_text_image(self):
        text = extract_text(self.image_file)
        self.assertIn("Dummy Image content", text)

    def test_extract_text_unsupported(self):
        with self.assertRaises(ValueError):
            extract_text(self.unsupported_file)

if __name__ == "__main__":
    unittest.main()
