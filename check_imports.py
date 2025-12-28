
import sys
import importlib

requirements = [
    "streamlit",
    "pandas",
    "numpy",
    "dotenv", # python-dotenv
    "sklearn", # scikit-learn
    "joblib",
    "langgraph",
    "langchain",
    "langchain_community",
    "langchain_google_genai",
    "langchain_core",
    "google.generativeai",
    "sentence_transformers",
    "huggingface_hub",
    "faiss", # faiss-cpu
    "transformers",
    "sentencepiece",
    "googletrans",
    "fitz", # pymupdf
    "PyPDF2",
    "pytest",
    "black",
    "flake8",
    "loguru",
    "pydantic",
    "pydantic_settings",
    "typing_extensions",
    "requests",
    "aiohttp",
    "markdown"
]

missing = []
for req in requirements:
    try:
        importlib.import_module(req)
        print(f"[OK] {req}")
    except ImportError:
        print(f"[MISSING] {req}")
        missing.append(req)

print(f"\nTotal Missing: {len(missing)}")
print("Missing modules:", missing)
