import streamlit as st

from components.dashboard import render_dashboard
from components.styles import load_css
from services.database import create_table


st.set_page_config(
    page_title="AI Job Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

create_table()
load_css()
render_dashboard()
