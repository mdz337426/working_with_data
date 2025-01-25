#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


df = pd.read_csv('netflix_titles.csv')


# In[8]:


print(df)


# In[15]:


print(df['show_id'])


# In[16]:


df.head()


# In[18]:


df.shape


# In[19]:


df.columns


# In[21]:


df.describe()


# In[22]:


df.tail 


# In[23]:


df.iloc[3]


# In[24]:


df.iloc[3,1]


# In[25]:


df.iloc[3][1]


# In[26]:


idx = df.columns.get_loc('director')
df.iloc[0, idx]


# In[27]:


df.iloc[3, idx]


# In[32]:


df.iloc[:,0:-3]


# In[34]:


#sorting dataframes

df.sort_values(by =['release_year'], ascending=True)


# In[35]:


data_array = df.values


# In[36]:


print(data_array)


# In[37]:


print(type(data_array))


# In[38]:


df


# In[42]:


filtered_data = df[df['release_year']>= 2020]


# In[43]:


filtered_data


# In[44]:


#grouping 

grouped_data = df.groupby('type')


# In[45]:


grouped_data


# In[47]:


grouped_data.get_group('Movie')


# In[62]:


import numpy as np
#append data into the end
df.shape

df['price'] = np.random.randint(1000,2000,df.shape[0])


# In[63]:


df['price']


# In[67]:


#Aggregation
total_price = df.groupby('type')['price'].sum()


# In[68]:


total_price


# In[70]:


aggregate_price = df.groupby('type')['price'].agg(['sum', 'mean'])
aggregate_price


# In[71]:


#combining fiktering grouping and aggregation
result = df[df['release_year'] >= 2020].groupby('type')['price'].sum()
result


# In[ ]:




