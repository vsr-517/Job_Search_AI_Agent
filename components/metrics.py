import streamlit as st

from services.database import get_saved_jobs


def get_dashboard_data():
    try:
        saved_jobs = get_saved_jobs()

        return {
            "saved_jobs": len(saved_jobs),
            "resume_analysis": 0,
            "companies_researched": 0,
            "database_status": "🟢 Online",
        }

    except Exception:
        return {
            "saved_jobs": 0,
            "resume_analysis": 0,
            "companies_researched": 0,
            "database_status": "🔴 Offline",
        }


def render_metrics():
    data = get_dashboard_data()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💾 Saved Jobs",
            data["saved_jobs"],
        )

    with col2:
        st.metric(
            "📄 Resume Analysis",
            data["resume_analysis"],
        )

    with col3:
        st.metric(
            "🏢 Companies",
            data["companies_researched"],
        )

    with col4:
        st.metric(
            "🗄 Database",
            data["database_status"],
        )