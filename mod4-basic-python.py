#!/usr/bin/env python
# coding: utf-8

# In[17]:


import math
from math import floor
def savings(gross_pay: int, tax_rate: float, expenses: int):
    take_home_pay=(gross_pay - round(gross_pay*tax_rate) - expenses)
    return(floor(take_home_pay))

def material_waste(total_material: int, material_units: str, num_jobs: int, job_consumption: int):
    waste=(total_material-(num_jobs*job_consumption))
    return(str(waste)+material_units)

def interest(principal, rate, periods):
    final_interest=(principal+(1+rate*periods))
    return(floor(final_interest))

def bmi(height:list,weight:int):
    height1 = height[0] * 0.3048
    height2 = height[1] * 0.0254
    final_height = height1 + height2
    weight1 = weight * 0.453592
    final_bmi = weight1/(final_height ** 2)
    return(round(final_bmi,2))


# In[18]:


bmi([5,10],50)


# In[5]:


1000,0.1,100


# In[6]:


1000,0.1,100


# In[12]:


1000,0.1,100


# In[13]:


savings(1000,0.1,100)


# In[15]:


savings(1000,0.1,100)


# In[16]:


1000,0.1,100


# In[17]:


savings(1000,0.1,100)


# In[18]:


savings(1000,0.1,100)


# In[19]:


savings(1000,0.1,100)


# In[21]:


savings(1000,0.1,100)


# In[22]:


savings(1000,0.1,100)


# In[24]:


savings(1000,0.1,100)


# In[25]:


material_waste(100,10,20)


# In[26]:


material_waste(100,10,20)


# In[27]:


material_waste(100,10,20)


# In[28]:


material_waste(100,10,20)


# In[29]:


material_waste(100,10,20)


# In[30]:


material_waste(100,10,20)


# In[31]:


interest(1000,2.5,4)


# In[32]:


material_waste(100,10,20)


# In[1]:


material_waste(100,10,20)


# In[2]:


material_waste(10,"hello",5,4)


# In[3]:


material_waste(10,"hello",5,4)


# In[11]:


material_waste(10,"hello",5,4)


# In[12]:


material_waste(10,"hello",5,4)


# In[13]:


material_waste(10,"hello",5,4)


# In[ ]:




