#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[19]:


data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [50, 130, 140, 160, 100]}


# In[20]:


df = pd.DataFrame(data)


# In[25]:


plt.figure(figsize=(10, 6))
df.plot(kind='bar', x='Month', y='Sales', figsize=(11,6), title='Sales by Month',color='Green')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.show()


# In[22]:


df.plot(kind='line', x='Month', y='Sales', figsize=(11,6), title='Sales by Month',color='Green')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.show()

