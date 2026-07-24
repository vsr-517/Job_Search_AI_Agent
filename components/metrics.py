import streamlit as st

from services.database import get_saved_jobs


def get_dashboard_data():
    try:
        saved_jobs = get_saved_jobs()

        return {
            "saved_jobs": len(saved_jobs),
            "database_status": "Connected",
        }

    except Exception:
        return {
            "saved_jobs": 0,
            "database_status": "Unavailable",
        }


def render_metrics():
    data = get_dashboard_data()

    column1, column2, column3, column4 = st.columns(4)

    with column1:
        st.metric(
            "Saved Jobs",
            data["saved_jobs"],
        )

    with column2:
        st.metric(
            "Job Source",
            "Adzuna",
        )

    with column3:
        st.metric(
            "AI Engine",
            "Gemini",
        )

    with column4:
        st.metric(
            "Database",
            data["database_status"],
        )
