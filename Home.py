##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##DocLib
##################################################################################################
# Importing dependencies

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
# Importing dependencies
import os
import logging
import streamlit as st
from pathlib import Path
import base64
import sys
import warnings
from dotenv import load_dotenv
from typing import Any, Dict
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import HumanMessage
from langchain_community.tools import DuckDuckGoSearchRun
from fpdf import FPDF

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

#Import from SRC
from src.components.navigation import page_config, custom_style, footer

# Setting up Llama3 via Ollama server @http://localhost:11434/v1 
os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(
    model="crewai-llama3",
    base_url="http://localhost:11434/v1"
)

search_tool = DuckDuckGoSearchRun()

###################################################################################################















































def main():
    # Streamlit Page Setup
    page_config("DocLib", "🤖", "wide") 
    custom_style()
    # st.sidebar.image('./src/logo.png')

    st.title("🤖DocLib🤖")
    st.markdown(
        '''
        <style>
            div.block-container{padding-top:0px;}
            font-family: 'Roboto', sans-serif; /* Add Roboto font */
            color: blue; /* Make the text blue */
        </style>
        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        ### DocLib help you find specialist nearby while suggestion home remedies for your health issues.
        """
    )

    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    col1, col2, col3 = st.columns(3)
    
    # Input for blog topic
    with col1:
        symptoms = st.text_input("Enter current symptoms:")

    # Dropdown for selecting the type of content  
    with col2:
        intensity = st.selectbox(
            "Select the intensity of symptoms:", 
            ["Mild", "Moderate", "Severe"]
        )
        
    # Input for City
    with col3:
        city = st.text_input("Enter current city:")

    if st.button("Get Advice"):
        if symptoms:
            # blog_crew = BlogCrew(blog_topic, content_type)
            # result = blog_crew.run()
            st.write("Test Advice")
        else:
            st.error("Please enter your symptoms first.")


if __name__ == "__main__":
    main()
    with st.sidebar:
        footer()