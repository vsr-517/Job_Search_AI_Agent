import streamlit as st

from services.database import get_saved_jobs


def render_recent_activity():

    st.subheader("📌 Recent Activity")

    jobs = get_saved_jobs()

    if len(jobs) == 0:
        st.info("No jobs have been saved yet.")
        return

    recent_jobs = jobs[:5]

    for job in recent_jobs:

        job_id, title, company, location, url = job

        with st.container(border=True):

            st.markdown(f"### {title}")

            st.write(f"🏢 **{company}**")

            st.write(f"📍 {location}")

            st.link_button(
                "View Job",
                url,
                use_container_width=True,
            )