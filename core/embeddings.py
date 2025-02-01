from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma  # Updated import
import os

class EmbeddingManager:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings()
        self.working_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
    def create_vector_store(self, documents):
        """Create and persist vector store from documents."""
        return Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=os.path.join(self.working_dir, "vector_store")
        )
        
    def load_vector_store(self):
        """Load existing vector store."""
        return Chroma(
            persist_directory=os.path.join(self.working_dir, "vector_store"),
            embedding_function=self.embeddings
        )