# kaggle-telco-churn
The Telco customer churn data contains information about a fictional telco company that provided home phone and Internet services to 7043 customers in California in Q3 provided by IBM. This is my Kaggle notebook and learning notes from this small project.

Reminder: update src/path.py

**Objectives**: The primary objective is to predict whether a customer will churn or not. This is given by Churn label. In our classification model we may also want to add a higher cost to customers with a higher Customer Lifetime Value (CLTV). A secondary objective would be understanding why customers churn, especially high value customers, so we can prevent against it. 3) Understand the potential loss/gains to be made in not preventing/avoiding customer churn. Summarise these findings in a presentation. 

**Business Impacts and Insights**
1. Identify customers who will churn and prevent them from doing so.
2. In order to prevent them from doing so, we need to understand the most common reason for them churning, and implement a stratergy to avoid it. A secondary ML model or non-ML approach could be applied down the line, to decide how to address each churning customer. 

**Additional Considerations**: 
1. As mentioned, customers with higher CLTV, a more costly to lose. Ideally, we want a final model which should account for this within the cost functions.

**KPI Used**
The aim of this is to model is to prevent churn with the ultimate goal of improving the business's profit. As such when assessing the performance of the model on the test set we want a metric which incooperates both our correct churn or not churn prediction and the CLTV. Comparing models based off
$$
CLTV retained = \sum Predicted churn \times CLTV,
$$
If the model correctly identifies a customer about to churn, then we assign predicted churn = 1, else 0. This KPI optimises the model which retains the most CLTV. 

**Metric used**
Select a model metric which aligns with this KPI. Depending on the cost of the intervention, the cost of incorrectly predicting no churn when a customer is about to churn may be more costly, than predicting churn when a customer will not churn. If we assume 