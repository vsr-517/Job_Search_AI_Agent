import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.title("🤖 AI Job Assistant")
        st.caption("Your intelligent career workspace")

        st.divider()

        st.page_link(
            "app.py",
            label="Dashboard",
            icon="🏠",
        )

        st.page_link(
            "pages/1_Job_Search.py",
            label="Search Jobs",
            icon="🔍",
        )

        st.divider()

        st.markdown("### Project stack")
        st.caption("Frontend: Streamlit")
        st.caption("Job API: Adzuna")
        st.caption("AI: Gemini")
        st.caption("Database: SQLite")
