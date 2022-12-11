#!/usr/bin/env python
# coding: utf-8

# In[12]:


import math
from math import floor

def shift_letter(letter:str,shift:int):
    if letter==" ":
        return(" ")
    else:
        result=((ord(letter)-65) + (shift%26))%26+65
        return chr(result)

def caesar_cipher(message,shift):
    result = ""
    for i in range(len(message)):
        character = message[i]
        if character=='':
            result+=''
            continue
        result+=chr(((ord(character)-65+((shift%26)%26)+65))
    return(result)

def shift_by_letter(letter:str,letter_shift:str):
    if letter=="":
        return("")
    else:
        shift=ord(letter_shift.upper())-ord("A")
        result=((ord(letter.upper())-65) + (shift%26))%26+65
        return chr(result)

def vigenere_cipher:
    orig_text = []
    for i in range(len(message)):
        if message[i]=='':
            x=ord("")
        else:
            x=(ord(message[i])+ord(key[i%len(key)]))%26
            x+= ord ('A')
        orig_text.append(chr(x))

    return("".join(orig_text))


# In[ ]:





# In[29]:





# In[ ]:





# In[41]:





# In[ ]:





# In[ ]:




