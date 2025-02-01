from setuptools import setup, find_packages

setup(
    name="document_rag",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.30.0",
        "langchain>=0.1.0",
        "langchain-community>=0.0.10",
        "langchain-groq>=0.0.3",
        "langchain-huggingface>=0.0.7",
        "chromadb>=0.4.22",
        "unstructured>=0.10.30",
        "sentence-transformers>=2.2.2",
        "python-dotenv>=1.0.0",
    ],
)