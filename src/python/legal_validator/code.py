#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import hashlib
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import nltk
from sentence_transformers import SentenceTransformer, util
from tqdm import tqdm
from rich import print
from rich.table import Table
from pypdf import PdfReader, PdfWriter
from docx import Document
from PIL import Image
import pytesseract
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
from rich.markdown import Markdown
from rich.live import Live
from rich.text import Text
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
 
# import textract

nltk.download('punkt')
MODEL = SentenceTransformer('all-MiniLM-L6-v2')

TAXONOMY_PATH = 'legal_semantic_taxon_v2_merged.json'
SUPPORTED_EXTENSIONS = ['.pdf', '.docx', '.odt', '.txt', '.rtf']

def load_taxonomy(path=TAXONOMY_PATH):
    with open(path, encoding='utf-8') as f:
        tax = json.load(f)
    flat = [item for sub in tax.values() for item in sub]
    return tax, list(set(flat))

def hash_file(path, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(4096), b""):
            h.update(block)
    return h.hexdigest()


# def extract_text(path):
#      return textract.process(str(path)).decode('utf-8', errors='ignore')

## Text Extraction
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():  # Asegúrate de manejar páginas sin texto
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs if paragraph.text])
    return text

def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang="eng", config="--psm 6")
    return text

def extract_text(file_path):
    """Extrae texto de un archivo según su tipo."""
    ext = file_path.suffix.lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext in [".png", ".jpg", ".jpeg", ".tiff", ".bmp"]:
        return extract_text_from_image(file_path)
    else:
        raise ValueError(f"Extensión de archivo no soportada: {ext}")
    
## Semantic Analysis

def semantic_analysis(text, keywords):
    sentences = nltk.sent_tokenize(text)
    text_vecs = MODEL.encode(sentences, convert_to_tensor=True)
    keyword_vecs = MODEL.encode(keywords, convert_to_tensor=True)
    sim_matrix = util.cos_sim(text_vecs, keyword_vecs)
    scores = sim_matrix.max(dim=0).values
    return [(kw, float(scores[i])) for i, kw in enumerate(keywords) if scores[i] > 0.3]

def draw_semantic_graph(matches, output_path):
    G = nx.Graph()
    for kw, score in matches:
        G.add_edge("DOCUMENTO", kw, weight=score)
    pos = nx.spring_layout(G)
    weights = [G[u][v]['weight'] * 5 for u, v in G.edges()]
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', width=weights)
    plt.title("Red Semántica del Documento")
    plt.savefig(output_path)
    plt.close()

def recursive_scan(directory):
    return [p for p in Path(directory).rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS]

def analyze_documents(input_folder, output_folder=None):
    if output_folder is None:
        output_folder = Path(input_folder)
    else:
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

    taxonomy, keywords = load_taxonomy()
    files = recursive_scan(input_folder)
    resultados = []

    print(f"[cyan]🔍 Analizando {len(files)} archivos en: {input_folder}")
    for file in tqdm(files, desc="Procesando documentos"):
        try:
            # Usar la función extract_text corregida
            text = extract_text(file)
            matches = semantic_analysis(text, keywords)
            sim = sum([m[1] for m in matches]) / len(matches) if matches else 0
            graph_out = output_folder / f"{file.stem}_semantico.png"
            draw_semantic_graph(matches, graph_out)

            resultados.append({
                "archivo": str(file.relative_to(input_folder)),
                "hash": hash_file(file),
                "categorias": ", ".join([m[0] for m in matches]),
                "similitud_promedio": round(sim, 3),
                "extracto": text[:300].replace("\n", " ")
            })
        except Exception as e:
            resultados.append({
                "archivo": str(file.relative_to(input_folder)),
                "hash": "ERROR",
                "categorias": "ERROR",
                "similitud_promedio": 0,
                "extracto": str(e)
            })

    df = pd.DataFrame(resultados)
    result_path = output_folder / "resultado_validador.csv"
    df.to_csv(result_path, index=False)

    table = Table(title="Resumen del Análisis", show_lines=True)
    table.add_column("Archivo", style="cyan", no_wrap=True)
    table.add_column("Similitud", justify="right")
    table.add_column("Categorías", overflow="fold")
    for r in resultados:
        table.add_row(r['archivo'], str(r['similitud_promedio']), r['categorias'])
    print(table)

    if len(resultados) > 1:
        df.plot(x="archivo", y="similitud_promedio", kind="barh", figsize=(10, 6), legend=False)
        plt.title("Similitud Semántica por Documento")
        plt.grid(True)
        plt.tight_layout()
        plot_path = output_folder / "dashboard_validador.png"
        plt.savefig(plot_path)
        print(f"[green]📊 Dashboard guardado: {plot_path}")

    print(f"[green]✅ Resultado general guardado en: {result_path}")
    return result_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Debes indicar la carpeta de entrada.")
        sys.exit(1)
    input_folder = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else None
    analyze_documents(input_folder, output_folder)
    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Validador Semántico Legal')
    parser.add_argument('file', type=str, help='Ruta del archivo a validar')
    args = parser.parse_args()
    from pathlib import Path
    text = extract_text(Path(args.file))
    tax, keywords = load_taxonomy()
    result = semantic_analysis(text, keywords)
    print(result)
   