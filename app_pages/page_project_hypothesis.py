import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Business Requirement 1: Hypothesis and Validation")

    st.info(
        f"**Hypothesis** \n"
        f"* We are already aware that there is a visable difference \n"
        f"between a healthy cherry leaf and a cherry leaf with a powdery \n"
        f"mildew on it. \n\n"
    )

    st.success(
        f"**Validation** \n\n"
        f"* text here. \n"
    )

    st.write("### Business Requirement 2: Hypothesis and Validation")

    st.info(
        f"**Hypothesis** \n"
        f"* It is requirement that when an image of a cherry leaf is  \n"
        f"uploaded to the site that is predicts if the cherry leaf is \n"
        f"healthy or has powdery mildew with an accuracy of at least 97% \n\n"
    )

    st.success(
        f"**Validation** \n\n"
        f"* n order to carry this out, a model shall be trained using \n"
        f"the images and calculating the accuracy with accuracy rate \n"
        f"of at least 97%. \n\n"
    )
