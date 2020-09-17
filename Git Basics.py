#!/usr/bin/env python
# coding: utf-8

# ## Jupyter Notebook Exercise

# In[1]:


import pandas as pd


# In[2]:


grab = pd.read_csv("DataSeerGrabPrizeData.csv")


# In[3]:


grab.describe()


# In[4]:


grab_cleaned = grab.dropna()


# In[5]:


grab_cleaned.describe()


# In[6]:


grab_cleaned.to_csv("DataSeerGrabCleaned.csv")


# In[ ]:




