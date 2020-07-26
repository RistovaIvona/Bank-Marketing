# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:09:26 2020

@author: Ivona-pc
"""

from sklearn.model_selection import train_test_split
from numpy import ravel
from imblearn.over_sampling import SMOTE

def train_test(data_drop):
    
    y = data_drop[['y']]
    X = data_drop.drop(['y'], axis=1)
    X_train_first, X_test, y_train_first, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    sm = SMOTE(random_state=2)
    X_train, y_train = sm.fit_resample(X_train_first, y_train_first.values.ravel())

    
    return X_train, X_test, y_train, y_test