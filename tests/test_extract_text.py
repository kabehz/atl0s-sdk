from PyPDF2 import PdfWriter

from docx import Document
from PIL import Image
import pytesseract
import unittest
from pathlib import Path
from validador_service_v4 import extract_text




from PyPDF2 import PdfWriter

class TestExtractText(unittest.TestCase):
    def setUp(self):
        self.pdf_file = Path(__file__).parent / "anexos/sample.pdf"
        self.docx_file = Path(__file__).parent / "anexos/sample.docx"
        self.image_file = Path(__file__).parent / "anexos/sample.png"
        self.unsupported_file = Path(__file__).parent / "anexos/sample.xlsx"

        # Crear un archivo PDF válido
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        writer.add_metadata({'/Title': 'Dummy PDF content'})
        with open(self.pdf_file, "wb") as f:
            writer.write(f)

        # Crear un archivo DOCX válido
        doc = Document()
        doc.add_paragraph("Dummy DOCX content")
        doc.save(self.docx_file)

        img = Image.new("RGB", (100, 100), color="white")
        draw = Image.Draw(img)
        draw.text((10, 10), "Dummy Image content", fill="black")
        img.save(self.image_file)
        img.save(self.image_file)

        # Crear un archivo no soportado
        self.unsupported_file.write_text("Dummy Unsupported content")

        self.pdf_file.unlink(missing_ok=True)
        self.docx_file.unlink(missing_ok=True)
        self.image_file.unlink(missing_ok=True)
        self.unsupported_file.unlink(missing_ok=True)
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

    # Test extracting text from an unsupported file type (e.g., .xlsx)
    def test_extract_text_unsupported_file_type(self):
        with self.assertRaises(ValueError):
            extract_text(self.unsupported_file)
        

    # def test_extract_text_empty_file(self):
    #     empty_file = Path(__file__).parent / "anexos/empty_file.txt"
    #     empty_file.write_text("")
    #     text = extract_text(empty_file)
    #     self.assertEqual(text, "")
    #     empty_file.unlink()
    # def test_extract_text_invalid_file(self):
    #     invalid_file = Path(__file__).parent / "anexos/invalid_file.txt"
    #     invalid_file.write_text("Invalid content")
    #     with self.assertRaises(ValueError):
    #         extract_text(invalid_file)
    #     invalid_file.unlink()
    # def test_extract_text_large_file(self):
    #     large_file = Path(__file__).parent / "anexos/large_file.txt"
    #     large_content = "A" * (10**6)
    #     large_file.write_text(large_content)
    #     text = extract_text(large_file)
    #     self.assertEqual(text, large_content)
    #     large_file.unlink()
    # def test_extract_text_corrupted_file(self):
    #     corrupted_file = Path(__file__).parent / "anexos/corrupted_file.pdf"
    #     with open(corrupted_file, "wb") as f:
    #         f.write(b"corrupted data")
    #     with self.assertRaises(ValueError):
    #         extract_text(corrupted_file)
    #     corrupted_file.unlink()
    # def test_extract_text_large_image(self):
    #     large_image = Path(__file__).parent / "anexos/large_image.png"
    #     img = Image.new("RGB", (1000, 1000), color="white")
    #     img.save(large_image)
    #     text = extract_text(large_image)
    #     self.assertIn("Dummy Image content", text)
    #     large_image.unlink()
    # def test_extract_text_large_docx(self):
    #     large_docx = Path(__file__).parent / "anexos/large_docx.docx"
    #     doc = Document()
    #     for _ in range(1000):
    #         doc.add_paragraph("Dummy DOCX content")
    #     doc.save(large_docx)
    #     text = extract_text(large_docx)
    #     self.assertIn("Dummy DOCX content", text)
    #     large_docx.unlink()
    # def test_extract_text_empty_pdf(self):
    #     empty_pdf = Path(__file__).parent / "anexos/empty_pdf.pdf"
    #     writer = PdfWriter()
    #     writer.add_blank_page(width=72, height=72)
    #     with open(empty_pdf, "wb") as f:
    #         writer.write(f)
    #     text = extract_text(empty_pdf)
    #     self.assertEqual(text, "")
    #     empty_pdf.unlink()
    # def test_extract_text_empty_docx(self):
    #     empty_docx = Path(__file__).parent / "anexos/empty_docx.docx"
    #     doc = Document()
    #     doc.save(empty_docx)
    #     text = extract_text(empty_docx)
    #     self.assertEqual(text, "")
    #     empty_docx.unlink()
    # def test_extract_text_empty_image(self):
    #     empty_image = Path(__file__).parent / "anexos/empty_image.png"
    #     img = Image.new("RGB", (0, 0), color="white")
    #     img.save(empty_image)
    #     text = extract_text(empty_image)
    #     self.assertEqual(text, "")
    #     empty_image.unlink()
    # def test_extract_text_unsupported_format(self):
    #     unsupported_file = Path(__file__).parent / "anexos/unsupported_file.txt"
    #     unsupported_file.write_text("Dummy Unsupported content")
    #     with self.assertRaises(ValueError):
    #         extract_text(unsupported_file)
    #     unsupported_file.unlink()

if __name__ == "__main__":
    unittest.main()
# from validador_service_v4 import extract_text



