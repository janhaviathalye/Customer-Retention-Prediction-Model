# Customer-Retention-Prediction-Model

American Express Women in Computer Science Engineering Shadowing Program Project

# Project Description

Overview

This project aims to develop a machine learning-based predictive model for identifying
American Express (AmEx) customers who are likely to disengage, cancel services, or
reduce their usage of Amex products. By analyzing customer behaviors and patterns,
the model will provide insights to implement effective retention strategies, improving
overall customer loyalty.

The project involves building both the frontend and backend, with a focus on visualizing
retention risks and customer engagement metrics. The frontend will offer a simple,
user-friendly interface to display and highlight relevant customer information about the
customers predicted to be on the verge of disengagement. The backend will manage
data processing, machine learning pipeline operations, and API requests.

The model will leverage data such as transaction history, demographic details, and
service usage patterns to predict churn risk. The objective is to enable Amex to
proactively engage customers at risk of leaving and reduce attrition rates through
targeted marketing or customer service initiatives.

Requirement Specifications

● Dataset used: Bank Customer Churn Model Kaggle dataset<br/>
● Pre-processing the data for usage by the model<br/>
● Feature engineering: Created more features for model performance improvement<br/>
● ML model ensemble: Built using LightGBM, SMOTE, Hyperparameter Tuning by
RandomizedSearchCV, Threshold Optimization and pipeline integration<br/>
● Backend: Python(Flask) API to automate taking in any customer dataset, run the
Customer Retention Prediction model on it and display the results<br/>
● Frontend: HTML & CSS used to display the customer names and id’s of
customers at the risk of disengagement from the dataset provided

# What Was Done & How It Was Done

● Determining which dataset and what customer fields to use:

<img src = "https://github.com/user-attachments/assets/6e07a060-3113-40ae-a13f-c35fc8ec5b13" width = "800"><br/>

I took my time to determine the right dataset for this model as the first step to
creating a robust ML model is to choose the right dataset and fields. I explored
PLAID API, different Kaggle datasets and online datasets for this project and
finally decided on this one.<br/>

● Exploring the type of dataset such as balanced or imbalanced and then deciding
the performance metrics to be used

<img src = "https://github.com/user-attachments/assets/268d6cce-529f-46cf-84b4-b9ce38b5f540" width = "800"><br/>

Exploring the dataset is equally important as it decides the next steps required to
be taken. Since this is a simulation of real world data and we are dealing with
Customer Churn prediction, the dataset was highly imbalanced. Understanding
this helped me to determine which performance metrics to be used for my model.
Accuracy, which works for most models, wouldn’t work because of this
imbalance. F-1 score, instead, was used to gauge the performances.

● Performing pre-processing steps on the data for it to be ready for usage by the
model

<img src = "https://github.com/user-attachments/assets/44a65ffb-9adb-48d1-9503-11308982c108" width = "800"><br/>

Comprehensive data pre-processing was undertaken to prepare the dataset for
effective model training. This involved cleaning the data by removing irrelevant
columns such as RowNumber, CustomerId, and Surname, which did not
contribute to the prediction of customer churn. Additionally, feature engineering
was performed to create new informative features like BalanceSalaryRatio,
CreditScoreAgeRatio, and interaction terms, enhancing the dataset's
predictive power.

Categorical variables (Geography and Gender) were transformed using
One-Hot Encoding to convert them into a numerical format suitable for machine
learning algorithms. Numerical features were standardized using
StandardScaler to ensure they had a mean of 0 and a standard deviation of 1,
facilitating faster and more efficient model convergence. To address class
imbalance, SMOTE (Synthetic Minority Over-sampling Technique) was applied
within an ImbPipeline, ensuring that the model received a balanced view of
both churned and retained customers.

● Building and executing different ML models to see their respective results on the
dataset

<img src = "https://github.com/user-attachments/assets/b788aae9-a4c1-4274-b3b2-e95397cc774d" width = "800"><br/>

Multiple machine learning models were developed and evaluated to determine
their effectiveness in predicting customer churn. Models such as Gradient
Boosting (LightGBM), Random Forest, Logistic Regression, and Support Vector
Machines (SVM) were built to compare their performance metrics, including F1
Score, Accuracy, Precision, and Recall. This comparative analysis aimed to
identify the most suitable model for our specific dataset and business objectives.

Each model was integrated into an ImbPipeline that included preprocessing
and SMOTE oversampling to ensure consistent data handling. Hyperparameter
tuning was conducted using RandomizedSearchCV with a predefined
hyperparameter grid, optimizing each model's performance efficiently. Stratified
K-Fold cross-validation was employed to maintain consistent class distribution
across training folds, providing reliable and unbiased performance estimates.
The results from these models were meticulously compared to select the
best-performing algorithm for further refinement.

● Creating a robust model for predicting customers at the risk of disengagement by
building an ensemble combining the best models together based on their
performances and output results

<img src = "https://github.com/user-attachments/assets/7cc5dcf2-26a0-49ca-9a42-7ba502c4e86c" width = "800"><br/>

To enhance prediction accuracy and model robustness, an ensemble approach
was adopted by combining the strengths of the top-performing individual models.
This ensemble, typically a stacking classifier, leverages the diverse perspectives
of multiple algorithms to capture complex data patterns and improve overall
predictive performance, particularly in identifying customers at risk of
disengagement.

The ensemble model was constructed by integrating models like LightGBM,
Random Forest, and Logistic Regression into a stacking framework, with a
meta-classifier (e.g., Logistic Regression) aggregating their predictions.
Hyperparameter tuning was again performed using RandomizedSearchCV to
optimize the ensemble's performance. The ensemble was trained within the
same ImbPipeline, ensuring consistent preprocessing and handling of class
imbalance. Cross-validation confirmed that the ensemble outperformed individual
models, achieving higher F1 scores and more balanced precision-recall
trade-offs.

● Creating a backend application in Python(Flask) to automate the execution of the
model by taking in any sample dataset

<img src = "https://github.com/user-attachments/assets/873da6a8-39df-4cf3-a54a-dc5fa4f76741" width = "800"><br/>

A backend application was developed using Python's Flask framework to
automate the execution of the predictive model. This application serves as an
interface for users to upload any sample dataset, triggers the model execution
process, and returns the evaluation metrics seamlessly, thereby streamlining the
predictive workflow.

The Flask app defines a POST endpoint (/execute-notebook) that accepts
user-uploaded CSV files as test datasets. Upon receiving a file, the app saves it
with a unique identifier and employs Papermill to execute the Jupyter Notebook
(Customer_Retention_Prediction_Model.ipynb) with the provided
dataset. After execution, the app reads the generated metrics_output.json
file containing key performance metrics and returns these metrics as a JSON
response to the user. Robust error handling ensures that any issues during
notebook execution are captured and communicated effectively, while temporary
files are cleaned up to maintain a tidy environment.

● Creating a simple, user-friendly frontend that can be used by both technical and
non-technical staff to see the results of the Customer Retention Prediction Model

<img src = "https://github.com/user-attachments/assets/5ad5156f-ec03-4e0b-8a72-b6b736023ba5" width = "800"><br/>

A user-friendly frontend interface was designed to allow both technical and
non-technical staff to interact with the Customer Retention Prediction Model
effortlessly. This interface enables users to upload test datasets and view the
resulting performance metrics without requiring deep technical knowledge,
thereby democratizing access to predictive insights.

The frontend was developed using web technologies such as HTML, CSS, and
JavaScript, ensuring a clean and intuitive user experience. It features a simple
upload form where users can select and submit their test datasets. Upon
submission, the frontend communicates with the Flask backend via HTTP POST
requests, sending the uploaded file for processing. Once the backend returns the
evaluation metrics, the frontend displays these results in an organized manner,
using visual elements like charts or summary tables to enhance readability and
comprehension. Error messages and status indicators provide feedback on the
processing status, ensuring transparency and user confidence.

● Delivering this business tool as the final output of this project

<img src = "https://github.com/user-attachments/assets/ebba42e8-d213-45ad-976d-8f1eb4db6812" width = "800"><br/>

The culmination of this project resulted in a comprehensive business tool that
integrates data preprocessing, machine learning model execution, and user
interaction into a cohesive system. This tool empowers the organization to
predict customer churn accurately and take proactive measures to enhance
retention strategies, thereby driving business growth and customer satisfaction.

The final tool combines the Flask backend and the user-friendly frontend,
allowing seamless interaction between users and the predictive model. Users
can upload any test dataset through the frontend, triggering the backend to
execute the Jupyter Notebook and process the data. The tool outputs key
performance metrics and identifies customers at risk of disengagement, providing
actionable insights.

# Resources Used

● Python<br/>
● Flask<br/>
● Jupyter Notebook<br/>
● Papermill<br/>
● Pandas<br/>
● NumPy<br/>
● Scikit-learn<br/>
● Imbalanced-learn (SMOTE)<br/>
● XGBoost<br/>
● LightGBM<br/>
● UIUD<br/>
● Matplotlib<br/>
● RandomizedSearchCV<br/>


