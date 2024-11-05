##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)

##################################################################################################
#Importing dependencies
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import os
import logging
import streamlit as st
from pathlib import Path
import base64
import sys
import os
import warnings
from dotenv import load_dotenv
from typing import Any, Dict
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import HumanMessage
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
from fpdf import FPDF
from src.agents import planner, writer, editor



##################################################################################################
#Setting up Llama3
os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(
    model = "crewai-llama3",
    base_url = "http://localhost:11434/v1")
##################################################################################################



# tasks.py
class DocLibTasks:
    def create_home_remedy_task(self, agent, symptom, intensity):
        return Task(
            description=f"Find immediate home remedies for {symptom} with {intensity} intensity",
            agent=agent
        )

    def create_doctor_finder_task(self, agent, location, symptom):
        return Task(
            description=f"Find specialists treating {symptom} in {location} with appointment availability",
            agent=agent
        )

    def create_symptom_analysis_task(self, agent, symptom, intensity):
        return Task(
            description=f"Analyze {symptom} with {intensity} intensity and provide medical recommendations",
            agent=agent
        )