import streamlit as st
from urllib.parse import quote_plus
from services.ai_agent import get_resume_feedback, get_company_research
from services.job_api import search_jobs
from services.resume_parser import extract_text_from_pdf
from services.ats_score import calculate_ats_score
from services.database import create_table, save_job, get_saved_jobs
create_table()
st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("🤖 AI Career Assistant")
page = st.sidebar.radio(
    "Navigation",
    ["Job Search", "Resume Analyzer", "Company Research", "Saved Jobs"]
)

if page == "Job Search":
    st.title("🔍 Job Search Dashboard")
    st.write("Search live jobs using Adzuna API and explore other platforms.")

    col1, col2 = st.columns(2)

    with col1:
        query = st.text_input("Job Role", "data analyst")

    with col2:
        location = st.text_input("Location", "India")

    search_button = st.button("Search Jobs")

    if search_button:
        jobs = search_jobs(query, location)

        st.subheader(f"Jobs Found: {len(jobs)}")

        internshala_url = f"https://internshala.com/jobs/keywords-{quote_plus(query)}/"
        unstop_url = f"https://unstop.com/jobs?search={quote_plus(query)}"
        naukri_url = f"https://www.naukri.com/{quote_plus(query)}-jobs-in-{quote_plus(location)}"
        linkedin_url = f"https://www.linkedin.com/jobs/search/?keywords={quote_plus(query)}&location={quote_plus(location)}"

        st.markdown("### Explore on Other Platforms")
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.link_button("Internshala", internshala_url)
        with c2:
            st.link_button("Unstop", unstop_url)
        with c3:
            st.link_button("Naukri", naukri_url)
        with c4:
            st.link_button("LinkedIn", linkedin_url)

        st.markdown("---")

        for job in jobs:
            with st.container(border=True):
                st.markdown(f"### {job.get('title', 'No title')}")
                st.write("**Company:**", job.get("company", {}).get("display_name", "Not available"))
                st.write("**Location:**", job.get("location", {}).get("display_name", "Not available"))
                st.write("**Description:**", job.get("description", "No description available")[:500])
                st.link_button("Apply / View Job", job.get("redirect_url", "#"))
                if st.button("Save Job", key=job.get("id", job.get("redirect_url"))):
                    save_job(
                        job.get("title", "No title"),
                        job.get("company", {}).get("display_name", "Not available"),
                        job.get("location", {}).get("display_name", "Not available"),
                        job.get("redirect_url", "#")
                    )
                    st.success("Job saved!")

elif page == "Resume Analyzer":
    st.title("📄 Resume Analyzer")
    st.write("Upload your resume PDF and extract text for analysis.")

    uploaded_resume = st.file_uploader("Upload Resume PDF", type=["pdf"])

    if uploaded_resume is not None:
        resume_text = extract_text_from_pdf(uploaded_resume)

        st.success("Resume uploaded successfully!")

        st.subheader("Extracted Resume Text")
        st.text_area("Resume Content", resume_text, height=300)
        
        st.subheader("ATS Score Checker")

        job_description = st.text_area("Paste Job Description Here", height=200)

        if st.button("Calculate ATS Score"):
            score, matched_keywords = calculate_ats_score(resume_text, job_description)

            st.metric("ATS Score", f"{score}%")

            st.write("Matched Keywords:")
            st.write(matched_keywords[:30])
        if st.button("Get AI Resume Feedback"):
            if job_description.strip() == "":
                st.warning("Please paste a job description first.")
            else:
                with st.spinner("Gemini is analyzing your resume..."):
                    feedback = get_resume_feedback(resume_text, job_description)

                st.subheader("AI Resume Feedback")
                st.write(feedback)

elif page == "Company Research":
    st.title("🏢 Company Research")
    st.write("Get AI-powered company and role insights.")

    company_name = st.text_input("Enter Company Name")
    job_role = st.text_input("Enter Job Role", "data analyst")

    if st.button("Research Company"):
        if company_name.strip() == "":
            st.warning("Please enter a company name.")
        else:
            with st.spinner("Researching company..."):
                result = get_company_research(company_name, job_role)

            st.subheader("Company Research Result")
            st.write(result)

elif page == "Saved Jobs":
    st.title("💾 Saved Jobs")

    saved_jobs = get_saved_jobs()

    if len(saved_jobs) == 0:
        st.info("No saved jobs yet.")
    else:
        for job in saved_jobs:
            title, company, location, url = job

            with st.container(border=True):
                st.markdown(f"### {title}")
                st.write("**Company:**", company)
                st.write("**Location:**", location)
                st.link_button("View Job", url)