import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from langchain_community.tools import DuckDuckGoSearchRun

# Load environment variables
load_dotenv()

# Import local components
from src.components.navigation import page_config, custom_style, footer

class HealthAdviceAgent:
    def __init__(self):
        # Validate API key
        self.api_key = os.getenv('GROQ_API_KEY')
        if not self.api_key:
            raise ValueError("GROQ API key not found. Please check your .env file.")
        
        # Initialize Groq client
        self.client = Groq(api_key=self.api_key)
        self.search_tool = DuckDuckGoSearchRun()

    def get_health_advice(self, symptoms: str, intensity: str) -> str:
        """
        Generate health advice using Groq's LLM
        
        Args:
            symptoms (str): User-reported symptoms
            intensity (str): Symptom intensity
        
        Returns:
            str: Generated health advice
        """
        query = f"Health advice for {symptoms} with {intensity} intensity"
        
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful medical assistant providing professional health advice."},
                    {"role": "user", "content": query}
                ],
                model="llama3-8b-8192",
                max_tokens=300,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            st.error(f"Error generating health advice: {e}")
            return "Unable to generate health advice at the moment."

def main():
    # Streamlit Page Setup
    page_config("DocLib", "🤖", "wide")
    custom_style()

    st.title("🤖 DocLib 🤖")
    st.markdown("### DocLib helps you find specialists nearby while suggesting home remedies for your health issues.")

    # Initialize health advice agent
    health_agent = HealthAdviceAgent()

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        symptoms = st.text_input("Enter current symptoms:")

    with col2:
        intensity = st.selectbox(
            "Select the intensity of symptoms:", 
            ["Mild", "Moderate", "Severe"]
        )

    with col3:
        city = st.text_input("Enter current city:")

    # Advice generation
    if st.button("Get Advice"):
        if symptoms:
            with st.spinner('Generating health advice...'):
                result = health_agent.get_health_advice(symptoms, intensity)
                st.success(result)
        else:
            st.error("Please enter your symptoms first.")

    # Optional: Add footer
    
    footer()

if __name__ == "__main__":
    main()