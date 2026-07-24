import streamlit as st
from urllib.parse import quote_plus

from services.job_service import JobAPIError, search_jobs
from services.database import save_job


st.set_page_config(
    page_title="Job Search",
    page_icon="🔍",
    layout="wide",
)

st.title("🔍 Job Search")
st.write("Search live job opportunities using the Adzuna API.")


if "search_results" not in st.session_state:
    st.session_state.search_results = []


col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    query = st.text_input(
        "Job Role",
        value="Python Developer",
        placeholder="Example: Data Analyst",
    )

with col2:
    location = st.text_input(
        "Location",
        value="India",
        placeholder="Example: Delhi",
    )

with col3:
    results_count = st.selectbox(
        "Number of results",
        options=[5, 10, 15, 20],
    )


search_button = st.button(
    "Search Jobs",
    type="primary",
)


if search_button:
    try:
        with st.spinner("Searching for jobs..."):
            jobs = search_jobs(
                query=query,
                location=location,
                results_count=results_count,
            )

        st.session_state.search_results = jobs

        if jobs:
            st.success(f"Found {len(jobs)} job opportunities.")
        else:
            st.info("No jobs found. Try another role or location.")

    except ValueError as error:
        st.warning(str(error))
        st.session_state.search_results = []

    except JobAPIError as error:
        st.error(str(error))
        st.session_state.search_results = []


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

    link_col1, link_col2, link_col3, link_col4 = st.columns(4)

    with link_col1:
        st.link_button(
            "Internshala",
            internshala_url,
            use_container_width=True,
        )

    with link_col2:
        st.link_button(
            "Unstop",
            unstop_url,
            use_container_width=True,
        )

    with link_col3:
        st.link_button(
            "Naukri",
            naukri_url,
            use_container_width=True,
        )

    with link_col4:
        st.link_button(
            "LinkedIn",
            linkedin_url,
            use_container_width=True,
        )

    st.markdown("---")

    for index, job in enumerate(jobs):
        title = job.get("title", "Job title unavailable")

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

        salary_min = job.get("salary_min")
        salary_max = job.get("salary_max")

        contract_type = job.get(
            "contract_type",
            "Not specified",
        )

        created_date = job.get(
            "created",
            "Not available",
        )

        if len(description) > 500:
            description = description[:500] + "..."

        with st.container(border=True):
            st.markdown(f"### {title}")
            st.write(f"**Company:** {company}")
            st.write(f"**Location:** {job_location}")
            st.write(f"**Contract:** {contract_type}")
            st.write(f"**Posted:** {created_date}")

            if salary_min or salary_max:
                salary_text = (
                    f"₹{salary_min or 'N/A'} - ₹{salary_max or 'N/A'}"
                )
                st.write(f"**Salary:** {salary_text}")

            st.write(description)

            button_col1, button_col2 = st.columns(2)

            with button_col1:
                st.link_button(
                    "Apply / View Job",
                    job_url,
                    use_container_width=True,
                )

            with button_col2:
                save_clicked = st.button(
                    "Save Job",
                    key=f"save_job_{index}",
                    use_container_width=True,
                )

            if save_clicked:
                saved = save_job(
                    title,
                    company,
                    job_location,
                    job_url,
                )

                if saved:
                    st.success(f"Saved: {title}")
                else:
                    st.warning("This job is already saved.")