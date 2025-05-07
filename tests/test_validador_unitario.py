import unittest
from pathlib import Path
from validador_service_v4 import hash_file, load_taxonomy, semantic_analysis

class TestValidadorSemantico(unittest.TestCase):

    def setUp(self):
        self.test_file = Path(__file__).parent / "sample_test.txt"
        self.test_file.write_text("Esto es una prueba legal sobre coeficiente y propiedad horizontal.")
        self.taxonomy, self.keywords = load_taxonomy()

    def tearDown(self):
        self.test_file.unlink()

    def test_hash_generation(self):
        h = hash_file(self.test_file)
        self.assertEqual(len(h), 64)

    def test_taxonomy_loading(self):
        self.assertTrue("coeficiente" in self.keywords or "propiedad horizontal" in self.keywords)

    def test_semantic_analysis_detects_keywords(self):
        text = self.test_file.read_text()
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] or "propiedad horizontal" in r[0] for r in results))

if __name__ == '__main__':
    unittest.main()