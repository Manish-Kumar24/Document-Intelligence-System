import os
import streamlit as st

# Keep only this one set_page_config() at the very top
st.set_page_config(
    page_title="Document RAG System",
    page_icon="📚",
    layout="wide"
)

from core.document_processor import DocumentProcessor
from core.qa_engine import QAEngine
from utils.config_manager import ConfigManager

class DocumentRAGApp:
    def __init__(self):
        # st.write("Initializing app...")  # Debug print
        self.config = ConfigManager()
        self.doc_processor = DocumentProcessor()
        self.qa_engine = QAEngine()
        self.working_dir = os.path.dirname(os.path.abspath(__file__))
        self.uploads_dir = os.path.join(self.working_dir, "uploads")
        os.makedirs(self.uploads_dir, exist_ok=True)
        # st.write(f"Working directory: {self.working_dir}")  # Debug print

    def run(self):
        # st.write("Starting app...")  # Debug print
        
        st.title("📚 Document Intelligence System")
        st.subheader("Powered by DeepSeek-R1")

        # Display current configuration
        # st.write("System Configuration:")
        # st.write(f"- Uploads directory: {self.uploads_dir}")
        # st.write(f"- Vector store directory: {os.path.join(self.working_dir, 'vector_store')}")

        uploaded_file = st.file_uploader(
            "Upload your document (PDF)",
            type=["pdf"],
            help="Upload a PDF document to analyze"
        )

        if uploaded_file:
            # st.write(f"File uploaded: {uploaded_file.name}")  # Debug print
            with st.spinner("Processing document..."):
                file_path = os.path.join(self.uploads_dir, uploaded_file.name)
                # st.write(f"Saving to: {file_path}")  # Debug print
                
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                try:
                    st.write("Starting document processing...")  # Debug print
                    self.doc_processor.process_document(file_path)
                    st.success("Document processed successfully!")
                except Exception as e:
                    st.error(f"Error processing document: {str(e)}")
                    st.write("Full error details:", e)  # Debug print
                    return

        user_question = st.text_area(
            "Ask a question about your document",
            help="Enter your question here and click 'Get Answer' to receive a response"
        )

        if st.button("Get Answer", type="primary"):
            if not user_question:
                st.warning("Please enter a question.")
                return
                
            with st.spinner("Analyzing..."):
                try:
                    st.write("Getting answer...")  # Debug print
                    answer = self.qa_engine.get_answer(user_question)
                    st.markdown("### Answer")
                    st.markdown(answer)
                except Exception as e:
                    st.error(f"Error getting answer: {str(e)}")
                    st.write("Full error details:", e)  # Debug print

if __name__ == "__main__":
    try:
        app = DocumentRAGApp()
        app.run()
    except Exception as e:
        st.error("Application error occurred!")
        st.write("Error details:", e)