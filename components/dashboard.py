import streamlit as st

from components.feature_cards import render_feature_cards
from components.hero import render_hero
from components.metrics import render_metrics
from components.sidebar import render_sidebar
from components.workflow import render_workflow


def render_dashboard():
    render_sidebar()
    render_hero()

    st.write("")
    render_metrics()

    st.write("")
    render_feature_cards()

    render_workflow()

    st.divider()

    st.caption(
    "AI Job Assistant · Built with Streamlit, "
    "Gemini, Adzuna, and SQLite"
)
