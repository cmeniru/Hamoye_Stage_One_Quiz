#!/usr/bin/env python
# coding: utf-8

# # Hamoye Stage One Quiz

# In[3]:


#import libraries
import numpy as np
import pandas as pd


# In[49]:


#Load the data 
data = pd.read_csv("C://Users//upsca//Downloads//FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding='latin1')
data.head(10)


# In[52]:


data.shape


# ### Question 1
# Which of these python data structures is unorderly?
# 
# Options
# - Set
# - Dictionary
# - List
# - Tuple
# 
# Answer: 
# #### Dictionary
# 
# Just like a dictionary, a set is also an unordered python data structure

# ### Question 2
# Perform a groupby operation on ‘Element’.  What year has the highest sum of Stock Variation?

# In[64]:


# Group the data by 'Element' and sum the numeric columns for each group
grouped_data = data.groupby('Element').sum()

# Access the 'Stock Variation' row and determine the year with the highest sum
max_stock_year = grouped_data.loc['Stock Variation', ['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']].idxmax()

# Print the year with the highest 'Stock Variation'
print(f"The year with the highest 'Stock Variation' is: {max_stock_year}")


# ### Question 3
# What is the mean and standard deviation across the whole dataset for the year 2017 to 2 decimal places?

# In[9]:


# Calculate mean and standard deviation for the year 2017
mean_2017 = data['Y2017'].mean()
std_dev_2017 = data['Y2017'].std()

# Print the mean and standard deviation rounded to two decimal places
print(f"Mean for 2017: {mean_2017:.2f}")
print(f"Standard Deviation for 2017: {std_dev_2017:.2f}")


# ### Question 4
# What is the total number and percentage of missing data in 2014 to 3 decimal places?

# In[12]:


# Calculate the total number of missing values in the year 2014 and the percentage of missing data
missing_value_2014 = data['Y2014'].isna().sum()
percentage_missing_2014 = (missing_value_2014 / len(data)) * 100

missing_value_2014, round(percentage_missing_2014, 3)


# ### Question 5
# What would be the output for?
# S = [['him', 'sell'], [90, 28, 43]]
# S[0][1][1]
# 

# In[14]:


S = [['him', 'sell'], [90, 28, 43]]
output = S[0][1][1]
print(output)


# ### Question 6
# How would you check for the number of rows and columns in a pandas DataFrame named df?
# 
# Options
# - df.shape
# - pd.length(df)
# - len(df)
# - df.shape( )
# 
# Answer: 
# #### df.shape

# ### Question 7
# Consider the following list of tuples:
# y = [(2, 4), (7, 8), (1, 5, 9)]
# How would you assign element 8 from the list to a variable x?
# 

# In[66]:


y = [(2, 4), (7, 8), (1, 5, 9)]
x = y[1][1]
print(x)


# ### Question 8
# What is the total number of unique countries in the dataset?

# In[16]:


# Calculate the number of unique countries
unique_countries_count = data['Area'].nunique()
unique_countries_count


# ### Question 9
# A pandas Dataframe with dimensions (100,3) has how many features and observations?
# 
# Options
# - 3 features, 100 observations
# - A pandas dataframe has no attribute feature or observation.
# - 100 rows and 3 observations.
# - 100 features, 3 observations.
# 
# Answer: 
# #### 100 rows and 3 observations

# ### Question 10
# What is the total sum of Wine produced in 2015 and 2018 respectively?

# In[18]:


# Perform a groupby operation on 'Item' and sum up the values for each year, then extract the sum for 'Wine' for 2015 and 2018
item_grouped = data.groupby('Item').sum()
wine_production_2015 = item_grouped.loc['Wine', 'Y2015']
wine_production_2018 = item_grouped.loc['Wine', 'Y2018']

wine_production_2015, wine_production_2018


# ### Question 11
# Which year had the least correlation with ‘Element Code’?

# In[27]:


correlations = data[['Element Code', 'Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']].corr()['Element Code']
least_correlation_year = correlations[1:].idxmin()  # Ignore the first entry as it is 'Element Code' with itself

correlations, least_correlation_year


# ### Question 12
# Perform a groupby operation on ‘Element’.  What is the total number of the sum of Processing in 2017?

# In[34]:


element_grouped = data.groupby('Element').sum()
processing_total_2017 = element_grouped.loc['Processing', 'Y2017'] 

print(processing_total_2017)


# ### Question 13
# Given the following python code, what would the output of the code give?
# 
# Options
# - Math Error
# - Value Error
# - Standard Error
# - Type Error
# 
# Answer:
# #### Type Error

# In[36]:


my_tuppy = (1,2,5,8)
my_tuppy[2] = 6


# ### Question 14
# Given the following numpy array 
# array  = 
# ([[94, 89, 63],
#              [93, 92, 48],
#              [92, 94, 56]])
# How would you select the elements in bold and italics from the array?
# 
# Options
# - array[ : 2, 1 : ] 
# - array[ 1 : , : ]
# - array[ : 1, 1 :] 
# - array[ : 1, 1 : ]
# - array[ : 2, 0 : ]
# 
# Answer: 
# #### array[ : 2, 1 : ]

# In[63]:


array = np.array([[94, 89, 63],
                  [93, 92, 48],
                  [92, 94, 56]])

selected_elements = array[ : 2, 1 : ]

selected_elements


# ### Question 15
# Which of the following dataframe methods can be used to access elements across rows and columns?
# 
# Options
# - df.iloc[ : ] 
# - df.iloc( )
# - df.loc( )
# - c and d
# - df.loc( : )
# 
# Answer:
# #### df.iloc[ : ]
# The answer given above is incorrect. Howerever, this was my submitted). The right answers would have been df.iloc() and df.loc() if they were represented with squared brackets (df.iloc[ ] and df.loc[ ]) instead of parentheses as using parentheses is incorrect in the context of accessing DataFrame elements.

# ### Question 16
# What is the total Protein supply quantity in Madagascar in 2015?

# In[40]:


# Filter data for Madagascar and the specific element for 2015
madagascar_protein = data[(data['Area'] == 'Madagascar') & (data['Element'] == 'Protein supply quantity (g/capita/day)')]
total_protein_2015 = madagascar_protein['Y2015'].sum()

# Round the total protein supply to 2 decimal places
total_protein_2015 = round(total_protein_2015, 2)

print("Total Protein Supply Quantity in Madagascar in 2015:", total_protein_2015)


# ### Question 17
# 
# Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the highest sum in 2017?
# 

# In[43]:


# Select only the 'Area' and 'Y2017' columns
selected_data = data[['Area', 'Y2017']]

# Group by 'Area' and sum up the values for 2017
groupby_area = selected_data.groupby('Area').sum()

# Find the area with the highest sum in 2017
highest_area = groupby_area['Y2017'].idxmax()
highest_sum = groupby_area['Y2017'].max()

print("Area with the highest sum in 2017:", highest_area)
print("Highest sum in 2017:", highest_sum)


# ### Question 18
# Select columns ‘Y2017’ and ‘Area’, Perform a groupby operation on ‘Area’.  Which of these Areas had the 7th lowest sum in 2017?

# In[45]:


# Select only the 'Area' and 'Y2017' columns
selected_data = data[['Area', 'Y2017']]

# Group by 'Area' and sum up the values for 2017
grouped_by_area = selected_data.groupby('Area').sum()

# Sort the results and find the 7th lowest sum
sorted_sums_2017 = grouped_by_area['Y2017'].sort_values()
seventh_lowest_area = sorted_sums_2017.index[6]  # Indexing starts at 0, so index 6 is the 7th element
seventh_lowest_sum = sorted_sums_2017.iloc[6]

print("The 7th lowest area in 2017 is:", seventh_lowest_area)
print("With a sum of:", seventh_lowest_sum)


# ### Question 19
# Which of the following is a python inbuilt module?
# 
# Options
# - Matplotlib
# - Math
# - Pandas
# - Seaborn
# 
# Answer:
# #### Math

# ### Question 20
# If you have the following list
# lst = [[35, 'Portugal', 94], [33, 'Argentina', 93], [30 , 'Brazil', 92]]
# col = [‘Age’,’Nationality’,’Overall’]
# How do you create a pandas DataFrame using this list, to look like the table below?
# 
# ![image.png](attachment:image.png)

# In[48]:


# Given list and columns
lst = [[35, 'Portugal', 94], [33, 'Argentina', 93], [30, 'Brazil', 92]]
col = ['Age', 'Nationality', 'Overall']

# Create a pandas DataFrame
df = pd.DataFrame(lst, columns=col, index=[1,2,3])
df

