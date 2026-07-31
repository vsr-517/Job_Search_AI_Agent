import pandas as pd
import plotly.express as px
import streamlit as st

from services.database import get_saved_jobs


def render_analytics():

    jobs = get_saved_jobs()

    if len(jobs) == 0:
        return

    df = pd.DataFrame(
        jobs,
        columns=[
            "ID",
            "Title",
            "Company",
            "Location",
            "URL",
        ],
    )

    st.subheader("📊 Dashboard Analytics")

    col1, col2 = st.columns(2)

    with col1:

        location_counts = (
            df["Location"]
            .value_counts()
            .reset_index()
        )

        location_counts.columns = [
            "Location",
            "Jobs",
        ]

        fig = px.bar(
            location_counts,
            x="Location",
            y="Jobs",
            title="Jobs by Location",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with col2:

        company_counts = (
            df["Company"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        company_counts.columns = [
            "Company",
            "Jobs",
        ]

        fig = px.pie(
            company_counts,
            values="Jobs",
            names="Company",
            title="Top Companies",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )