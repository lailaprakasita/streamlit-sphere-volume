#!/usr/bin/env python
# coding: utf-8

# In[46]:


import streamlit as st
import numpy as np
from math import pi
st.title("Hello!")
st.header("Let me calculate volume of a sphere for you!")


# In[43]:


number_input = st.number_input("Please input r value")


# In[44]:


volume = (4/3)*pi*number_input**3


# In[55]:


st.write("Volume your sphere is :",{volume} )


# In[ ]:




