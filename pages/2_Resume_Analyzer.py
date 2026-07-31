import streamlit as st

from services.resume_parser import extract_text_from_pdf
from services.ats_score import calculate_ats_score
from services.ai_agent import get_resume_feedback

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI Resume Analyzer")
st.caption("Analyze your resume, calculate ATS score, and receive AI-powered feedback.")

uploaded_resume = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"],
)

if uploaded_resume is not None:

    resume_text = extract_text_from_pdf(uploaded_resume)

    st.success("Resume uploaded successfully!")

    st.subheader("Extracted Resume")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300,
    )

    st.divider()

    job_description = st.text_area(
        "Paste Job Description",
        height=220,
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Calculate ATS Score"):

            score, matched_keywords = calculate_ats_score(
                resume_text,
                job_description,
            )

            st.metric("ATS Score", f"{score}%")

            st.write("Matched Keywords")

            st.write(matched_keywords[:30])

    with col2:

        if st.button("Get AI Feedback"):

            if job_description.strip() == "":
                st.warning("Please paste a Job Description first.")

            else:

                with st.spinner("Analyzing Resume..."):

                    feedback = get_resume_feedback(
                        resume_text,
                        job_description,
                    )

                st.subheader("AI Feedback")

                st.write(feedback)