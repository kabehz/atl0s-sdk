import unittest
from pathlib import Path
import sys
from pathlib import Path

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))
# Importar la función a probar
from src.pip.legal_validator.code import analyze_documents
from src.pip.legal_validator.code import extract_text
from src.pip.legal_validator.code import hash_file
from src.pip.legal_validator.code import draw_semantic_graph


def test_extract_text_functionality(self):
    test_file = Path(__file__).parent / "test_file.txt"
    test_file.write_text("Este es un texto de prueba.")
    extracted_text = extract_text(test_file)
    self.assertIn("texto de prueba", extracted_text)
    test_file.unlink()

def test_hash_file_functionality(self):
    test_file = Path(__file__).parent / "test_file.txt"
    test_file.write_text("Este es un texto de prueba.")
    file_hash = hash_file(test_file)
    self.assertIsInstance(file_hash, str)
    test_file.unlink()

def test_draw_semantic_graph_functionality(self):
    test_graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A"],
        "D": ["B"]
    }
    output_file = Path(__file__).parent / "test_graph.png"
    draw_semantic_graph(test_graph, output_file)
    self.assertTrue(output_file.exists())
    output_file.unlink()

def test_analyze_documents_functionality(self):
    entrada = Path(__file__).parent.parent / "Anexos_Ejemplo"
    salida = Path(__file__).parent / "salida_test"
    salida.mkdir(exist_ok=True)
    output_csv = analyze_documents(entrada, salida)
    self.assertTrue(output_csv.exists())
    # Ensure the output file is not empty, validating that analyze_documents produced meaningful content.
    self.assertTrue(output_csv.stat().st_size > 0)


class TestValidadorIntegracion(unittest.TestCase):

    def test_document_analysis_pipeline(self):
        entrada = Path(__file__).parent.parent / "Anexos_Ejemplo"
        salida = Path(__file__).parent / "salida_test"
        salida.mkdir(exist_ok=True)
        output_csv = analyze_documents(entrada, salida)
        self.assertTrue(output_csv.exists())
        self.assertTrue(output_csv.stat().st_size > 0)

        self.assertGreater(output_csv.stat().st_size, 0)

if __name__ == '__main__':
    unittest.main()
