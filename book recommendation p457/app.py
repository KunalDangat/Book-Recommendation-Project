#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[2]:


st.title('Book Recommendation System')  ## adding title


# In[3]:


## loading the files
df_new=pickle.load(open('df_new.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
similarity_scores=pickle.load(open('similarity_scores.pkl','rb'))


# In[4]:


## defining the function
def recommend(book_name):
    # fetch the index of the book from the pivot table
    index=np.where(df_new.index==book_name)[0][0]
    # getting similar suggestions with greater similarity score,
    similar_items=sorted(list(enumerate(similarity_scores[index])), # enumerate to get the distance with index
                         key=lambda x:x[1],  # key=lambda x:x[1] is used to sort the list of based on the similarity score, not on the basis of index
                         reverse=True)[1:6]  # 1:6 will get the books excluding that book as the similarity score of a book with itself is highest
    
    data=[]
    for i in similar_items:
        item=[]
        temp_df=df[df['Book']==df_new.index[i[0]]] # df_new.index[i[0]]] to get the index of the books
        item.extend(list(temp_df.drop_duplicates('Book')['Book'].values))
        item.extend(list(temp_df.drop_duplicates('Book')['Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book')['Genre'].values))
        item.extend(list(temp_df.drop_duplicates('Book')['Award Name'].values))
                            
        data.append(item)
    return pd.DataFrame(data,columns=['Book','Author','Genre','Award Name'])


# In[5]:


book_list=df_new.index.values


# In[6]:


selected_book=st.selectbox('Type or select a book from the dropdown',book_list)


# In[7]:


if st.button('Show Recommendation'):
    recommended_books=recommend(selected_book)
    recommended_books


# In[8]:


st.header("Top 10 popular books based on ratings")


# In[9]:


df1_new1=pickle.load(open('df1_new1.pkl','rb'))


# In[10]:


st.dataframe(df1_new1)


# In[11]:


st.header("Top 10 books offering maximum discount")


# In[12]:


df2_new1=pickle.load(open('df2_new1.pkl','rb'))


# In[13]:


st.dataframe(df2_new1)


# In[14]:


st.header("Top 10 books at least price")


# In[15]:


df3_new1=pickle.load(open('df3_new1.pkl','rb'))


# In[16]:


st.dataframe(df3_new1)


# In[17]:


st.header("Top 10 books by maximum checkouts")


# In[18]:


df4_new1=pickle.load(open('df4_new1.pkl','rb'))


# In[19]:


st.dataframe(df4_new1)


# In[ ]:




