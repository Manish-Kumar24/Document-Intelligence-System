import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from core.embeddings import EmbeddingManager

class DocumentProcessor:
    def __init__(self):
        self.embedding_manager = EmbeddingManager()
        self.working_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
    def process_document(self, file_path):
        """Process a document and store its embeddings."""
        if not os.path.exists(file_path):
            raise ValueError(f"File not found: {file_path}")
            
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )
        texts = text_splitter.split_documents(documents)
        
        vectordb = self.embedding_manager.create_vector_store(texts)
        return vectordb