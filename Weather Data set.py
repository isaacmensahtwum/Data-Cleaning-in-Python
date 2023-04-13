#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[11]:


data = pd.read_csv(r"D:\DATA ANALYSIS\4. Data Analysis with Python\Weather Data.csv")


# In[12]:


data.head()


# In[14]:


#Total rows x columns
data.shape


# In[15]:


data.index


# In[19]:


# column names
data.columns


# In[20]:


# data types
data.dtypes


# In[30]:


#number of unique values for one variable
data["Weather"].unique()


# In[34]:


# Total observations in each variable
data.nunique() # or data["Weather"].nunique()


# In[35]:


data.count()


# In[40]:


# count of each unique value
data["Weather"].value_counts()


# In[45]:


data.info()


# ### Find all the unique "Wind Speed" values in the data

# In[49]:


data["Wind Speed_km/h"].unique()


# In[51]:


#counting the total number of unique values
data["Wind Speed_km/h"].nunique()


# ### Find the number of times when the weather is exactly clear

# In[66]:


# value_counts, filtering, groupby
# data.Weather.value_counts()
# data.Weather == 'Clear' ................. boolean form
data[data.Weather == 'Clear']


# In[65]:


# same as the above code
data.groupby('Weather').get_group('Clear')


# ### Find the number of times when the 'Wind Speed was exactly 4km/h'

# In[78]:


#data["Wind Speed_km/h"].value_counts()
data[data["Wind Speed_km/h"] == 4]


# ### Find out all the null values in the data set

# In[80]:


data.isnull().sum()


# In[81]:


data.notnull().sum()


# ### Rename Column

# In[84]:


data.rename(columns = {'Weather':'Weather Condition'}, inplace = True)


# In[85]:


data.head()


# ### What is the mean "Visibility"?

# In[95]:


data.Visibility_km.mean()


# ### What is the Stand. Dev. of this data "Pressure" in this data set

# In[98]:


data.Press_kPa.std()


# ### What is the variance of 'Relative Humidity' in this data?

# In[104]:


data["Rel Hum_%"].var()


# ### Find all insttances when "snow" was recorded

# In[118]:


#data[data["Weather Condition"]=="Snow"].................. filtering
#data["Weather Condition"].value_counts() #................. value counts
data[data["Weather Condition"].str.contains('Snow')]


# ### Find all instances when "Wind Speed is above 24" and "Visibility is 25"

# In[127]:


#data.head(2)
data[(data["Wind Speed_km/h"] >24) & (data["Visibility_km"] == 25)].head()


# ### What is the Mean value of each column against each Weather Condition?

# In[130]:


data.head(2)


# In[135]:


data.groupby('Weather Condition').mean()


# ### What is the Min and Max value of each column against each Weather Condition?

# In[145]:


data.groupby("Weather Condition").min()


# In[144]:


data.groupby("Weather Condition").max()


# ### Show all the records where weather condition is Fog

# In[149]:


data[data["Weather Condition"]=='Fog']
# data[data["Weather Condition"].str.contains('Fog')]


# ### Find all instances when Weather is clear or Visibility is above 40

# In[156]:


data[(data["Weather Condition"]== 'Clear') | (data.Visibility_km>40)]


# ### Find all instances when:
# #### A. Weather is clear and relative humidity is > 50
# #### B. Visibility is above 40

# In[165]:


data[(data["Weather Condition"]=='Clear') & (data["Rel Hum_%"]>50) | (data.Visibility_km>40)]


# In[ ]:





# In[ ]:




