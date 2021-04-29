#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]


# In[15]:


def BMI(data:list):
    info=data
    variables=len(info)
    result=[]
    for i in range(variables):
        info2=data[i]
        height=data[i]['HeightCm']/100
        weight=data[i]['WeightKg']
        bmi=round(weight/height**2,1)
        info2['bmi in kg/m2']=bmi
        if (bmi<=18.4):
            info2['BMI Category']='Underweight'
            info2['Health risk']= 'Malnutrition risk'
            result.append(info2)
        elif (bmi >=18.5 and bmi <= 24.9):
            info2['BMI Category']='Normal weight'
            info2['Health risk']= 'Low risk'
            result.append(info2)
        elif (bmi >=25 and bmi<=29.9):
            info2['BMI Category']='Overweight'
            info2['Health risk']= 'Enhanced risk'
            result.append(info2)
        elif (bmi >=30 and bmi<=34.9):
            info2['BMI Category']='Moderately obese'
            info2['Health risk']= 'Medium risk'
            result.append(info2)
        elif (bmi >=35 and bmi<=39.9):
            info2['BMI Category']='Severely obese'
            info2['Health risk']= 'High risk'
            result.append(info2)
        else:
            info2['BMI Category']='Very severely obese'
            info2['Health risk']= 'Very high risk'
            result.append(info2)
            
    return result


# In[16]:


#Overweight function
def overweight(result:list):
    info=result
    variables=len(info)
    count=0
    for i in range(variables):
        if (result[i]['BMI Category']=='Overweight'):
            count=count+1
            
    return count


# In[17]:


#Results  
result_BMI=BMI(data)
print(result_BMI)

result_overweight=overweight(data)
print(result_overweight)


# In[ ]:





# In[ ]:




