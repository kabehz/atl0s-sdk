import unittest
from pathlib import Path
from validador_service_v4 import analyze_documents

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