

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains over 4,000 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and Validation

- List here your project hypothesis(es) and how you envision validating it (them).

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

#### Summary page
- Contains General Infomration about the client's background, infomration about the dataset, a link to the README file and the business requirements.
  
#### Cherry Leaves Visualiser page
- Shows the difference between average and variability image
- Shows the differences between average powdery mildew cherry leaves and average healthy cherry leaves
- Provides an image montage

#### Powdery Mildew Detection page
- Provides a link to download a set of health and powdery mildew cherry leaves
- Provides a user interface with a file uploader widget to allow the user to apply any image of a cherry leaf and give a prediction as to whther the leaf is healthy or has powdery mildew on it.
- When the result (healthy or powdery mildew) is povided, a table with the image name and prediction results, and a download button to download the table is also provided.

#### Hypothesis page
- A page indicatuing the hypothesis and explanation of validation.

#### ML Performance Metrics
- A technical page displaying the model performance.


## PEP8 Checks

- All 10 pages that ended with **.py** were PEP8 checked for errors using [CI Python Linter](https://pep8ci.herokuapp.com).
- All 10 pages return no errors.

### app_pages/mulipage.py

![multipage_PEP8](assets/imagesforreadme/01_multipage.png)

### app_pages/page_detector.py

![page_detector_PEP8](assets/imagesforreadme/02_page_detector.png)

### app_pages/page_ml_performance.py

![ml_performance_PEP8](assets/imagesforreadme/03_ml_performance.png)

### app_pages/page_project_hypothesis.py

![summary_PEP8](assets/imagesforreadme/04_hypothesis.png)

### app_pages/page_summary.py

![summary_PEP8](assets/imagesforreadme/05_summary.png)

### app_pages/page_visualiser.py

![visualiser_PEP8](assets/imagesforreadme/06_visualiser.png)

### src/machine_learning/evaluate_clf.py

![evaluate_clf_PEP8](assets/imagesforreadme/07_evaluate_clf.png)

### src/machine_learning/predictive_analysis.py

![predictive_analysis_PEP8](assets/imagesforreadme/08_predictive_analysis.png)

### src/data_management.py

![data_management_PEP8](assets/imagesforreadme/09_data_management.png)

### app.py

![app_PEP8](assets/imagesforreadme/10_app.png)

## Testing

| Test  | Page  | Action  | Result  | Pass/Fail  |
|---|---|---|---|---|
| 1  |  Summary | Test  | Outcome  | Pass  |
| 2  |  Cherry Leaves Visulaiser | Test | Outcome  | Pass  |
| 3  |  Powdery Mildew Detection | Test | Outcome  |  Pass |
| 4  |  Hypothesis | Test  | Outcome  | Pass  |
| 5  |  ML Performance | Test | Outcome  | Pass  |

## Deployment

### Render

- The App live link is: [Cherry Leaves Mildew Detection](https://jsp-mildew-detection-in-cherry-leaves.onrender.com)
- The project was deployed to Render using the following steps.

1. Log in to Render and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.
- NumPy -
- Pandas -
- Matplotlib -
- Seaborn -
- Plotly -
- Pillow -
- Streamlit - used for the app interface which is deployed to Render
- Joblib - 
- Scikit-learn - used for predictive analysis
- TensorFlow and Keras - used to train the model


## Credits

- The majority of code used for this project was taken from the Code Institue Malaria Detection Walkthrough project and edited accordingly.

## Acknowledgements (optional)

- Tutor: Niel
- Tutor: Tom
