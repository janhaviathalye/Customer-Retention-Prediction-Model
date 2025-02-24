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

![image](https://github.com/user-attachments/assets/6e07a060-3113-40ae-a13f-c35fc8ec5b13)

