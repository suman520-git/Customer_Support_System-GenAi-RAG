# Customer_Support_System-GenAi-RAG

A Chatbot with LLM and RAG system gives response for given query about Head Phones product from FlipKart web site data.
## 🎯 Project Overview

This project demonstrates core RAG concepts through a practical implementation that includes:
- Web Scraping from FlipKart ecommerce website for Headphones product data.
- Document ingestion and Transformation from "flipkart_product_review.csv" file
- Creation of Vector storage database in AstraDB
- LLM integration for answer generation
- FastAPI with HTML and CSS for front end
- streamlit app file for front end



## 📋 Project Structure

```
langchain-rag-project/
├── notebooks/              # Jupyter notebooks for demos
│   ├── 01_setup.ipynb
│   ├── 02_data_ingestion.ipynb
│   ├── 03_embedding_pipeline.ipynb
│   ├── 04_retrieval_demo.ipynb
│   ├── 05_rag_testing.ipynb
│   ├── 06_hyde_experiments.ipynb
│   ├── 07_advanced_search.ipynb
│   ├── 08_api_integration.ipynb
│   └── 09_master_demo.ipynb
├── src/                    # Source code modules
│   ├── ingestion/          # Document processing
│   ├── chunking/           # Text chunking strategies
│   ├── embedding/          # Embedding generation
│   ├── retrieval/          # Search and retrieval
│   ├── generation/         # LLM integration
│   └── optimization/       # Advanced techniques
├── app/                    # FastAPI application
│   ├── main.py            # Main application entry point
│   ├── enhanced_api.py    # Advanced RAG features API
│   └── routes/            # API route modules
│       ├── search.py      # Search endpoints
│       ├── rag.py         # RAG pipeline endpoints
│       └── enhancement.py # Enhancement endpoints
├── config/                 # Configuration files
├── data/                   # Data storage
│   ├── raw/               # Source documents
│   ├── processed/         # Processed chunks
│   └── embeddings/        # Vector embeddings
├── tests/                  # Organized test cases
│   ├── api/               # API endpoint tests
│   └── integration/       # Integration tests
├── chatbot.py             # Terminal-based chat interface
└── static/                # Web UI assets
```

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone the repository
git clone <repository-url>
cd Customer_Support_System-GenAi-RAG

# Create virtual environment
conda create -p venv python==3.10 -y
conda activate venv/ 

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Create environment template
.env

# Edit .env with your API keys
# Required:
# - ASTRA_DB_API_ENDPOINT="xxx"
# - ASTRA_DB_APPLICATION_TOKEN="xxx"
# - ASTRA_DB_KEYSPACE="xxxx"
#- GOOGLE_API_KEY="xxxx"
#- GROQ_API_KEY="xxxx"
```

### 3. Verify Setup

```bash
# Or start the FastAPI server (from project root in virtual environment)
uvicorn main:app --host 0.0.0.0 --port 8000
# Visit http://localhost:8000/docs
# Or start through streamlit: streamlit run Streamlit_ui.py
```

## 📚 Usage

### Interactive Development
Start with the Jupyter notebooks in order:
1. **01_setup.ipynb** - Environment validation
2. **02_data_ingestion.ipynb** - Document collection
3. **03_embedding_pipeline.ipynb** - Vector generation
4. **04_retrieval_demo.ipynb** - Search testing
5. **05_rag_testing.ipynb** - Q&A system
6. **06_hyde_experiments.ipynb** - Advanced retrieval
7. **07_advanced_search.ipynb** - Hybrid search
8. **08_api_integration.ipynb** - API testing
9. **09_master_demo.ipynb** - Complete showcase

### API Usage
Start the FastAPI server and visit `/docs` for interactive API documentation:

```bash
# From project root
uvicorn app.main:app --host 0.0.0.0 --port 8000

#Or start through streamlit 
streamlit run Streamlit_ui.py
```

### Model Settings
- **LLM**: "deepseek-r1-distill-llama-70b" 
- **Embedding**: "models/text-embedding-004"
- **Top-K Retrieval**: 10 documents

## 🤝 Contributing

This is an educational project. Feel free to:
- Experiment with different models and parameters
- Add new chunking strategies
- Implement additional retrieval techniques


## 📄 License

This project is for educational purposes. Please check individual component licenses for production use.

## 🆘 Support

For issues and questions:
1. Review the configuration settings
2. Ensure all API keys are properly set
3. Verify network connectivity to external services

---

*Built with ❤️ for learning RAG systems and LangChain*
