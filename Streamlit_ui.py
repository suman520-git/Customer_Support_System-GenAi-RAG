import asyncio
import nest_asyncio
import streamlit as st

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from retriever.retrieval import Retriever
from utils.model_loader import ModelLoader
from prompt_library.prompt import PROMPT_TEMPLATES
from dotenv import load_dotenv
import os


# Fix event loop for Streamlit thread

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

nest_asyncio.apply()


# Load environment + models

load_dotenv()

retriever_obj = Retriever()
model_loader = ModelLoader()

def invoke_chain(query: str):
    retriever = retriever_obj.load_retriever()
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATES["product_bot"])
    llm = model_loader.load_llm()

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    output = chain.invoke(query)
    return output


# Streamlit UI

st.title("🎧 Flipkart Product (Headphones) Assistant")

# Chat input
user_query = st.chat_input("Ask me anything about headphones!")

if user_query:
    with st.spinner("Thinking..."):
        result = invoke_chain(user_query)
    st.chat_message("user").write(user_query)
    st.chat_message("assistant").write(result)
