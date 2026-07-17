import streamlit as st
from urllib.parse import quote_plus

from services.job_service import JobAPIError, search_jobs
from services.resume_parser import extract_text_from_pdf
from services.ats_score import calculate_ats_score
from services.ai_agent import (
    get_resume_feedback,
    get_company_research,
)
from services.database import create_table, save_job, get_saved_jobs


# Create the database table when the application starts.
create_table()


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="AI Job Assistant",
    page_icon="🤖",
    layout="wide",
)


# ---------------- CUSTOM CSS ----------------

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        color: #777;
        margin-bottom: 25px;
    }

    div[data-testid="stMetric"] {
        background-color: rgba(120, 120, 120, 0.08);
        border: 1px solid rgba(120, 120, 120, 0.15);
        padding: 14px;
        border-radius: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------- SESSION STATE ----------------

if "search_results" not in st.session_state:
    st.session_state.search_results = []


# ---------------- SIDEBAR ----------------

st.sidebar.title("🤖 AI Job Assistant")
st.sidebar.caption("Track A Job Search Project")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Job Search",
        "Resume Analyzer",
        "Company Research",
        "Saved Jobs",
    ],
)


# ====================================================
# DASHBOARD
# ====================================================

if page == "Dashboard":
    st.markdown(
        '<p class="main-title">AI Job Assistant</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="subtitle">
        Find jobs, improve your resume, prepare for interviews,
        and manage your career journey.
        </p>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Live Job Search", "Adzuna API")

    with col2:
        st.metric("Resume Analysis", "PDF + ATS")

    with col3:
        st.metric("AI Features", "Gemini")

    with col4:
        st.metric("Saved Jobs", len(get_saved_jobs()))

    st.markdown("---")
    st.subheader("Available Tools")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):
            st.markdown("### 🔍 Job Search")
            st.write("Search live jobs by role and location.")

        with st.container(border=True):
            st.markdown("### 📄 Resume Analyzer")
            st.write("Upload a resume and calculate an ATS score.")

    with c2:
        with st.container(border=True):
            st.markdown("### 🏢 Company Research")
            st.write(
                "Generate company and interview insights using Gemini."
            )

        with st.container(border=True):
            st.markdown("### 💾 Saved Jobs")
            st.write("Store opportunities in the SQLite database.")


# ====================================================
# JOB SEARCH
# ====================================================

elif page == "Job Search":
    st.title("🔍 Job Search")
    st.write("Search live job opportunities using the Adzuna API.")

    form_col1, form_col2, form_col3 = st.columns([2, 2, 1])

    with form_col1:
        query = st.text_input(
            "Job Role",
            value="Python Developer",
            placeholder="Example: Data Analyst",
            key="job_role_input",
        )

    with form_col2:
        location = st.text_input(
            "Location",
            value="India",
            placeholder="Example: Delhi",
            key="job_location_input",
        )

    with form_col3:
        results_count = st.selectbox(
            "Number of results",
            options=[5, 10, 15, 20],
            index=0,
            key="results_count_input",
        )

    search_button = st.button(
        "Search Jobs",
        type="primary",
        key="main_search_button",
    )

    if search_button:
        try:
            with st.spinner("Searching for jobs..."):
                jobs = search_jobs(
                    query=query,
                    location=location,
                    results_count=results_count,
                )

            # Store results so they remain visible after clicking Save Job.
            st.session_state.search_results = jobs

            if jobs:
                st.success(
                    f"Found {len(jobs)} job opportunities."
                )
            else:
                st.info(
                    "No jobs found. Try a different role or location."
                )

        except ValueError as error:
            st.session_state.search_results = []
            st.warning(str(error))

        except JobAPIError as error:
            st.session_state.search_results = []
            st.error(str(error))

        except Exception as error:
            st.session_state.search_results = []
            st.error(f"Unexpected error: {error}")

    jobs = st.session_state.search_results

    if jobs:
        st.markdown("### Explore on Other Platforms")

        encoded_query = quote_plus(query)
        encoded_location = quote_plus(location)

        internshala_url = (
            f"https://internshala.com/jobs/keywords-{encoded_query}/"
        )
        unstop_url = (
            f"https://unstop.com/jobs?search={encoded_query}"
        )
        naukri_url = (
            f"https://www.naukri.com/"
            f"{encoded_query}-jobs-in-{encoded_location}"
        )
        linkedin_url = (
            "https://www.linkedin.com/jobs/search/"
            f"?keywords={encoded_query}&location={encoded_location}"
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.link_button(
                "Internshala",
                internshala_url,
                use_container_width=True,
            )

        with c2:
            st.link_button(
                "Unstop",
                unstop_url,
                use_container_width=True,
            )

        with c3:
            st.link_button(
                "Naukri",
                naukri_url,
                use_container_width=True,
            )

        with c4:
            st.link_button(
                "LinkedIn",
                linkedin_url,
                use_container_width=True,
            )

        st.markdown("---")
        st.subheader(f"Jobs Found: {len(jobs)}")

        for index, job in enumerate(jobs):
            title = job.get(
                "title",
                "Job title unavailable",
            )

            company = job.get("company", {}).get(
                "display_name",
                "Company unavailable",
            )

            job_location = job.get("location", {}).get(
                "display_name",
                "Location unavailable",
            )

            description = job.get(
                "description",
                "No description available.",
            )

            job_url = job.get("redirect_url", "#")

            if len(description) > 500:
                description = description[:500] + "..."

            with st.container(border=True):
                st.markdown(f"### {title}")
                st.write(f"**Company:** {company}")
                st.write(f"**Location:** {job_location}")
                st.write(description)

                button_col1, button_col2 = st.columns(2)

                with button_col1:
                    st.link_button(
                        "Apply / View Job",
                        job_url,
                        use_container_width=True,
                        key=f"view_job_{index}",
                    )

                with button_col2:
                    save_clicked = st.button(
                        "Save Job",
                        key=f"save_job_{index}",
                        use_container_width=True,
                    )

                if save_clicked:
                    try:
                        save_job(
                            title,
                            company,
                            job_location,
                            job_url,
                        )
                        st.success(f"Saved: {title}")

                    except Exception as error:
                        st.error(
                            f"Could not save the job: {error}"
                        )


# ====================================================
# RESUME ANALYZER
# ====================================================

elif page == "Resume Analyzer":
    st.title("📄 Resume Analyzer")
    st.write(
        "Upload your resume PDF and compare it with a job description."
    )

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        key="resume_upload",
    )

    if uploaded_resume is not None:
        try:
            resume_text = extract_text_from_pdf(uploaded_resume)

            if not resume_text.strip():
                st.warning(
                    "No readable text was found in the PDF."
                )
            else:
                st.success("Resume uploaded successfully!")

                with st.expander("View Extracted Resume Text"):
                    st.text_area(
                        "Resume Content",
                        resume_text,
                        height=300,
                        key="resume_content",
                    )

                st.subheader("ATS Score Checker")

                job_description = st.text_area(
                    "Paste Job Description Here",
                    height=200,
                    key="resume_job_description",
                )

                action_col1, action_col2 = st.columns(2)

                with action_col1:
                    calculate_button = st.button(
                        "Calculate ATS Score",
                        type="primary",
                        key="calculate_ats_button",
                        use_container_width=True,
                    )

                with action_col2:
                    feedback_button = st.button(
                        "Get AI Resume Feedback",
                        key="resume_feedback_button",
                        use_container_width=True,
                    )

                if calculate_button:
                    if not job_description.strip():
                        st.warning(
                            "Please paste a job description first."
                        )
                    else:
                        score, matched_keywords = (
                            calculate_ats_score(
                                resume_text,
                                job_description,
                            )
                        )

                        st.metric("ATS Score", f"{score}%")
                        st.progress(
                            min(max(int(score), 0), 100)
                        )

                        st.write("**Matched Keywords:**")

                        if matched_keywords:
                            st.write(matched_keywords[:30])
                        else:
                            st.info(
                                "No matching keywords were found."
                            )

                if feedback_button:
                    if not job_description.strip():
                        st.warning(
                            "Please paste a job description first."
                        )
                    else:
                        with st.spinner(
                            "Gemini is analyzing your resume..."
                        ):
                            feedback = get_resume_feedback(
                                resume_text,
                                job_description,
                            )

                        st.subheader("AI Resume Feedback")
                        st.markdown(feedback)

        except Exception as error:
            st.error(f"Could not analyze the resume: {error}")


# ====================================================
# COMPANY RESEARCH
# ====================================================

elif page == "Company Research":
    st.title("🏢 Company Research")
    st.write("Get AI-powered company and role insights.")

    company_name = st.text_input(
        "Enter Company Name",
        key="company_name_input",
    )

    job_role = st.text_input(
        "Enter Job Role",
        value="Data Analyst",
        key="company_job_role_input",
    )

    research_button = st.button(
        "Research Company",
        type="primary",
        key="research_company_button",
    )

    if research_button:
        if not company_name.strip():
            st.warning("Please enter a company name.")

        elif not job_role.strip():
            st.warning("Please enter a job role.")

        else:
            try:
                with st.spinner("Researching company..."):
                    result = get_company_research(
                        company_name,
                        job_role,
                    )

                st.subheader("Company Research Result")
                st.markdown(result)

            except Exception as error:
                st.error(
                    f"Company research failed: {error}"
                )


# ====================================================
# SAVED JOBS
# ====================================================

elif page == "Saved Jobs":
    st.title("💾 Saved Jobs")

    try:
        saved_jobs = get_saved_jobs()
    except Exception as error:
        st.error(f"Could not load saved jobs: {error}")
        saved_jobs = []

    if not saved_jobs:
        st.info("No saved jobs yet.")

    else:
        st.success(
            f"You have {len(saved_jobs)} saved job opportunities."
        )

        for index, job in enumerate(saved_jobs):
            title, company, location, url = job

            with st.container(border=True):
                st.markdown(f"### {title}")
                st.write(f"**Company:** {company}")
                st.write(f"**Location:** {location}")

                st.link_button(
                    "View Job",
                    url,
                    key=f"saved_job_link_{index}",
                )