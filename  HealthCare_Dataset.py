#!/usr/bin/env python
# coding: utf-8

# Data Analysis project:
# 
# Problem Statement :
# Our analysis includes several important aspects such as the classification of medical conditions by gender for suspected possible health gaps. Exploring how insurance companies relate to billing will help us understand how costs differ among various providers. The study also looks into patterns regarding the volume of different types of admissions and their related bills. In addition, we will analyze expenses in relation to patients’ ages and genders to discover patterns regarding the costs of healthcare. We also try to evaluate medical conditions by age to assess which conditions are prominent in certain age groups. In addition, we will analyze the proportion of patients by sex and the overall pattern of admissions. Important aspects of the examination include monitoring average costs of bills for different age cohorts and total expenses incurred per admission date to establish seasonal or temporal patterns of hospital expenditure. Through this research, many conclusions can be drawn which will assist healthcare providers alongside patient's insurers and policymakers to improve the quality of care given to patients at a lower cost.
# 

# # Opening of file in Python Environment and displaying some rows 

# In[1]:


import pandas as pd
healthcare_file_path = 'F:\healthcare_dataset.csv'
healthcare_df= pd.read_csv(r"F:\healthcare_dataset.csv",encoding='utf-8')
# Displaying   few rows.
healthcare_df.head()


# # Here is the classification of medical conditions by gender for suspected possible health gaps using Bar graph.

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

healthcare_df = pd.read_csv(healthcare_file_path, encoding="utf-8")
# giving style to sheet 
sns.set_style("whitegrid")
#------------------------------------------------------------------------------------------------------------------------------------------
# showing the Distribution of Medical Conditions by Gender.

plt.figure(figsize=(10,5))

sns.countplot(data=healthcare_df, x='Medical Condition', hue='Gender', palette="Set2")
plt.xticks(rotation=45)
plt.title("Distribution of Medical Conditions by Gender")
plt.xlabel("Medical Condition")
plt.ylabel("Count")
plt.legend(title="Gender")
plt.show()


# Count the number of male and female patients for each medical condition
gender_medical_condition_count = healthcare_df.groupby(["Medical Condition", "Gender"]).size().unstack()

# Display the result
print(f"Total number of male and female in different medical condition  {gender_medical_condition_count}")


# # This Analysis Help how insurance companies relate to billing Amount ,and we  understand how costs differ among various providers with the help of boxPlot.

# In[5]:


plt.figure(figsize=(10,5))
sns.boxplot(data=healthcare_df, x='Insurance Provider', y='Billing Amount', palette="muted")
plt.xticks(rotation=45)
plt.title("Billing Amount Across Different Insurance Providers")
plt.xlabel("Insurance Provider")
plt.ylabel("Billing Amount ($)")
plt.show()


# In[ ]:





# # The purpose of this visualization is to analyze key relationships in patient data by
# (1) comparing the average billing amount across different genders,
# (2) examining the average age of patients based on their medical conditions, and
# (3) evaluating the total billing amount associated with each type of admission,
# to uncover patterns that can aid in healthcare management and decision-making.
# 
# 

# In[20]:


fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Gender vs. Average Billing Amount (Bar Chart)
gender_avg_billing = df.groupby("Gender")["Billing Amount"].mean().sort_values()
sns.barplot(x=gender_avg_billing.index, y=gender_avg_billing.values, ax=axes[0, 0], palette="pastel")
axes[0,0].set_title("Average Billing Amount by Gender")
axes[0, 0].set_ylabel("Avg Billing Amount")

# 2. Medical Condition vs. Average Age (Bar Chart)
condition_avg_age = df.groupby("Medical Condition")["Age"].mean().sort_values()
sns.barplot(x=condition_avg_age.index, y=condition_avg_age.values, ax=axes[0, 1], palette="Set2")
axes[0, 1].set_title("Average Age by Medical Condition")
axes[0, 1].set_ylabel("Avg Age")
axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Admission Type vs. Total Billing Amount (Bar Chart)
admission_total_billing = df.groupby("Admission Type")["Billing Amount"].sum().sort_values()
sns.barplot(x=admission_total_billing.index, y=admission_total_billing.values, ax=axes[1, 0], palette="coolwarm")
axes[1, 0].set_title("Total Billing Amount by Admission Type")
axes[1, 0].set_ylabel("Total Billing Amount")
axes[1, 0].tick_params(axis='x', rotation=45)

 

# Adjust layout and display
plt.tight_layout()
plt.show()


# # The objective of this analysis is to visualize key patterns in patient billing and demographic data through
# (1) A comparison of average billing amount across different age groups,
# (2) A trend analysis of total billing amount over various admission dates,
# (3) A distribution chart of patients based on their admission type, and
# (4) a percentage breakdown of patients by gender, in order to derive meaningful insights that can support healthcare decision-making and resource planning.

# In[9]:


# Create subplots for line graphs and pie charts
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Line Graph: Age vs. Average Billing Amount
age_avg_billing = df.groupby("Age")["Billing Amount"].mean()
sns.lineplot(x=age_avg_billing.index, y=age_avg_billing.values, ax=axes[0, 0], color="b", marker="o")
axes[0, 0].set_title("Average Billing Amount by Age")
axes[0, 0].set_xlabel("Age")
axes[0, 0].set_ylabel("Avg Billing Amount")

# 2. Line Graph: Admission Date vs. Total Billing Amount
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])  # Ensure datetime format
date_billing = df.groupby("Date of Admission")["Billing Amount"].sum()
sns.lineplot(x=date_billing.index, y=date_billing.values, ax=axes[0, 1], color="r", marker="o")
axes[0, 1].set_title("Total Billing Amount Over Time")
axes[0, 1].set_xlabel("Admission Date")
axes[0, 1].set_ylabel("Total Billing Amount")

# 3. Pie Chart: Distribution of Admission Types
admission_counts = df["Admission Type"].value_counts()
axes[1, 0].pie(admission_counts, labels=admission_counts.index, autopct="%1.1f%%", colors=sns.color_palette("pastel"))
axes[1, 0].set_title("Distribution of Admission Types")

# 4. Pie Chart: Percentage of Patients by Gender
gender_counts = df["Gender"].value_counts()
axes[1, 1].pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", colors=sns.color_palette("coolwarm"))
axes[1, 1].set_title("Percentage of Patients by Gender")

# Adjust layout and display
plt.tight_layout()
plt.show()


# # In this Analysis it shows that the percentage of patient in different Medication.   

# In[10]:


plt.figure(figsize=(12, 10))
medication_counts = df["Medication"].value_counts()
plt.pie(medication_counts, labels=medication_counts.index, autopct="%1.1f%%", colors=sns.color_palette("pastel"))
plt.title("Distribution of Medications Prescribed")
plt.show()



# #  Here is the total profit gained by the hospital.

# In[11]:


total_profit = df["Billing Amount"].sum()
print(f"Total profit Gain by hospital is {total_profit}")


# # In this Analysis we calculate the yearwise and Monthly wise profit earned by the Hospital from 2019-2024 With the help of Line Chart.  

# In[18]:


# Replot graphs with formatted y-axis labels
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])#, errors="coerce")

# Extract Year and Month
df["Year"] = df["Date of Admission"].dt.year
df["Month"] = df["Date of Admission"].dt.to_period("M")

# Calculate total billing per year
yearly_profit = df.groupby("Year")["Billing Amount"].sum()

# Calculate total billing per month
monthly_profit = df.groupby("Month")["Billing Amount"].sum()
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Yearly profit trend
sns.lineplot(x=yearly_profit.index, y=yearly_profit.values, marker="o", ax=axes[0], color="b")
axes[0].set_title("Yearly Profit Trend")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Total Billing Amount (₹)")
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'₹{x/1e6:.1f}M'))  # Converting  to Millions

# Monthly profit trend
sns.lineplot(x=monthly_profit.index.astype(str), y=monthly_profit.values, marker="o", ax=axes[1], color="g")
axes[1].set_title("Monthly Profit Trend")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Total Billing Amount (₹)")
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'₹{x/1e6:.1f}M'))  # Converting  to Millions
plt.xticks(rotation=45)  

plt.tight_layout()
plt.show()


# # Our first Analysis help how many patients have different type of Blood group in Percentage.For this we use Pie Chart and then Our Second Analysis tells about the distribution of different type of medical condition of patients.

# In[17]:


fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Blood Type Pie Chart
df["Blood Type"].value_counts().plot.pie(autopct="%1.1f%%", cmap="viridis", ax=axes[0])
axes[0].set_title("Distribution of Blood Types")
axes[0].set_ylabel("")

# Medical Condition Pie Chart
df["Medical Condition"].value_counts().plot.pie(autopct="%1.1f%%", cmap="plasma", ax=axes[1])
axes[1].set_title("Distribution of Medical Conditions")
axes[1].set_ylabel("")

plt.tight_layout()
plt.show()


# In[ ]:




