import os
import json
import streamlit as st

class ConfigManager:
    def __init__(self):
        self.working_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.load_config()
        
    def load_config(self):
        """Load configuration from JSON file or environment."""
        # Default settings that don't include secrets
        self.config = {
            "model_settings": {
                "embedding_model": "sentence-transformers/all-mpnet-base-v2",
                "llm_model": "deepseek-r1-distill-llama-70b",
                "temperature": 0
            },
            "chunk_settings": {
                "chunk_size": 2000,
                "chunk_overlap": 200
            }
        }
            
    def get_groq_api_key(self):
        """Get GROQ API key from Streamlit secrets."""
        return st.secrets["GROQ_API_KEY"]