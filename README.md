# kaggle-telco-churn
The Telco customer churn data contains information about a fictional telco company that provided home phone and Internet services to 7043 customers in California in Q3 provided by IBM. This is my Kaggle notebook and learning notes from this small project.

Reminder: update src/path.py

**Objectives**: The primary objective is to predict whether a customer will churn or not. This is given by Churn label. In our classification model we may also want to add a higher cost to customers with a higher Customer Lifetime Value (CLTV). A secondary objective would be understanding why customers churn, especially high value customers, so we can prevent against it. 3) Understand the potential loss/gains to be made in not preventing/avoiding customer churn. Summarise these findings in a presentation. 

**Business Impacts**
1. Identify customers who will churn and prevent them from doing so.
2. In order to prevent them from doing so, we need to understand the most common reason for them churning, and implement a stratergy to avoid it. *Could we build a secondary model to predict churn reason, or should we implement a non-ML solution for predicting churn reason in high probability of churn customers?*. 
3. Assess the financial impact of preventing churn versus doing nothing. 

**Additional Considerations**: 
1. As mentioned, customers with higher CLTV, a more costly to lose. Ideally, final model should account for this within the cost functions.

**Metrics**
The following metrics were considered,

Ultimately, the _ was chosen as the final model metric 
