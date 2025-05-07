from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import pytesseract

def extract_text_from_pdf(file_path):
    """Extrae texto de un archivo PDF."""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error al procesar el PDF: {e}"

def extract_text_from_docx(file_path):
    """Extrae texto de un archivo DOCX."""
    try:
        doc = Document(file_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text
    except Exception as e:
        return f"Error al procesar el DOCX: {e}"

def extract_text_from_image(image_path):
    """Extrae texto de una imagen usando OCR."""
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        return f"Error al procesar la imagen: {e}"

if __name__ == "__main__":
    # Archivos de prueba
    pdf_file = "example.pdf"
    docx_file = "example.docx"
    image_file = "example.png"

    print("=== Test de extracción de texto ===\n")

    # Test PDF
    print(f"Probando extracción de texto desde PDF: {pdf_file}")
    pdf_text = extract_text_from_pdf(pdf_file)
    print(f"Texto extraído:\n{pdf_text}\n")

    # Test DOCX
    print(f"Probando extracción de texto desde DOCX: {docx_file}")
    docx_text = extract_text_from_docx(docx_file)
    print(f"Texto extraído:\n{docx_text}\n")

    # Test Imagen
    print(f"Probando extracción de texto desde Imagen: {image_file}")
    image_text = extract_text_from_image(image_file)
    print(f"Texto extraído:\n{image_text}\n")
    