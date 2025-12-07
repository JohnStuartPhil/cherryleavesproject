import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, '
             'Validation and Test Sets')
    st.info(
        f"**Summary of the above** \n\n"
        f"* Train - powdery mildew: 1,472 images \n"
        f"* Train - healthy: 1,472 images \n"
        f"* Validation - powdery mildew: 210 images \n"
        f"* Validation - healthy: 210 images \n"
        f"* Test - powdery mildew: 422 images \n"
        f"* Test - healthy: 242 images \n"
    )
    st.write("---")

    st.write("### Model History")
    col1, col2 = st.columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                              index=['Loss', 'Accuracy']))
    st.write("---")

    st.info(
        f"**Summary of the above** \n\n"
        f"* The learning curves shown above indicate that the model is a "
        f"normal fit and that the accuracy is at 99% thus meeting Business "
        f"Requirement 2."
        )
