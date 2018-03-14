
# coding: utf-8

# In[47]:


import pandas as pd

data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")
data.head(5)


# In[48]:


data["Do you celebrate Thanksgiving?"].value_counts()


# In[49]:


data = data[data["Do you celebrate Thanksgiving?"] == "Yes"]


# In[50]:


data


# In[51]:


data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[52]:


data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]["Do you typically have gravy?"]


# In[62]:


data["Do you typically have gravy?"].head(5)


# In[60]:


apple_isnull=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
pumpkin_isnull=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
pecan_isnull=pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])



# In[68]:


apple_isnull.head(6)


# In[66]:


pumpkin_isnull.head(6)


# In[67]:


pecan_isnull.head(6)


# In[58]:


ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull

ate_pies.value_counts()


# In[69]:


ate_pies.head(6)


# In[74]:


data["Age"].value_counts()
data["Age"].head(10)


# In[75]:


def extract_age(age_str):
    if pd.isnull(age_str):
        return None
    age_str = age_str.split(" ")[0]
    age_str = age_str.replace("+", "")
    return int(age_str)

data["int_age"] = data["Age"].apply(extract_age)
data["int_age"].head(10)


# Although we only have a rough approximation of age, and it skews downward because we took the first value in each string (the lower bound), we can see that that age groups of respondents are fairly evenly distributed.

# In[76]:


data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts()


# In[79]:


data["How much total combined money did all members of your HOUSEHOLD earn last year?"].head(10)


# In[77]:


def extract_income(income_str):
    if pd.isnull(income_str):
        return None
    income_str = income_str.split(" ")[0]
    if income_str == "Prefer":
        return None
    income_str = income_str.replace(",", "")
    income_str = income_str.replace("$", "")
    return int(income_str)

data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(extract_income)


# In[78]:


data["int_income"].head(10)


# Although we only have a rough approximation of income, and it skews downward because we took the first value in each string (the lower bound), the average income seems to be fairly high, although there is also a large standard deviation.

# In[80]:


data[data["int_income"] < 150000]["How far will you travel for Thanksgiving?"].value_counts()


# In[81]:


data[data["int_income"] > 150000]["How far will you travel for Thanksgiving?"].value_counts()


# It appears that more people with high income have Thanksgiving at home than people with low income. This may be because younger students, who don't have a high income, tend to go home, whereas parents, who have higher incomes, don't.

# In[83]:


data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",
    values="int_age")


# In[86]:


data.pivot_table(index='Have you ever attended a "Friendsgiving?"',
    values="int_age")


# In[89]:


data.pivot_table(
    columns="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    index='Have you ever attended a "Friendsgiving?"',
    values="int_income"
)


# 
# Findings
# It appears that people who are younger are more likely to attend a Friendsgiving, and try to meet up with friends on Thanksgiving.
# 

# In[90]:


data["How is the main dish typically cooked?"].value_counts()


# In[99]:


data[data["How is the main dish typically cooked?"] == "Baked"]["What kind of stuffing/dressing do you typically have?"]


# In[100]:


data["Will you employer make you work on Black Friday?"].value_counts()


# In[110]:


data[data["Will you employer make you work on Black Friday?"] == "Yes"]["What is your gender?"].value_counts()


# More Females work on Black Friday than Men
