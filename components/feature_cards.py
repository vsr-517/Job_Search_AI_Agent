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
    st.subheader("Your Career Toolkit")
    st.caption(
        "Search, evaluate, research, and organize job opportunities."
    )

    column1, column2, column3, column4 = st.columns(4)

    # Job Search
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

    # Resume Analyzer
    with column2:
        feature_card(
            "📄",
            "Resume Analyzer",
            "Calculate an ATS score and receive AI feedback.",
        )

        st.page_link(
            "pages/2_Resume_Analyzer.py",
            label="Open Resume Analyzer",
            icon="📄",
            use_container_width=True,
        )

    # Company Research
    with column3:
        feature_card(
            "🏢",
            "Company Research",
            "Research companies and prepare for interviews.",
        )

        st.page_link(
            "pages/3_Company_Research.py",
            label="Open Company Research",
            icon="🏢",
            use_container_width=True,
        )

    # Saved Jobs
    with column4:
        feature_card(
            "💾",
            "Saved Jobs",
            "Manage your saved job applications.",
        )

        st.page_link(
            "pages/4_Saved_Jobs.py",
            label="Open Saved Jobs",
            icon="💾",
            use_container_width=True,
        )