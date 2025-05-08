import unittest
from pathlib import Path

# Importaciones corregidas según nueva estructura
from validador.service import hash_file, load_taxonomy, semantic_analysis

class TestValidadorSemantico(unittest.TestCase):
    def setUp(self):
        # Crear archivo de prueba con texto relevante
        self.test_file = Path(__file__).parent / "sample_test.txt"
        self.test_file.write_text("Esto es una prueba legal sobre coeficiente y propiedad horizontal.")
        self.taxonomy, self.keywords = load_taxonomy()

    def tearDown(self):
        # Eliminar archivo de prueba al finalizar cada test
        if self.test_file.exists():
            self.test_file.unlink()

    def test_hash_generation(self):
        # Verifica que se genere un hash SHA-256 válido
        h = hash_file(self.test_file)
        self.assertEqual(len(h), 64)

    def test_taxonomy_loading(self):
        # Verifica que palabras clave estén presentes en la taxonomía
        self.assertIn("coeficiente", self.keywords)
        self.assertIn("propiedad horizontal", self.keywords)

    def test_semantic_analysis_detects_keywords(self):
        # Verifica que se detecten correctamente palabras clave en el texto
        text = self.test_file.read_text()
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0] for r in results))

    def test_semantic_analysis_empty(self):
        # Verifica comportamiento ante texto vacío
        results = semantic_analysis("", self.keywords)
        self.assertEqual(results, [])

    def test_semantic_analysis_with_non_keywords(self):
        # Verifica que no se encuentren coincidencias en texto irrelevante
        text = "Este texto no contiene palabras clave."
        results = semantic_analysis(text, self.keywords)
        self.assertEqual(results, [])

if __name__ == '__main__':
    unittest.main()