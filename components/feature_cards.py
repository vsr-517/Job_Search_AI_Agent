import streamlit as st


def feature_card(icon, title, description):
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_feature_cards():
    st.subheader("Your career toolkit")
    st.caption(
        "Search, evaluate, research, and organize job opportunities."
    )

    column1, column2, column3, column4 = st.columns(4)

    with column1:
        feature_card(
            "🔍",
            "Live Job Search",
            "Search real job listings by role and location.",
        )

        st.page_link(
            "pages/1_Job_Search.py",
            label="Open Job Search",
            icon="🚀",
            use_container_width=True,
        )

    with column2:
        feature_card(
            "📄",
            "Resume Analyzer",
            "Calculate an ATS score and receive AI feedback.",
        )

        st.button(
            "Coming next",
            key="resume_coming_next",
            disabled=True,
            use_container_width=True,
        )

    with column3:
        feature_card(
            "🏢",
            "Company Research",
            "Generate company and interview preparation insights.",
        )

        st.button(
            "Coming soon",
            key="research_coming_soon",
            disabled=True,
            use_container_width=True,
        )

    with column4:
        feature_card(
            "💾",
            "Saved Jobs",
            "Keep useful opportunities together in one place.",
        )

        st.button(
            "Coming soon",
            key="saved_jobs_coming_soon",
            disabled=True,
            use_container_width=True,
        )
