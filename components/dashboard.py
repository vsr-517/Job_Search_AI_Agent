import streamlit as st

from components.feature_cards import render_feature_cards
from components.hero import render_hero
from components.metrics import render_metrics
from components.recent_activity import render_recent_activity
from components.sidebar import render_sidebar
from components.workflow import render_workflow
from components.analytics import render_analytics

def render_dashboard():
    render_sidebar()

    render_hero()

    st.write("")
    render_metrics()

    st.write("")
    render_feature_cards()

    st.write("")
    render_analytics()

    st.write("")
    render_workflow()

    st.divider()

    st.caption(
        "🤖 AI Job Assistant • Built with Streamlit, Gemini, Adzuna & SQLite"
    )