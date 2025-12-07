import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Business Requirement 1: Hypothesis and Validation")

    st.info(
        f"**Hypothesis** \n"
        f"* It is suspected that some of the cherry leaves have a powdery \n"
        f"on them differentiate them from a healthy cherry leaf. \n\n"
    )

    st.success(
        f"**Validation** \n\n"
        f"* text here. \n"
    )

    st.write("### Business Requirement 2: Hypothesis and Validation")

    st.info(
        f"**Hypothesis** \n"
        f"* It is suspected that some of the cherry leaves have a powdery \n"
        f"on them. The difference between \n\n"
    )

    st.success(
        f"**Validation** \n\n"
        f"* text here. \n"
    )
