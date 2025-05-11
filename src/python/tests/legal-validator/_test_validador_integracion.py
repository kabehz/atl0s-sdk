import unittest
from pathlib import Path
import sys
from pathlib import Path
from wsgiref.validate import validator

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))


# Importar la función a probar
from src.pip.legal_validator.code import analyze_documents
from src.pip.legal_validator.code import extract_text
from src.pip.legal_validator.code import hash_file
from src.pip.legal_validator.code import draw_semantic_graph


class TestValidadorIntegracion(unittest.TestCase):

    def test_document_analysis_pipeline(self):
        entrada = Path(__file__).parent.parent / "Anexos_Ejemplo"
        salida = Path(__file__).parent / "salida_test"
        salida.mkdir(exist_ok=True)
        output_csv = analyze_documents(entrada, salida)
        self.assertTrue(output_csv.exists())
        self.assertTrue(output_csv.stat().st_size > 0)

if __name__ == '__main__':
    unittest.main()