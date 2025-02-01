from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from core.embeddings import EmbeddingManager
from utils.config_manager import ConfigManager

class QAEngine:
    def __init__(self):
        self.config = ConfigManager()
        self.embedding_manager = EmbeddingManager()
        self.llm = ChatGroq(
            model="deepseek-r1-distill-llama-70b",
            temperature=0,
            api_key=self.config.get_groq_api_key()
        )
        
    def get_answer(self, question):
        """Get answer for a given question using RAG."""
        vectordb = self.embedding_manager.load_vector_store()
        retriever = vectordb.as_retriever(
            search_kwargs={"k": 3}
        )
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )
        
        response = qa_chain.invoke({"query": question})
        return response["result"]