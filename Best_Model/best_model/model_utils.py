# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:50:19 2020

@author: Ivona-pc
"""

import numpy as np
import pandas as pd

#Data reading, data cleaning
def clean_data(data):
    
    data = data.replace('unknown', np.nan)
    
    return data

#categoricat variables
def categorical_values(data_read):
    
    data = pd.DataFrame()
    data = data_read 
    data['education'] = data['education'].fillna(data['education'].mode()[0])
    data['job'] = data['job'].fillna(data['job'].mode()[0])
    data['marital'] = data['marital'].fillna(data['marital'].mode()[0])
    data['housing'] = data['housing'].fillna(data['housing'].mode()[0])
    data['default'] = data['default'].fillna(data['default'].mode()[0])
    
    return data
    
def mean_encoder(categorical_values):    
    #mean encoder
    
    data = pd.DataFrame()
    data = categorical_values
    data['y'].replace({"no":0, "yes":1}, inplace=True)
    
    Mean_encoded_job = data.groupby(['job'])['y'].mean().to_dict()   
    data['job'] =  data['job'].map(Mean_encoded_job) 
    
    Mean_encoded_marital = data.groupby(['marital'])['y'].mean().to_dict()   
    data['marital'] =  data['marital'].map(Mean_encoded_marital) 
    
    Mean_encoded_default = data.groupby(['default'])['y'].mean().to_dict()   
    data['default'] =  data['default'].map(Mean_encoded_default)

    Mean_encoded_housing = data.groupby(['housing'])['y'].mean().to_dict()   
    data['housing'] =  data['housing'].map(Mean_encoded_housing)

    Mean_encoded_loan = data.groupby(['loan'])['y'].mean().to_dict()   
    data['loan'] =  data['loan'].map(Mean_encoded_loan)

    Mean_encoded_contact = data.groupby(['contact'])['y'].mean().to_dict()   
    data['contact'] =  data['contact'].map(Mean_encoded_contact)

    Mean_encoded_month = data.groupby(['month'])['y'].mean().to_dict()   
    data['month'] =  data['month'].map(Mean_encoded_month)

    Mean_encoded_poutcome = data.groupby(['poutcome'])['y'].mean().to_dict()   
    data['poutcome'] =  data['poutcome'].map(Mean_encoded_poutcome)

    Mean_encoded_day_of_week = data.groupby(['day_of_week'])['y'].mean().to_dict()   
    data['day_of_week'] =  data['day_of_week'].map(Mean_encoded_day_of_week)
 
    Mean_encoded_education = data.groupby(['education'])['y'].mean().to_dict()   
    data['education'] =  data['education'].map(Mean_encoded_education)

    data_drop = pd.DataFrame()
    data_drop = data
    data_drop.fillna(data_drop.mean(), inplace = True)
    
    return data_drop

