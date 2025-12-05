import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Marianne McGuineys, is the head of IT and Innovation at Farmy & \n"
        f"Foods, a company in the agricultural sector that produces and \n"
        f"harvests different types of food. Recently, she is facing a \n"
        f"challenge where their cherry plantations have been presenting \n"
        f"powdery mildew, which is a fungal disease that affects a wide \n"
        f"range of plants.\n"
        f"* The cherry plantation crop is one of their finest products in \n"
        f"the portfolio and the company is concerned about supplying the \n"
        f"market with a product of compromised quality.\n"
        f"* Currently, the process is to manually verify if a given cherry \n"
        f"tree contains powdery mildew. An employee spends around 30 \n"
        f"minutes in each tree, taking a few samples of tree leaves and \n"
        f"verifying visually if the leaf tree is healthy or has powdery \n"
        f"mildew. If it has powdery mildew, the employee applies a \n"
        f"specific compound to kill the fungus. The time spent applying \n"
        f"this is 1 minute. The company has thousands of cherry leaves \n"
        f"located in multipe farms across the country. As a result, this\n"
        f"manual process is not scalable due to time spent in the manual \n"
        f"process inspeaction. \n"
        f"* To save time in this process, the IT team suggested an ML system\n"
        f" that is capable of detecting instantly, using a tree leaf image,\n"
        f"if it is healthy or has powdery mildew. A similar manual process \n"
        f"is in place for other crops for detecting pests, and if this \n"
        f"initiative is successful, there is a realistic chance to replicate\n"
        f" this project to all other crops. The dataset is a collection of \n"
        f"cherry leaf images provided by Farmy & Foods, taken from their \n"
        f"crops. \n"
        f"\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4,208 images of cherry leaves, \n"
        f"2,104 of which are healthly and 2,104 of which contain a powdery \n"
        f"mildew. \n"
        f".")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file]"
        f'(https://github.com/JohnStuartPhil/cherryleaves/blob/main/README.md)'
    )

    st.success(
        f"**The project has 2 business requirements:** \n"
        f"* 1 - The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that contains\n"
        f" powdery mildew. \n"
        f"* 2 - The client is interested in predicting if a cherry leaf is \n"
        f"healthy or contains powdery mildew. \n"
        )
