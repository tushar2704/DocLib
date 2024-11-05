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
