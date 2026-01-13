import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

def configure_page():
    st.set_page_config(
        page_title="AntiFraude Azure AI",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
