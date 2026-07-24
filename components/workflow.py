import streamlit as st


def render_workflow():
    st.divider()
    st.subheader("How it works")

    column1, column2, column3 = st.columns(3)

    with column1:
        with st.container(border=True):
            st.markdown("### 1. Discover")
            st.write(
                "Search live opportunities by role and location."
            )

    with column2:
        with st.container(border=True):
            st.markdown("### 2. Prepare")
            st.write(
                "Analyze your resume and research the company."
            )

    with column3:
        with st.container(border=True):
            st.markdown("### 3. Organize")
            st.write(
                "Save relevant opportunities for later."
            )
