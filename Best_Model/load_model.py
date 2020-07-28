# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 18:57:26 2020

@author: Ivona-pc
"""

import joblib 
import pandas as pd

#Loading the saved model with joblib
pipe = joblib.load('model.pkl')

# New data to predict
pr = pd.read_csv('dataset_to_predict.csv')
pred_cols = list(pr.columns.values)[:-1]

# apply the whole pipeline to data
pred = pd.Series(pipe.predict(pr[pred_cols]))
print (pred)