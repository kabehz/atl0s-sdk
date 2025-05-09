import unittest
import networkx as nx
import matplotlib.pyplot as plt
import sys
from pathlib import Path
# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))
# Importar la función a probar
from src.pip.legal_validator.code import draw_semantic_graph

class TestVisualizations(unittest.TestCase):

    def setUp(self):
        # Crear un grafo de ejemplo
        self.graph = nx.Graph()
        self.graph.add_node("Concepto A")
        self.graph.add_node("Concepto B")
        self.graph.add_edge("Concepto A", "Concepto B", weight=0.8)

        # Directorio temporal para guardar visualizaciones
        self.output_dir = Path(__file__).parent / "output"
        self.output_dir.mkdir(exist_ok=True)

    def tearDown(self):
        # Eliminar archivos generados durante las pruebas
        for file in self.output_dir.iterdir():
            file.unlink()
        self.output_dir.rmdir()

    def test_draw_semantic_graph(self):
        """Prueba que el grafo semántico se genere correctamente."""
        output_file = self.output_dir / "semantic_graph.png"
        draw_semantic_graph(self.graph, output_file)

        # Verificar que el archivo se haya generado
        self.assertTrue(output_file.exists())

    def test_matplotlib_visualization(self):
        """Prueba que una visualización simple con matplotlib se guarde correctamente."""
        output_file = self.output_dir / "example_plot.png"

        # Crear una visualización simple
        plt.figure()
        plt.plot([1, 2, 3], [4, 5, 6], label="Ejemplo")
        plt.title("Gráfico de Ejemplo")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.legend()
        plt.savefig(output_file)
        plt.close()

        # Verificar que el archivo se haya generado
        self.assertTrue(output_file.exists())

if __name__ == '__main__':
    unittest.main()