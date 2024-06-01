# Advanced Sales Analytics and Prediction Project

This project dives deep into customer sales data to provide comprehensive insights and actionable recommendations. It combines various data analysis techniques to address critical business challenges in customer retention, demand forecasting, and product recommendations.

## Table of Contents

1. Project Overview
2. Data
3. Models and Analyses
    * Churn Prediction (XGBoost)
    * Demand Forecasting (Prophet)
    * Customer Segmentation (K-Means Clustering)
    * Customer Lifetime Value (BG/NBD)
    * Association Rule Mining (Apriori)
4. Results and Insights
5. Usage
6. Limitations and Future Work
7. Contributors

## 1. Project Overview

This project goes beyond basic analysis and aims to provide a holistic view of customer behavior, product performance, and future trends. It leverages machine learning, time series forecasting, and association rule mining to generate actionable insights for:

* **Customer Retention:** Identifying high-risk customers for churn.
* **Demand Optimization:** Forecasting product demand accurately.
* **Customer Segmentation:** Understanding distinct customer groups.
* **Customer Lifetime Value (CLV):** Estimating the long-term value of each customer.
* **Product Recommendations:** Suggesting relevant products to customers.

## 2. Data

* `data_cleaned.csv`: The cleaned and preprocessed sales data, including:
    * Customer ID, Order ID, Date of Purchase, Quantity, Total Price, Product Details (ID, Name, Category, Subcategory, Range)
* Additional data sources could include (if available):
    * Customer demographics
    * Website interaction data
    * Product reviews

## 3. Models and Analyses

* **Churn Prediction:**
    * **Model:** XGBoost Classifier (potentially tuned using GridSearchCV)
    * **Features:** 
        * Transactional data (order history, recency, frequency, monetary value)
        * Additional Features (RFM scores, time since first purchase, change in purchase frequency)
    * **Evaluation:**  Accuracy, Precision, Recall, F1-score, ROC-AUC, SHAP values for feature importance analysis.

* **Demand Forecasting:**
    * **Model:** Facebook Prophet
    * **Features:**  Date, quantity sold
    * **Optional:** External regressors (holidays, promotions, etc.)
    * **Evaluation:**  MAE, MAPE, RMSE, visual inspection, backtesting.

* **Customer Segmentation:**
    * **Model:** K-Means Clustering
    * **Features:**  Selected subset from the aggregated customer data
    * **Evaluation:** Silhouette Analysis, Elbow method to determine optimal cluster number

* **Customer Lifetime Value (CLV):**
    * **Model:** Beta Geometric / Negative Binomial Distribution (BG/NBD)
    * **Features:**  Frequency, recency, and customer age (T)
    * **Evaluation:** Holdout validation using a testing set.

* **Association Rule Mining (Apriori):**
    * **Model:** Apriori algorithm
    * **Goal:** Discover relationships between products frequently purchased together
    * **Metrics:** Support, confidence, lift.


## 4. Results and Insights

[Summarize your findings here. For example:]

* We identified 2 distinct customer segments. 
* High-value customers are characterized by [characteristics].
* Top-selling products are [list of products].
* We achieved [accuracy metrics] for churn prediction and [error metrics] for demand forecasting.
* Association rule mining revealed the following interesting product bundles [list some examples].

## 5. Usage

Detailed instructions on how to run the different analyses and models within the provided Jupyter Notebooks.

## 6. Limitations and Future Work

[Discuss any limitations of the current models, assumptions made, and potential improvements, such as incorporating new data sources or experimenting with different algorithms.]

## 7. Contributors

* [Your Name]
* [Mention any other collaborators or sources you used]
