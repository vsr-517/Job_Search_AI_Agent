import streamlit as st

from services.database import create_table, get_saved_jobs


create_table()


st.set_page_config(
    page_title="AI Job Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>
        .block-container {
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        [data-testid="stSidebar"] {
            border-right: 1px solid rgba(128, 128, 128, 0.18);
        }

        .hero {
            padding: 2.5rem;
            border-radius: 24px;
            background:
                linear-gradient(
                    135deg,
                    rgba(79, 70, 229, 0.16),
                    rgba(14, 165, 233, 0.10)
                );
            border: 1px solid rgba(99, 102, 241, 0.22);
            margin-bottom: 1.8rem;
        }

        .hero-badge {
            display: inline-block;
            padding: 0.4rem 0.8rem;
            border-radius: 999px;
            background: rgba(99, 102, 241, 0.15);
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        .hero-title {
            font-size: 3rem;
            line-height: 1.1;
            font-weight: 800;
            margin: 0;
        }

        .hero-description {
            max-width: 760px;
            font-size: 1.08rem;
            opacity: 0.78;
            margin-top: 1rem;
            margin-bottom: 0;
        }

        .section-title {
            font-size: 1.55rem;
            font-weight: 750;
            margin-top: 1rem;
            margin-bottom: 0.25rem;
        }

        .section-description {
            opacity: 0.68;
            margin-bottom: 1rem;
        }

        .feature-card {
            min-height: 210px;
            padding: 1.45rem;
            border-radius: 20px;
            border: 1px solid rgba(128, 128, 128, 0.20);
            background: rgba(128, 128, 128, 0.045);
            transition:
                transform 0.2s ease,
                border-color 0.2s ease,
                box-shadow 0.2s ease;
        }

        .feature-card:hover {
            transform: translateY(-4px);
            border-color: rgba(99, 102, 241, 0.50);
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.08);
        }

        .feature-icon {
            font-size: 2rem;
            margin-bottom: 0.75rem;
        }

        .feature-title {
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .feature-text {
            opacity: 0.72;
            line-height: 1.6;
        }

        .status-card {
            padding: 1.25rem;
            border-radius: 18px;
            border: 1px solid rgba(128, 128, 128, 0.20);
            background: rgba(128, 128, 128, 0.045);
        }

        div[data-testid="stMetric"] {
            padding: 1.15rem;
            border-radius: 18px;
            border: 1px solid rgba(128, 128, 128, 0.20);
            background: rgba(128, 128, 128, 0.045);
        }

        div[data-testid="stMetricValue"] {
            font-size: 1.55rem;
        }

        .footer-text {
            opacity: 0.58;
            text-align: center;
            margin-top: 2rem;
            font-size: 0.9rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.title("🤖 AI Job Assistant")
    st.caption("Your intelligent career workspace")

    st.markdown("---")

    st.markdown("### Quick access")
    st.page_link(
        "pages/1_Job_Search.py",
        label="Search Jobs",
        icon="🔍",
    )

    st.caption(
        "More dedicated pages will be added for resume analysis, "
        "company research, and saved jobs."
    )

    st.markdown("---")
    st.markdown("### Project stack")
    st.write("**Frontend:** Streamlit")
    st.write("**Job API:** Adzuna")
    st.write("**AI:** Gemini")
    st.write("**Database:** SQLite")


# --------------------------------------------------
# DATA
# --------------------------------------------------

try:
    saved_jobs = get_saved_jobs()
    saved_jobs_count = len(saved_jobs)
    database_status = "Connected"
except Exception:
    saved_jobs_count = 0
    database_status = "Unavailable"


# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">AI-powered career platform</div>

        <h1 class="hero-title">
            Build a smarter path<br>
            toward your next job.
        </h1>

        <p class="hero-description">
            Search live opportunities, analyze your resume,
            research companies, and organize applications
            from one intelligent workspace.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# METRICS
# --------------------------------------------------

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric(
        label="Saved Jobs",
        value=saved_jobs_count,
        help="Jobs currently stored in your SQLite database.",
    )

with metric2:
    st.metric(
        label="Job Source",
        value="Adzuna",
        help="Live jobs are retrieved through the Adzuna API.",
    )

with metric3:
    st.metric(
        label="AI Engine",
        value="Gemini",
        help="Gemini powers resume feedback and company research.",
    )

with metric4:
    st.metric(
        label="Database",
        value=database_status,
        help="Current SQLite database connection status.",
    )


# --------------------------------------------------
# MAIN FEATURES
# --------------------------------------------------

st.markdown(
    '<p class="section-title">Your career toolkit</p>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p class="section-description">
        Everything you need to search, evaluate, and organize
        job opportunities.
    </p>
    """,
    unsafe_allow_html=True,
)

feature1, feature2, feature3, feature4 = st.columns(4)

with feature1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Live Job Search</div>
            <div class="feature-text">
                Search real job listings by role and location.
                View salary, contract information, and direct
                application links.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.page_link(
        "pages/1_Job_Search.py",
        label="Open Job Search",
        icon="🚀",
        use_container_width=True,
    )

with feature2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">📄</div>
            <div class="feature-title">Resume Analyzer</div>
            <div class="feature-text">
                Upload a PDF resume, compare it with a job
                description, calculate an ATS score, and receive
                AI-powered feedback.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.button(
        "Resume page coming next",
        disabled=True,
        use_container_width=True,
    )

with feature3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🏢</div>
            <div class="feature-title">Company Research</div>
            <div class="feature-text">
                Generate company overviews, role expectations,
                interview preparation insights, and important
                topics to study.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.button(
        "Research page coming next",
        disabled=True,
        use_container_width=True,
    )

with feature4:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">💾</div>
            <div class="feature-title">Saved Opportunities</div>
            <div class="feature-text">
                Keep important roles in one place, revisit
                application links, and remove opportunities that
                are no longer relevant.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.button(
        "Saved Jobs page coming next",
        disabled=True,
        use_container_width=True,
    )


# --------------------------------------------------
# WORKFLOW
# --------------------------------------------------

st.markdown("---")

st.markdown(
    '<p class="section-title">How the assistant works</p>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p class="section-description">
        A simple workflow designed around the real job-search process.
    </p>
    """,
    unsafe_allow_html=True,
)

step1, step2, step3 = st.columns(3)

with step1:
    with st.container(border=True):
        st.markdown("### 1. Discover")
        st.write(
            "Search live opportunities and compare jobs across "
            "multiple platforms."
        )

with step2:
    with st.container(border=True):
        st.markdown("### 2. Prepare")
        st.write(
            "Evaluate resume alignment and understand the company "
            "before applying."
        )

with step3:
    with st.container(border=True):
        st.markdown("### 3. Organize")
        st.write(
            "Save relevant opportunities and maintain a focused "
            "application list."
        )


# --------------------------------------------------
# SYSTEM STATUS
# --------------------------------------------------

st.markdown("---")

st.markdown(
    '<p class="section-title">System status</p>',
    unsafe_allow_html=True,
)

status1, status2, status3 = st.columns(3)

with status1:
    with st.container(border=True):
        st.markdown("#### 🟢 Job Search API")
        st.caption("Adzuna integration configured")

with status2:
    with st.container(border=True):
        st.markdown("#### 🟢 AI Services")
        st.caption("Gemini features configured")

with status3:
    with st.container(border=True):
        status_icon = "🟢" if database_status == "Connected" else "🔴"
        st.markdown(f"#### {status_icon} Local Database")
        st.caption(f"SQLite status: {database_status}")


st.markdown(
    """
    <p class="footer-text">
        AI Job Assistant • Built with Python, Streamlit,
        Gemini, Adzuna, and SQLite
    </p>
    """,
    unsafe_allow_html=True,
)