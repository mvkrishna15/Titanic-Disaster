#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing liabries 
import numpy as np
import pandas as pd


# In[3]:


# get data
df= pd.read_csv( r"C:\titanicdata.csv")
df


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# Data Understanding
# PassengerId - Sr. No of passangers
# 
# Survived - Data of passengers if they are dead or alive
# 
# Pclass - Passenger class
# 
# Name - Name of passenger
# 
# Sex - Sex of passanger
# 
# Age - age of passanger on the ship
# 
# SibSp - Sibliings and spouse travelling along with a particular passanger
# 
# Parch - Parents or children travelling along with a particular passanger
# 
# Ticket - Ticket number of a passanger
# 
# Fare - Amount of money paid for the journey
# 
# Cabin - Cabin/room number whih was allocated during the journey
# 
# Embarked - Name of places from where passenger was onboarding

# In[ ]:





# In[6]:


# will give info of the data
df.info()


# In[7]:


print(df.describe())


# Cleaning data
# Keep Required columns
# Data type of each column
# Duplicate values
# Fill the missing values
# Checking wrong values

# In[8]:


df["family"]=df["SibSp"]+df["Parch"]


# In[9]:


# droping the unnecessary columns
df.drop(columns = ["SibSp","Parch","Ticket","Cabin"], axis=0,inplace=True)


# In[10]:


df.head()


# In[11]:


# checking null values 
df.isnull().sum()


# In[12]:


df["Embarked"].value_counts()


# In[13]:


df["Embarked"].unique()


# In[14]:


# handling the missing values by filter method


# In[15]:


df[df["Embarked"].isna()]


# In[16]:


df[(df["Survived"]==1)&(df["Pclass"]==1)&(df["Sex"]=="female")&(df["Age"]>60)]


# In[17]:


df.at[829,"Embarked"]="S"


# In[18]:


df.loc[829]


# In[19]:


df[(df["Survived"]==1)&(df["Pclass"]==1)&(df["Sex"]=="female")&(df["Age"]==38)]


# In[20]:


df.at[61,"Embarked"]="C"


# In[21]:


df.loc[61]


# In[22]:


df.isnull().sum()


# In[23]:


df[df["Age"].isna()]


# In[24]:


# pivot table it will summary of the data
pd.pivot_table(data=df,index="Sex",columns="Pclass",values="Age")


# In[ ]:


Filling the missing values .


# In[25]:


df[(df["Sex"]=="female")&(df["Pclass"]==1)&(df["Age"].isna())]


# In[26]:


f1=df[(df["Sex"]=="female")&(df["Pclass"]==1)&(df["Age"].isna())].index
f1


# In[27]:


for i in f1:
    df.at[i,"Age"]=34.611


# In[28]:


df.loc[166]


# In[29]:


f2=df[(df["Sex"]=="female")&(df["Pclass"]==2)&(df["Age"].isna())].index
f2


# In[30]:


for i in f2:
    df.at[i,"Age"]=28.72


# In[31]:


f3=df[(df["Sex"]=="female")&(df["Pclass"]==3)&(df["Age"].isna())].index
f3


# In[32]:


for i in f3:
    df.at[i,"Age"]=21.750


# In[33]:


f4=df[(df["Sex"]=="male")&(df["Pclass"]==1)&(df["Age"].isna())].index
f4


# In[34]:


for i in f4:
    df.at[i,"Age"]=41.28


# In[35]:


f5=df[(df["Sex"]=="male")&(df["Pclass"]==2)&(df["Age"].isna())].index
f5


# In[36]:


for i in f5:
    df.at[i,"Age"]=30.74


# In[37]:


f6=df[(df["Sex"]=="male")&(df["Pclass"]==3)&(df["Age"].isna())].index
f6


# In[38]:


for i in f6:
    df.at[i,"Age"]=26.50


# In[39]:


df["Age"].isnull().sum()


# In[40]:


df.isnull().sum()


# In[41]:


# clean the wrong data / outliner 
df["Survived"].unique()


# In[42]:


df["Age"].unique()


# In[43]:


df["Pclass"].unique()


# In[44]:


df["Sex"].unique()


# In[45]:


df.head()


# In[46]:


df["PassengerId"].unique()


# In[47]:


df["Name"].unique()


# In[48]:


df["Embarked"].unique()


# In[49]:


df["Fare"].unique()


# In[50]:


df["family"].unique()


# In[51]:


df["Fare"].max()


# There are 248 unique fare amounts for the same journey. This amount varies for various classes and genders. The range of fare paid by passangers is from 0 to 512$
# 
# But here paying 0 might not be the correct amount.Analyze and gather passengerswho paid b/w 0 to
#  -1$

# In[52]:


df["Fare"].min()


# In[53]:


df["Age"].max()


# In[54]:


df["Age"].min()


# In[55]:


df.columns


# In[56]:


df[df["Fare"]==0]


# 1) All the passangers whose fare is 0 did not survive the disaster.
# 2) All of them are male
# 3) All of them had embarked S
# 4) All were travelling alone
# 5) Analysing the average fare based on above criteria to fill these values

# In[57]:


pd.pivot_table(data=df,index="Survived",columns=["Pclass","Embarked"],values="Fare")


# In[ ]:


According to the given criteria we found the average fare for each class and it is as follows

1st class - 34.02
2nd class - 14.41
3rd class - 17.42
Now let us fill these values in dataset


# In[58]:


df[(df["Survived"]==0)&(df["Sex"]=="male")&(df["Embarked"]=="S")&(df["family"]==0)&(df["Pclass"]==1)&(df["Fare"]==0)]


# In[59]:


g1=df[(df["Survived"]==0)&(df["Sex"]=="male")&(df["Embarked"]=="S")&(df["family"]==0)&(df["Pclass"]==1)&(df["Fare"]==0)].index
g1


# In[60]:


for i in g1:
    df.at[i,"Fare"]=57.26


# In[61]:


g2=df[(df["Survived"]==0)&(df["Sex"]=="male")&(df["Embarked"]=="S")&(df["family"]==0)&(df["Pclass"]==2)&(df["Fare"]==0)].index
g2


# In[62]:


for i in g2:
    df.at[i,"Fare"]=18.94


# In[63]:


g3=df[(df["Survived"]==0)&(df["Sex"]=="male")&(df["Embarked"]=="S")&(df["family"]==0)&(df["Pclass"]==3)&(df["Fare"]==0)].index
g3


# In[64]:


for i in g3:
    df.at[i,"Fare"]=14.52


# In[65]:


df[df["Fare"]==0]


# In[66]:


df.at[271,"Fare"]=15.31


# In[67]:


df["Fare"].min()


# In[ ]:


# survival analysis of disaster
total ppl survived
ppl survived from each class
ppl suvived from each gender
histogram of age 
which age survived most
histogram for fare of survivors
passenger from which embarked survived the most
passenger from which family survived the most


# In[70]:


df[(df["Survived"]==1)&(df["Sex"]=="male")&(df["Pclass"]==1)]


# In[ ]:


# matplotlib - basic vis lib
# seaborn - advanced vis lib


# In[4]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[79]:


sns.barplot(df,x="Survived",y=df["Survived"].value_counts())
plt.show()


# 549 passengers which makes approx 61% of passangers did not survived the distater
# 
# where as 342 passangers survived the distater.

# There are only three unique values in Pclass column.
# 
# Where,
# 
# 1 - passangers who belong from 1st class
# 
# 2 - passangers who belong from 2nd class
# 
# 3 - passangers who belong from 3rd class

# In[81]:


df["Survived"].value_counts()


# conclusion 
# more than 500 ppl were dead where as less than 300 ppl has survied 
# which means x% ppl did nt survived the diaster and only y% ppl survived it 
# 
# 3 parts
# 1) about the data 
# 2) conclusion
# 3) final conclusion

# In[86]:


sns.countplot(df,x="Pclass",hue="Survived")
# hue =spearation / diiffertion citreia


# In[83]:


df["Pclass"].value_counts()


# In[87]:


sns.countplot(df,x="Survived",hue="Pclass")


# In[95]:


sns.countplot(df,x="family",hue="Survived")


# In[94]:


plt.pie(data=df,x=df["Sex"].value_counts(),labels=["male","female"],autopct="%0.2f%%")


# In[97]:


plt.hist(data=df,x="Age",bins=[0,10,20,30,40,50,60,70,80,90])


# In[112]:


plt.hist(data=df,x="Fare",histtype="bar",range=(df["Fare"].min(),df["Fare"].max()))


# In[104]:


df[df["Fare"]>300]


# In[106]:


pd.pivot_table(data=df,values="Fare",index=["Survived","Sex"] ,columns=["Pclass","Embarked"])


# In[111]:


df.at[258,"Fare"]=116.83
df.at[679,"Fare"]=112.19
df.at[737,"Fare"]=112.19


# In[113]:


df[df["Fare"]>200]


# In[114]:


df1=df[df["Survived"]==1]
df1.head()


# In[115]:


plt.hist(data=df1,x="Age",histtype="bar",range=(df1["Age"].min(),df1["Age"].max()))


# In[116]:


plt.hist(data=df1,x="Fare",histtype="bar",range=(df1["Fare"].min(),df1["Fare"].max()))


# In[118]:


# embarked wise survival 
sns.stripplot(df,x="Fare",y="Pclass",hue="Survived")


# Which gender has the max youth

# In[11]:


plt.figure(figsize=(10,3))
sns.violinplot(x ="Pclass", y = "Age", hue="Sex", orient="v", data =df )
plt.show()


# On an avereage every class and every genader wass having agerage age arounf the range of 25-35 From the box plot males had more avg age than female passangers irrespective of class
# 
# maximum travellers were male from 1st class and the range of theor age is from below 0years to 80+ years
# Where as the age range of females belonging from 1st class is from 1year to 70+ years
# Same observations were seen in other two classes

# Classifying fare for each gender

# In[10]:


sns.boxplot(x ="Fare", y = "Pclass", hue="Sex", orient="h", data =df )
plt.show()


# Females ffrom 1st class paid avg fare of 80$
# Males from 3rd class paid negligible fare
# on an avg females paid more fare for travelling

# In[119]:


sns.stripplot(df,x="Embarked",y="Pclass",hue="Survived")


# Classifying gender wise age for each survival

# In[7]:


sns.violinplot(x ="Sex", y = "Age", hue="Survived", orient="v", data =df )


# In[5]:


plt.figure(figsize=(10,3))
sns.violinplot(x ="Survived", y = "Age", hue="Pclass", orient="v", data =df )
plt.show()


# The range of age of passangers who belong from1st class and did not survived the disaster was wide form 0-80years
# The range of age of passangers who belong from 2nd class and did not survived the disaster was narrow form 10-70years
# The range of age of passangers who belong from 3rd class and did not survived the disaster was wide same like 1st class also it had wide spread along the axis.
# Same observations were observed for survived category of passangers.

# In[129]:


plt.figure(figsize=(5,5))
sns.pairplot(df,hue="Survived")


# 1. Conclusion of analysis based on passangers who survived the disaster: As we have analysed the dataset, there were 891 passangers on the ship.
# 
# 2. Out of all passangers 39% of passangers survived the disaster.
# 3. Out of which 28.37% belonged to 1st class the maximum survivours, due to class system 1st class passangers were given more prefrence than other classes.
# 4. As the analysis says 64% were Male passangers which is more than female passangers but due to prefrence of saving female passangers first 40.63% female passangers survived the disaster ie more female passangers were saved.
# 5. As per the class system 20.97% of female passsnagers were from first class , 17.11 % were from second class, and 17.51% were from third class
# 6. Average age of passangers was around 30 years and same was replicated for survived passangers
# 7. Passangers who paid more fare amount (ie 1st passangers) were saved in more amount as compared to others who paid less fare
# 8. Also we noted female passangers were always charged more fare and that can be reason we saw less female passangers as compared to male
# 9. The max fare for each class was 68 𝑓𝑜𝑟3𝑟𝑑𝑐𝑙𝑎𝑠𝑠,77
#   for 2nd class, and 263$ for 1st class passangers
# Heavy onboarding was seen from S Embarked where passangers from all class, all gender and al age group were seen to get on ship. One reason might be easy to get to this port appropriate fare for each class Passangers.
# Passangers from S enbarked were affected as well as saved more than any other port.
# Similar sinario was observed from C Embarked but passsanger were saved more than those who were not saved because most of them belonged from 1st class category
# Q embarked was very inconvienent to get and hence only 3rd class people were boarding from this port and most of them did not survived the disaster.
# People travelling woth families paid paid more amount than people travelling alone.
# Keeping in mind the above analysis we can focus on reducing the fare for female passangers. Increase transport for Q port and promote travelling with families.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




