#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
dataset=pd.read_csv('iris.csv')
dataset


# In[3]:


import pandas as pd
dataset=pd.read_csv('iris.csv')
dataset


# In[4]:


dataset.shape


# In[5]:


dataset.head


# In[6]:


dataset.head(10)


# In[7]:


dataset.tail()


# In[8]:


dataset.tail(10)


# In[11]:


dataset.columns


# In[12]:


dataset['variety']


# In[13]:


dataset.dtypes


# In[14]:


dataset.describe()


# In[15]:


dataset.iloc[:,:]


# In[16]:


dataset.iloc[0:20,:]


# In[17]:


dataset.iloc[0:20,1:3]


# In[18]:


dataset[dataset['sepal.length']>7]


# In[19]:


dataset[(dataset['sepal.length']>7)&(dataset['petal.width']==2.1)]


# In[20]:


dataset.isna().sum()


# In[23]:


dataset['variety'].value_counts()

