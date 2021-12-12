#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st
import numpy as np
from math import pi
st.title("Hello!")
st.header("Let me calculate the volume of a sphere for you!")


# In[5]:


number_input = st.number_input("Please input your r (radius) value")


# In[9]:


volume = (4/3)*pi*number_input**3


# In[19]:


st.write("Volume of your sphere:",{volume})


# In[18]:


st.image("rumus_volume_bola.jpg")

