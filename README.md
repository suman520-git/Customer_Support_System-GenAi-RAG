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
Customer_Support_System-GenAi-RAG           
├─ config                                   
│  ├─ config.yaml                           
│  └─ __init__.py                           
├─ data                                     
│  └─ flipkart_product_review.csv           
├─ data_collection                          
│  └─ Flipkart_headsetdata_web_scraping.py  
├─ data_ingestion                           
│  ├─ ingestion_pipeline.py                 
│  └─ __init__.py                           
├─ notebook                                 
│  └─ Expermentation.ipynb                  
├─ prompt_library                           
│  ├─ __pycache__                           
│  │  ├─ prompt.cpython-310.pyc             
│  │  └─ __init__.cpython-310.pyc           
│  ├─ prompt.py                             
│  └─ __init__.py                           
├─ retriever                                
│  ├─ __pycache__                           
│  │  ├─ retrieval.cpython-310.pyc          
│  │  └─ __init__.cpython-310.pyc           
│  ├─ retrieval.py                          
│  └─ __init__.py                           
├─ static                                   
│  └─ style.css                             
├─ templates                                
│  └─ chat.html                             
├─ utils                                    
│  ├─ __pycache__                           
│  │  ├─ config_loader.cpython-310.pyc      
│  │  ├─ model_loader.cpython-310.pyc       
│  │  └─ __init__.cpython-310.pyc           
│  ├─ config_loader.py                      
│  ├─ model_loader.py                       
│  └─ __init__.py                           
├─ __pycache__                              
│  └─ main.cpython-310.pyc                  
├─ main.py                                  
├─ README.md                                
├─ requirements.txt                         
├─ setup.py                                 
├─ Streamlit_ui.py                          
└─ test.py                                  
                          
                              
                                 
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
1. **Flipkart_headsetdata_web_scraping.py** - Web Scraping and Datacollection(csv file)
2. **ingestion_pipeline.py** - Data Transformation and Ingestion in to Vectore store(AstraDB)
3. **retrieval.py** - Data retrieval from vectore store(AstraDB) acts as retriver
4. **main.py** - API testing


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



## 🆘 Support

For issues and questions:
1. Review the configuration settings
2. Ensure all API keys are properly set
3. Verify network connectivity to external services

---


