# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:49:51 2020

@author: Ivona-pc
"""
import pandas as pd
import xgboost as xgb
from best_model.model_utils import clean_data, categorical_values, mean_encoder
from best_model.load_and_split import train_test
from joblib import dump


if __name__ == "__main__":
    # read the raw data, preprocess it and save it.
    data_filename = pd.read_csv('dataset.csv',sep = ';')
    cleaning = clean_data(data_filename)
    categorical = categorical_values(cleaning)
    data_drop = mean_encoder(categorical)

    # load preprocessed data
    X_train, X_test, y_train, y_test = train_test(data_drop)

    # model 
    clf = xgb.XGBClassifier(max_depth=5, n_estimators=100 ,class_weight='balanced', n_jobs=-1)
    clf.fit(X_train, y_train)
    dump(clf, 'xgb_model.joblib') 
    
    print()

