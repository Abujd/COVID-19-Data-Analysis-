#!/usr/bin/env python
# coding: utf-8

# # Covid 19 Data Analysis using Python

# Import Modules

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
print('Module Sucessfully imported')


# # Task 2
# 

# 2.1 Import Covid 19 dataset

# In[8]:


corona_dataset_csv = pd.read_csv("Dataset/covid19_Confirmed_dataset.csv")


# In[9]:


corona_dataset_csv.head()


# Cheak the shape

# In[11]:


corona_dataset_csv.shape


# 2.2 Delete Useless Column

# In[18]:


corona_dataset_csv.drop(["Lat","Long"],axis = 1,inplace = True)


# In[23]:


corona_dataset_csv.head(10)


# 2.3 Aggragation 

# In[21]:


corona_dataset_aggragated = corona_dataset_csv.groupby("Country/Region").sum()


# In[22]:


corona_dataset_aggragated.head()


# In[24]:


corona_dataset_aggragated.shape


# 2.4 Visualizing data for specific country

# In[27]:


corona_dataset_aggragated.loc["Angola"].plot()


# In[31]:


corona_dataset_aggragated.loc["Spain"].plot()
corona_dataset_aggragated.loc["China"].plot()
corona_dataset_aggragated.loc["Italy"].plot()


# In[32]:


corona_dataset_aggragated.loc["Spain"].plot()
corona_dataset_aggragated.loc["China"].plot()
corona_dataset_aggragated.loc["Italy"].plot()
plt.legend()


# # 3 Finding good measure

# Representing in the form of numbers

# 3.1 Calculating and Plotting frist derivating of curve

# In[36]:


corona_dataset_aggragated.loc["China"].diff().plot()


# 3.2 Find Maximum infection rate for China.Italy,Spane

# In[40]:


corona_dataset_aggragated.loc["China"].diff().max()


# In[39]:


corona_dataset_aggragated.loc["Italy"].diff().max()


# In[42]:


corona_dataset_aggragated.loc["Spain"].diff().max()


# 3.3 Find maximum infection rate for all of the countries

# In[52]:


countries = list(corona_dataset_aggragated.index)
max_infection_rates = []
for c in countries:
    max_infection_rates.append(corona_dataset_aggragated.loc[c].diff().max())
max_infection_rates


# # 3.4 Add Maximum_column_rate to our dataset
# 

# In[53]:


corona_dataset_aggragated["Max_infection_rate"] = max_infection_rates


# In[54]:


corona_dataset_aggragated.head()


# Delete some column

# In[55]:


corona_data = pd.DataFrame(corona_dataset_aggragated["Max_infection_rate"])


# In[56]:


corona_data.head()


# # Task 4 Importing And preparing worls happiness report dataset

# 4.1 Import dataset

# In[59]:


happiness_report_csv = pd.read_csv("Dataset/worldwide_happiness_report.csv")


# In[61]:


happiness_report_csv.head()


# # 4.2 Let's drop useless column from dataset

# In[103]:


useless_cols=["Overall Rank","Score","Generosity","Perceptions of corruption"]


# In[93]:


happiness_report_csv(useless_cols,axis=1,inplace=True)


# In[111]:


happiness_report_csv.head()


# # 4.3 Changing indices of dataframe

# make index to Country or region column using set_index method

# In[114]:


happiness_report_csv.set_index("Country or region",inplace = True)


# In[116]:


happiness_report_csv.head()


# # 4.4 Join both datasets

# corona dataset

# In[118]:


corona_data.head()


# In[119]:


corona_data.shape


# In[120]:


happiness_report_csv.head()


# In[121]:


happiness_report_csv.shape


# In[123]:


data = corona_data.join(happiness_report_csv,how="inner")


# In[124]:


data.head()


# In[125]:


data.shape


# # 4.5 Correlation Matrix

# In[126]:


data.corr()


# # Task 5 Visualization

# 5.1 ploting GDP vs Max_infection_rate
# 

# In[127]:


x = data["GDP per capita"]
y = data["Max_infection_rate"]
sns.scatterplot(x,y)


# In[129]:


sns.scatterplot(x,np.log(y))


# # The Country have more GDP have more infection rate

# In[130]:


data.head()


# 5.2 Social Supoort Vs Max Rate Infection
# 

# In[133]:


x = data["Social support"]
y = data["Max_infection_rate"]
sns.scatterplot(x,np.log(y))


# 5.3 Health life Expetancy vs max_rate_infection

# In[135]:


x = data["Healthy life expectancy"]
y = data["Max_infection_rate"]
sns.scatterplot(x,np.log(y))


# # Conclusion 

# # The Country is more Developed The Infection rate also high
# due to large no. of test

# In[ ]:





# In[ ]:




