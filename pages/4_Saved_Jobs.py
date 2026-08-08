import streamlit as st

from services.database import get_saved_jobs, delete_job


st.set_page_config(
    page_title="Saved Jobs",
    page_icon="💾",
    layout="wide",
)


st.title("💾 Saved Jobs")
st.caption("Manage your saved job opportunities.")


jobs = get_saved_jobs()


if not jobs:

    st.info("You haven't saved any jobs yet.")

else:

    st.success(f"{len(jobs)} saved jobs found.")

    for job in jobs:

        job_id, title, company, location, url = job

        with st.container(border=True):

            st.subheader(title)

            st.write(f"**Company:** {company}")
            st.write(f"**Location:** {location}")

            col1, col2 = st.columns(2)

            with col1:

                st.link_button(
                    "View Job",
                    url,
                    use_container_width=True,
                )

            with col2:

                if st.button(
                    "Delete Job",
                    key=f"delete_{job_id}",
                    use_container_width=True,
                ):

                    delete_job(job_id)

                    st.success("Job deleted successfully.")

                    st.rerun()