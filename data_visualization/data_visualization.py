#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[9]:


x = np.arange(10)
y1 = x**2
y2 = 2*x+3

print(x)
print(y1)
print(y2)


# In[10]:


plt.plot(x, y1)


# In[12]:


themes = plt.style.available
themes


# In[13]:


plt.style.use('bmh')


# In[14]:


plt.plot(x, y1)


# In[25]:


plt.style.use('seaborn-v0_8')

plt.plot(x,y1, color='red', label="aeroplane", marker='o')
plt.plot(x,y2,color='green', label="car", linestyle='dashed')
plt.xlabel("time")
plt.ylabel("velocity")
plt.title("Acceleration")
plt.legend()
plt.show()


# In[29]:


prices = np.array([1,2,3,4])**3
plt.plot(prices)
plt.show()


# In[33]:


#scatter plot
plt.scatter(x,y1)
plt.show()


# In[38]:


plt.scatter(x,y1, marker = "^", color= "red")
plt.scatter(x,y2, color = "green")
plt.show()


# In[42]:


plt.bar([0,1,2,3,4,5],[10,20, 7 ,17, 3 ,2])
plt.bar([0,1,2,3,4,5],[10,25, 10 ,15, 5 ,10])
plt.show()


# In[44]:


xsn = np.random.randn(100)
sigma = 8
u = 70
X = np.round(xsn*sigma+u)
X


# In[50]:


plt.style.use("classic")
plt.hist(X)
plt.show()


# In[49]:


plt.style.available


# In[56]:


#data visualization of netflix titles dataset of frequency distribution of movies released in given year


import pandas as pd
df = pd.read_csv('netflix_titles.csv')
release_year =list(df.get('release_year'))


# In[66]:


freq_movies = {}

for year in release_year:
    if year in freq_movies:
        freq_movies[year] += 1
    else:
        freq_movies[year] =1   


# In[65]:


plt.scatter(list(freq_movies.keys()), list(freq_movies.values()))
plt.show()


# In[ ]:




