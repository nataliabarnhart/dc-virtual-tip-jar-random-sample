#!/usr/bin/env python
# coding: utf-8

# In[177]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[178]:


# Import everything from the Google spreadsheet
url = 'https://docs.google.com/spreadsheets/d/1tz2uyhgy3MsBS68MHPzO8H455_879fqfIaRPyUUw3QE/htmlview?sle=true#gid=0'
response = requests.get(url)

# Find and parse the table
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all('table')


# In[179]:


# Convert the HTML table to a dataframe
df1 = pd.read_html(str(table), header=0, flavor='html5lib')[0]
# df1.head()


# In[180]:


# Clean up the dataframe
header = df1.iloc[2]
df2 = df1[4:]
df2.columns = header
df3 = df2.drop(columns=[3.0])
df4 = df3.dropna(axis='columns', how='all')
df4 = df4.reset_index(drop=True)
# df5 = df4.replace(np.nan, '', regex=True)
df4 = df4.rename_axis('#', axis='columns')
# df4.head()


# In[181]:


# Show a random sample of 5

df5 = df4.replace(np.nan, '', regex=True)
df5.sample(5)


# In[182]:


# Only sample people with a Venmo

df6 = df4.dropna(subset=['Venmo'])
df6 = df6.replace(np.nan, '', regex=True)
df6.sample(5)


# In[183]:


# Only sample people with a Paypal or Cash App

df7 = df4.dropna(subset=['Paypal or Cash App'])
df7 = df7.replace(np.nan, '', regex=True)
df7.sample(5)


# In[184]:


# Only sample people with no healthcare

df8 = df4.loc[df4['Do you have healthcare?'] == 'No']
df8 = df8.replace(np.nan, '', regex=True)
df8.sample(5)


# In[ ]:




