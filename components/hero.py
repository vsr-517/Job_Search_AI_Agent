import streamlit as st


def render_hero():
    hero_html = """
<div class="hero-card">
<div class="hero-badge">AI-powered career platform</div>

<h1 class="hero-title">Build a smarter path toward your next job.</h1>

<p class="hero-description">
Search live opportunities, analyze your resume, research companies,
and organize applications from one intelligent workspace.
</p>
</div>
"""

    st.markdown(
        hero_html,
        unsafe_allow_html=True,
    )

    st.page_link(
        "pages/1_Job_Search.py",
        label="Start searching for jobs",
        icon="🚀",
    )