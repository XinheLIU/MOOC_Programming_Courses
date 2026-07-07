
# coding: utf-8

# In[2]:


import pandas as pd


# In[27]:


# 1. Read data
# As the only useful data is ['user id','gender'] in u.user 
# and ['user id','rating'] in u.data, 
# first split these columns
data_df=pd.DataFrame([]) 
# pass in column names for each CSV
u_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_csv('./ml-100k/u.user', sep='|', names=u_cols,
                    encoding='latin-1')
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('./ml-100k/u.useru.data', sep='\t', names=r_cols,
                      encoding='latin-1')


# In[32]:


d = pd.merge(users, ratings)
pdf = pd.pivot_table(d, values=["rating"], index=["user_id","gender"])


# In[33]:


pdf.groupby("gender").std()

