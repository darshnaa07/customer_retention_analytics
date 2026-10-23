# CUSTOMER CHURN & RETENTION ANALYSIS 
## PROJECT OVERVIEW
Customer curn occurs when customers stop using a company's products or services. Understanding churn helps bussiness identify customer retention challenges and make better decisions.
This project analyzes a telecommunications customer dataset using Python to calculate churn rates, explore customer behaviour , and identify pattern associated with customer churn.

## OBJECTIVES
-Calculate the overall customer churn and retention rates.
-Analyze churn across different contract types.
-Investigate churn pattern based on customer tenure.
-Compare churn rate across payment methods.
-Explore the relationship between monthly charges and churn.
-Create visualizations and summarize bussiness findings.

## TOOLS AND TECHNOLOGIES
-Python
-Pandas
-Matplotlib
-Seaborn
-VS code
-Github

## DATASET
The project uses the telco Customer Churn Dataset, which contains customer information such as:
-Customer tenure
-Contract type
-Payment Method
-Monthly Charges
-Internet and phone services
-Customer churn status

The datset is used for educational and analytical purposes.

## ANALYSIS PERFORMED 
1. Data quality checks
- Identified missing value
- Checked for duplicate records
- Reviewed column data types

2. Overall Churn analysis
- Calculated the number of customers who left
- Calculated the number of customers who stayed
- Measured churn and retention rates

3. Contract analysis
Compared to churn rate across month to month,one year, and two year contract.

4. Tenure analysis
Grouped customer by tenure to compare churn patterns among newer and longer-term customers.

5. Payment method analysis
Compared to churn rate across different payment method.

6. Monthly charges analysis
Grouped customers by monthly charges and compared their churn rates.

## VISUALIZATIONS
The project generate four charts:
- churn_by_contract.png
- churn_by_tenure.png
- churn_by_payment_method.png
- churn_by_monthly_charge.png

then charts are saved in reports/ directory.

## BUSINESS RECOMENDATION
The analysis can help businesses:
- Investigate why customer leaves.
- Review retenion strategies for customer group with higher churn.
- Evaluate contract option and payment experiences.
- Monitor churn and retention rate.
These recommendation are starting points for further investigation. Observe patterns do not necessarily establish the cause of churn.
 
 ## HOW TO RUN THE PROJECT
 - Install python
 - on terminal: pip install -r requirement.txt
 - Add the dataset
 - Run the analysis: main.py
 
 ## SKILL DEMONSTRATED
 - Data loading and exploration
 - Data quality assessment 
 - Data manipulation with pandas
 - Grouping and aggregations
 - Percentage and churn-rate calculation
 - Data visualization
 - Business-oriented analytical thinking
 - Organizing python project into reusable functions

 ## CONCLUSION
 This project demonstrates how python can be used to explore customer churn, compare customer groups, visualise patterns. and communicate finding that may support customer retention decisions.
 