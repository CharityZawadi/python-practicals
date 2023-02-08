#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns 


# In[2]:


data = pd.read_csv(r'C:\Users\Zawadi\Desktop\EDA\Insurance.csv')


# In[3]:


data.head()


# In[4]:


data.describe()


# In[5]:


data.tail()


# In[6]:


data.shape


# In[7]:


data.columns


# In[8]:


data.nunique()


# In[9]:


data['sex'].unique()


# In[11]:


data['bmi'].unique()


# In[12]:


data.isnull().sum()


# In[13]:


client=data.drop(['children'],axis=1)


# In[14]:


client.head()


# In[15]:


corelation=client.corr()


# In[18]:


sns.heatmap(corelation,xticklabels=corelation.columns,yticklabels=corelation.columns,annot=True)


# In[19]:


sns.pairplot(client)


# In[21]:


sns.relplot(x='age',y='charges',hue='smoker', data=client)


# In[22]:


sns.displot(client['bmi'])


# In[23]:


sns.catplot(x='region',y='charges',data=client)


# In[24]:


sns.catplot(x='charges',kind='box',data=client)


# In[ ]:




