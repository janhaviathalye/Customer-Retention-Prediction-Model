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

I took my time to determine the right dataset for this model as the first step to
creating a robust ML model is to choose the right dataset and fields. I explored
PLAID API, different Kaggle datasets and online datasets for this project and
finally decided on this one.

<img src = "https://github.com/user-attachments/assets/6e07a060-3113-40ae-a13f-c35fc8ec5b13" width = "800"><br/>


● Exploring the type of dataset such as balanced or imbalanced and then deciding
the performance metrics to be used

![image](https://github.com/user-attachments/assets/268d6cce-529f-46cf-84b4-b9ce38b5f540)

Exploring the dataset is equally important as it decides the next steps required to
be taken. Since this is a simulation of real world data and we are dealing with
Customer Churn prediction, the dataset was highly imbalanced. Understanding
this helped me to determine which performance metrics to be used for my model.
Accuracy, which works for most models, wouldn’t work because of this
imbalance. F-1 score, instead, was used to gauge the performances.


● Performing pre-processing steps on the data for it to be ready for usage by the
model

![image](https://github.com/user-attachments/assets/44a65ffb-9adb-48d1-9503-11308982c108)

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

![image](https://github.com/user-attachments/assets/b788aae9-a4c1-4274-b3b2-e95397cc774d)

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




