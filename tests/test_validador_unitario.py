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
        self.assertIn("coeficiente", self.keywords)
        self.assertIn("propiedad horizontal", self.keywords)

    def test_semantic_analysis_detects_keywords(self):
        text = self.test_file.read_text()
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0] for r in results))

    def test_semantic_analysis_empty(self):
        text = ""
        results = semantic_analysis(text, self.keywords)
        self.assertEqual(results, [])

    def test_semantic_analysis_with_non_keywords(self):
        text = "Este texto no contiene palabras clave."
        results = semantic_analysis(text, self.keywords)
        self.assertEqual(results, [])
    
    def test_semantic_analysis_with_special_characters(self):
        text = "Este texto contiene coeficiente y propiedad horizontal, pero también caracteres especiales: @#$%^&*()!"
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0] for r in results))
    
    def test_semantic_analysis_with_numbers(self):
        text = "El coeficiente es 0.5 y la propiedad horizontal tiene un valor de 100."
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0] for r in results))

    def test_semantic_analysis_with_unicode(self):
        text = "El coeficiente es 0.5 y la propiedad horizontal tiene un valor de 100. También incluye caracteres unicode: ñ, ü, é."
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0] for r in results))
    
    def test_semantic_analysis_with_html_tags(self):
        text = "<p>El coeficiente es 0.5 y la propiedad horizontal tiene un valor de 100.</p>"
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0] for r in results))

    def test_semantic_analysis_with_long_text(self):
        text = " ".join(["El coeficiente es 0.5 y la propiedad horizontal tiene un valor de 100."] * 1000)
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0] for r in results))
    
    def test_semantic_analysis_with_multiple_keywords(self):
        text = "El coeficiente es 0.5 y la propiedad horizontal tiene un valor de 100. Además, el coeficiente de propiedad horizontal es importante."
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0] for r in results))
        self.assertEqual(len(results), 2)

    def test_semantic_analysis_with_different_cases(self):
        text = "El Coeficiente es 0.5 y la Propiedad Horizontal tiene un valor de 100."
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0].lower() for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0].lower() for r in results))
    
    def test_semantic_analysis_with_punctuation(self):
        text = "El coeficiente es 0.5, y la propiedad horizontal tiene un valor de 100."
        results = semantic_analysis(text, self.keywords)
        self.assertTrue(any("coeficiente" in r[0] for r in results))
        self.assertTrue(any("propiedad horizontal" in r[0] for r in results))


if __name__ == '__main__':
    unittest.main()