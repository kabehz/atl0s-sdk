import unittest
from pathlib import Path
from docx import Document
from PIL import Image, ImageDraw
# Importar la función a probar
from src.pip.legal_validator.code import extract_text


class TestExtractText(unittest.TestCase):
    def setUp(self):
        self.anexos_dir = Path(__file__).parent / "anexos"
        self.anexos_dir.mkdir(exist_ok=True)

        # Preparar archivos para pruebas
        self.pdf_file = self.anexos_dir / "sample.pdf"
        self.docx_file = self.anexos_dir / "sample.docx"
        self.image_file = self.anexos_dir / "sample.png"
        self.unsupported_file = self.anexos_dir / "sample.xlsx"

        # Crear DOCX de prueba
        doc = Document()
        doc.add_paragraph("Contenido de prueba DOCX")
        doc.save(self.docx_file)

        # Crear imagen con texto
        img = Image.new("RGB", (200, 100), color="white")
        draw = ImageDraw.Draw(img)
        draw.text((10, 40), "Texto imagen", fill="black")
        img.save(self.image_file)

    def test_extract_text_from_docx(self):
        texto = extract_text(self.docx_file)
        self.assertIn("Contenido de prueba", texto)

    def test_extract_text_from_image(self):
        texto = extract_text(self.image_file)
        self.assertIn("Texto", texto)

    def test_unsupported_extension(self):
        with self.assertRaises(ValueError):
            extract_text(self.unsupported_file)

    def tearDown(self):
        for f in [self.docx_file, self.image_file]:
            if f.exists():
                f.unlink()

if __name__ == '__main__':
    unittest.main()