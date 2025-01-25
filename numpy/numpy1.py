#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


a = np.array([1,2,3,4])
print(a)


# In[4]:


print(type(a))


# In[5]:


print(a.shape)


# In[8]:


b = np.array([[1,2,3,4], [5,6,7,8]])
print(b)


# In[7]:


print(b.shape)


# In[9]:


b.T


# In[10]:


np.dot(b,b.T)


# In[12]:


np.random.randint(60,100,10)


# In[17]:


matrix = np.random.randint(60,100,(5,5))


# In[18]:


print(matrix)


# In[19]:


#find max element from numpy array
np.max(matrix)


# In[20]:


#minimum element
np.min(matrix)


# In[21]:


a = np.array([0,1,24,3,4,8,4])


# In[22]:


np.argmin(a)


# In[23]:


np.argmax(a)


# In[24]:


np.unique(a)


# In[25]:


print(np.unique(a, return_counts = True))


# In[31]:


b = np.array([22,4524,42,42,42,23, 34, 87,98,56,67,45,345])


# In[32]:


print(b[0])
print(b[-1])


# In[28]:


#program to find the number with highest frequency in the given array


# In[33]:


b= np.unique(b,return_counts=True)


# In[34]:


print(b)


# In[37]:


print(b[0][np.argmax(b[1])])


# In[39]:


#slicing arrays
matrix


# In[40]:


matrix[2:4, 1: 3]


# In[41]:


matrix[0][0]


# In[ ]:



