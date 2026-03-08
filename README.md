# Customer-Segmentation-Churn-Pattern-Analytics-in-European-Banking
A data analytics project that explores customer churn behavior using EDA, segmentation analysis, and an interactive Streamlit dashboard to identify high-risk customer segments and provide data-driven retention insights. 


<h1>🏦 Customer Segmentation & Churn Pattern Analytics in European Banking</h1>

<h2>📊 Project Overview</h2>

Customer churn is one of the most critical challenges in the banking industry, directly affecting revenue, customer trust, and long-term profitability.

This project analyzes customer churn patterns in a European banking dataset using Exploratory Data Analysis (EDA), customer segmentation, and interactive data visualization.

The objective is to uncover hidden patterns in customer behavior and identify high-risk customer segments that are more likely to leave the bank.

To present insights effectively, an interactive Streamlit dashboard was developed with KPIs, analytical modules, and drill-down capabilities that allow users to explore churn patterns dynamically.

<h2>🎯 Project Objectives</h2>

The main objectives of this project are:

✔ Measure the overall customer churn rate

✔ Identify churn distribution across customer segments

✔ Compare churn behavior across European regions

✔ Analyze demographic and financial factors affecting churn

✔ Provide data-driven recommendations to improve customer retention

<h2>📂 Dataset Overview</h2>

The dataset represents 10,000 banking customers from European regions including France, Germany, and Spain.

It contains demographic, financial, and behavioral attributes that help analyze churn patterns.

<h2>🔑 Key Features</h2>
Feature	Description
CreditScore	Customer credit rating
Geography	Customer region (France, Germany, Spain)
Gender	Male / Female
Age	Customer age
Tenure	Years with the bank
Balance	Account balance
NumOfProducts	Number of bank products used
HasCrCard	Credit card ownership
IsActiveMember	Whether the customer is active
EstimatedSalary	Estimated annual salary
Exited	Churn indicator
<h3>🎯 Target Variable</h3>

Exited

0 → Customer Retained

1 → Customer Churned

<h2>🧹 Data Preprocessing</h2>

Before performing analysis, several preprocessing steps were conducted:

✔ Removed unnecessary columns (RowNumber, CustomerId, Surname)

✔ Checked for missing values

✔ Verified data types

✔ Performed data cleaning and validation

✔ Prepared the dataset for EDA and dashboard visualization

<h2>🔍 Exploratory Data Analysis (EDA)</h2>

EDA was performed to understand patterns and relationships within the dataset.

The analysis focused on:

📊 Customer demographics

📊 Regional churn patterns

📊 Credit score impact on churn

📊 Account balance behavior

📊 Customer engagement levels

📊 Product usage patterns

<h2>📈 Key Visualizations</h2>

The following visual analyses were performed:

Churn distribution

Churn by geography

Age vs churn analysis

Balance distribution

Active vs inactive customer comparison

Product usage behavior

These visualizations helped identify segments with the highest churn risk.

<h2>🖥️ Streamlit Interactive Dashboard</h2>

To present insights interactively, a Streamlit web dashboard was developed.

The dashboard allows users to explore churn patterns using visual analytics and interactive filters.

<h2>📊 Key Performance Indicators (KPIs)</h2>

The dashboard highlights important metrics including:

📌 Total Customers

📌 Customer Churn Rate

📌 Average Customer Age

📌 Average Account Balance

📌 Active Customer Ratio

<h2>🧭 Dashboard Modules</h2>

The dashboard is organized into four core analytical modules:

<h5>1️⃣ Customer Overview</h5>

Provides a high-level summary of the dataset, including customer counts, churn rate, and overall trends.

<h5>2️⃣ Demographic Analysis</h5>

Examines churn patterns based on:

👥 Gender

🌍 Geography

🎂 Age groups

<h5>3️⃣ Financial Behavior Analysis</h5>

Analyzes relationships between:

💰 Account balance

📉 Credit score

🏦 Number of banking products

<h5>4️⃣ Churn Segmentation Insights</h5>

Identifies high-risk customer groups and compares churn behavior across different segments.

<h2>🔎 Drill-Down Analytics</h2>

The dashboard includes interactive filters that allow deeper exploration of the data.

Users can drill down by:

✔ Geography

✔ Gender

✔ Age groups

✔ Credit score range

✔ Customer activity status

This makes the dashboard useful for segment-level decision making.

<h2>🛠️ Technologies Used</h2>

This project was built using the following technologies:

🐍 Python

📊 Pandas

🔢 NumPy

📈 Matplotlib

📉 Seaborn

🌐 Streamlit

🤖 Scikit-learn

📓 Jupyter Notebook

<h2>💡 Key Insights</h2>

The analysis revealed several important findings:

📉 The overall churn rate is approximately 20%

🌍 Germany shows the highest churn rate

⚠ Inactive customers are significantly more likely to churn

👥 Customers aged 30–45 have higher churn probability

📊 Customers with lower credit scores show higher attrition risk

<h2>*🚀 Business Recommendations*</h2>

Based on the insights obtained, the following strategies are recommended:

✔ Implement early churn detection systems

✔ Improve customer engagement programs

✔ Introduce personalized offers for high-risk customers

✔ Strengthen customer loyalty programs

✔ Encourage digital banking adoption

<h2>🔮 Future Improvements</h2>

Possible future enhancements include:

🚀 Machine learning models for churn prediction

📊 Advanced customer segmentation techniques

☁ Deployment on cloud platforms

📡 Real-time analytics dashboards

<h2>▶️ Run the Project</h2>

To run the Streamlit dashboard locally:

streamlit run app.py
🌐 Streamlit Dashboard

<h2>🔗 Live Dashboard:</h2>
(http://localhost:8501/)

-----
<h6>[Created by: Poorvi Malvi]</h6>
