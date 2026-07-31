import streamlit as st

from services.ai_agent import get_company_research

st.set_page_config(
    page_title="Company Research",
    page_icon="🏢",
    layout="wide",
)

st.title("🏢 AI Company Research")
st.caption("Research companies and prepare for interviews using AI.")

company_name = st.text_input(
    "Company Name",
    placeholder="Example: Google",
)

job_role = st.text_input(
    "Job Role",
    value="Software Engineer",
)

if st.button("Research Company", type="primary"):

    if company_name.strip() == "":
        st.warning("Please enter a company name.")

    else:

        with st.spinner("Researching company..."):

            result = get_company_research(
                company_name,
                job_role,
            )

        st.success("Research completed!")

        st.markdown(result)