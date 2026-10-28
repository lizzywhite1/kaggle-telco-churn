# kaggle-telco-churn
The Telco customer churn data contains information about a fictional telco company that provided home phone and Internet services to 7043 customers in California in Q3 provided by IBM. This is my Kaggle notebook and learning notes from this small project.

Reminder: update src/path.py

**Objectives**: The primary objective is to predict whether a customer will churn or not. This is given by Churn label. In our classification model we may also want to add a higher cost to customers with a higher Customer Lifetime Value (CLTV). A secondary objective would be understanding why customers churn, especially high value customers, so we can prevent against it. 3) Understand the potential loss/gains to be made in not preventing/avoiding customer churn. Summarise these findings in a presentation. 

**Business Impacts and Insights**
1. Identify customers who will churn and prevent them from doing so.
2. In order to prevent them from doing so, we need to understand the most common reason for them churning, and implement a stratergy to avoid it. A secondary ML model or non-ML approach could be applied down the line, to decide how to address each churning customer. 

**Additional Considerations**: 
1. CLTV, satisfaction score, churn reason and category are not used as inputs into our model as these are likely to be variables that leak in the churn label to the data. In real life, satisfaction scores usually aren't known. 

**KPI Used**
The aim of this is to model is to prevent churn with the ultimate goal of improving the business's profit. As such when assessing the performance of the model on the test set we want a metric which incooperates both our correct churn or not churn prediction and the CLTV. Comparing models based off
$$
CLTV retained = \sum Predicted churn \times CLTV,
$$
If the model correctly identifies a customer about to churn, then we assign predicted churn = 1, else 0. This KPI optimises the model which retains the most CLTV. 

**Exploratory Data Analysis Findings**
- The most recent offer, Offer E, seems to be linked to churn, it is likely also linked to the fact most Offer E customers are new and on month to month contract. This is despite Offer E having lowest median monthly charge.
- Internet / Internet + Phone Service seems to drive up churn rate, Fibre Optic internet seems to drive churn.
- Having premium tech support and online backup lowers churn rate. 
- Approx 26% customers churned this quarter, total monthly charges for these customers $139,130.85. 
- Higher median monthly charge for churners. 
- Churn largely due to better devices and offer. For phone only users (less likely to churn), churned due to customer support issues. 

**Feature Engineering**
- 

**Metric used**
Select a model metric which aligns with this KPI. Depending on the cost of the intervention, the cost of incorrectly predicting no churn when a customer is about to churn may be more costly, than predicting churn when a customer will not churn. If we assume 