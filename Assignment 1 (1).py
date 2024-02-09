#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to the CSV file
file_path = "/Users/ccirilloadmin/Downloads/ACSST1Y2022.S2701-2024-02-06T170536.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Define the relevant demographic groups
desired_demographics = [
    "Civilian noninstitutionalized population",
    "        White alone",
    "        Black or African American alone",
    "        Asian alone",
    "        Native Hawaiian and Other Pacific Islander alone",
    "        Some other race alone",
    "        Hispanic or Latino (of any race)",
    "        Two or more races"
]

# Filter the DataFrame to include only the desired demographic groups
df_filtered = df[df['Label (Grouping)'].isin(desired_demographics)]


# In[136]:


df_filtered = df[df['Label (Grouping)'].isin(desired_demographics)]

# Sort the DataFrame by the percentage uninsured in ascending order
df_filtered = df_filtered.sort_values(by='District of Columbia!!Percent Uninsured!!Estimate', ascending=True)

# Set up the figure and axis with a larger size
plt.figure(figsize=(15, 10), facecolor='lavenderblush')

# Plot the bar chart for percentage uninsured by demographic group
plt.barh(df_filtered['Label (Grouping)'], df_filtered['District of Columbia!!Percent Uninsured!!Estimate'], color='palevioletred')
plt.xlabel('Percentage Uninsured')
plt.ylabel('Demographic Group')

# Remove the empty title
plt.title('Percentage of Uninsured Population by Demographic Group in D.C.')

plt.ylim(0, len(df_filtered))
# Show the plot
plt.show()


# In[135]:


# Define the relevant age groups
desired_age_groups = [
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0Under 6 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa06 to 18 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa019 to 25 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa026 to 34 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa035 to 44 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa045 to 54 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa055 to 64 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa065 to 74 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa075 years and older', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0Under 19 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa019 to 64 years', 
    '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa065 years and older'
]

# Filter to include only the desired age groups
df_age_filtered = df[df['Label (Grouping)'].isin(desired_age_groups)]

# Sort by the percentage uninsured in descending order
df_age_filtered = df_age_filtered.sort_values(by='District of Columbia!!Percent Uninsured!!Estimate', ascending=True)

# Set up the figure and add a background color
plt.figure(figsize=(15, 10), facecolor='antiquewhite')

# Plot the bar chart for percentage uninsured by age group
plt.barh(df_age_filtered['Label (Grouping)'], df_age_filtered['District of Columbia!!Percent Uninsured!!Estimate'], color='indianred')
plt.xlabel('Percentage Uninsured')
plt.ylabel('Age Group')

# Remove the empty title
plt.title('Percentage of Uninsured Population by Age Group in D.C.')

plt.ylim(0, len(df_age_filtered))
# Show the plot
plt.show()

