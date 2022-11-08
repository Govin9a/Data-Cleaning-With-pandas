#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[26]:


flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()


# In[51]:


print(flights_data.head(4)) #printing first 5 flights 


# In[57]:


#Question 1 How many flights were there from JFK to SLC? Int
q_1 = flights_data[(flights_data['origin'] == 'JFK') & (flights_data['dest'] == 'SLC')] #All flights from JFK_to_SLC
print(len(q_1)) #number of flights from JFK to SLC


# In[58]:


#Question 2 How many airlines fly to SLC? Should be int
q_2 = flights_data[(flights_data['dest'] == 'SLC')]  #All flights to SLC
print(len(q_2)) #number of flights to SLC


# In[59]:


#Question 3 What is the average arrival delay for flights to RDU? float
q_3 = flights_data.groupby(flights_data['dest']=='RDU')['arr_delay'].mean().to_frame() #arrival delay to RDU
print(q_3)


# In[75]:


#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
Flights_NYC_to_SEA = flights_data[(flights_data['origin'].isin(['LGA', 'JFK'])) & (flights_data['dest'] == 'SEA')]  #Total flights from NYC to SEA  
len(Flights_NYC_to_SEA) #number of flights from NYC to SEA
len(flights_data[(flights_data['dest'] == 'SEA')]) #total number of flights to SEA
q_4 = len(Flights_NYC_to_SEA) / len(flights_data[(flights_data['dest'] == 'SEA')]) #porportion of flights from NYC(LGA+JFK) to SEA
print(q_4)


# In[61]:


#Question 5 Which date has the largest average depature delay? Pd slice with date and float. please make date a column. Preferred format is 2013/1/1 (y/m/d)
flights_data['date'] = flights_data['year'].astype(str) + '/' + flights_data['month'].astype(str) + '/' + flights_data['day'].astype(str) #changing the flight date format
q_5 = flights_data.groupby('date').mean() #Average flights by date
print(q_5.sort_values(['dep_delay'], ascending=False)['dep_delay'].head(1)) #largest no. of average departure delay


# In[64]:


#Question 6 Which date has the largest average arrival delay? pd slice with date and float
q_6 = flights_avg_by_date.sort_values(['arr_delay'], ascending=False)['arr_delay'].head(1) #sorting average flights by arrival date and extracting the largest average arrival date
print(q_6)


# In[65]:


#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed #speed = distance/airtime
flights_data ['speed'] = flights_data['distance']/flights_data['air_time']   #speed of all flights in the data
column = ['tailnum', 'speed']                                                #slicing tailnumber and speed
q_7 = flights_data.sort_values(['speed'], ascending=False)[column].head(1)   #sorting flights based on their speed
print(q_7)


# In[16]:


weather_data = pd.read_csv('weather.csv')
print(weather_data.head(4))


# In[ ]:


#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
weather_data = pd.read_csv('weather.csv')
weather_data.fillna(0)   #replacing nans with 0s. 
q_8 = (weather_data.to_string())   #to_string renders new dataframe to a tubular output. 
print(q_8)


# In[67]:


#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
feburary = weather_data_np[:,3] == 2.0   #indexing only the month of feburary 
q_9 = np.count_nonzero(feburary)       #counting nonzero values in the month of feburary
print(q_9)


# In[55]:


#Question 10 What was the mean for humidity in Feburary? Float
Feb_mean_humidity = np.split(weather_data_np[:,8], np.unique(weather_data_np[:,3],return_index=True)[1][1:]) #using splilt and unique function to filter humiditity for the month of feburary. 
q_10 = Feb_mean_humidity[1]
mean= np.mean(q_10) #calculating mean for humidity in Feburary
print(mean)


# In[56]:


#Question 11 What was the std for humidity in February? Float
Feb_mean_humidity = np.split(weather_data_np[:,8], np.unique(weather_data_np[:,3],return_index=True)[1][1:])
q_11 = Feb_mean_humidity[1]
std= np.std(q_11) #calculating standard deviation for humidity in feburary
print(std)

