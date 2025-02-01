# Document Intelligence System
![Main Interface](https://github.com/Manish-Kumar24/Document-Intelligence-System/blob/main/image/Capture.PNG)
A powerful document analysis system powered by DeepSeek-R1 LLM and RAG (Retrieval Augmented Generation) technology. This application allows users to upload PDF documents and ask questions about their content, receiving accurate, context-aware responses.

## 🎯 Features
- 📄 PDF document processing and analysis
- 💡 Intelligent question answering using DeepSeek-R1 LLM
- 🔍 Advanced document chunking and embedding
- 🚀 Vector store-based retrieval system
- 🎨 Clean and intuitive Streamlit interface

## 🛠️ Technology Stack
- **Framework**: Streamlit
- **LLM**: DeepSeek-R1 via Groq
- **Vector Store**: Chroma DB
- **Embeddings**: HuggingFace
- **Document Processing**: PyPDF

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Groq API Key

### Installation

1. Clone the repository
```bash
git clone https://github.com/Manish-Kumar24/Document-Intelligence-System.git
cd Document-Intelligence-System
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up your configuration
```bash
# Update config/settings.json with your Groq API key
{
    "GROQ_API_KEY": "your-api-key-here"
}
```

5. Run the application
```bash
streamlit run app.py
```

## 📁 Project Structure
```
Document-Intelligence-System/
|── app.py
|── core/
│   |── __init__.py
│   |── document_processor.py
│   |── embeddings.py
│   |── qa_engine.py
|── utils/
│   ├── __init__.py
│   └── config_manager.py
├── config/
│   └── settings.json
├── requirements.txt
└── README.md
```

## 🎯 Usage

1. Launch the application
2. Upload a PDF document using the file uploader
3. Wait for the document to be processed
4. Type your question in the text area
5. Click "Get Answer" to receive a response

## ⚙️ Configuration

The system can be configured through `config/settings.json`:
```json
{
    "GROQ_API_KEY": "your-api-key-here",
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
```

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- DeepSeek for their amazing LLM model
- Groq for providing fast LLM inference
- Langchain for the RAG framework
- Streamlit for the web interface framework

## 📧 Contact
Your Name - [manishkumar202209@gmail.com](mailto:manishkumar202209@gmail.com)

Project Link: [https://github.com/Manish-Kumar24/Document-Intelligence-System](https://github.com/Manish-Kumar24/Document-Intelligence-System)
