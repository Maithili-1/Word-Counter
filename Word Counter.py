#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Prompt the user to enter the Sentence or Paragraph
text=input("Enter the Sentence or Paragraph : ")

#Function to count the words in a given text
def word_count(text):
    return len(text.split())

# Count the number of words and print the result
if text:
    print(f"The text contains {word_count(text)} words.")
# Check for empty input
else:
    print("Error: Input cannot be empty.")


# In[ ]:




