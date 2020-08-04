<!DOCTYPE html>
<html>
 <head>
 </head>
<body>

<h2>Bank Marketing (with social/economic context)</h2>

:star: Star us on GitHub — it helps!

<p align="center"><img src="https://github.com/RistovaIvona/Bank-Marketing/blob/master/documentation/gvideo.gif" /></p>
<h3>Introduction </h3>

<small><p>
 <i>"Data-driven marketing is the engine behind improved marketing results and it creates measurable internal accountability as marketers become more effective in planning, executing and proving the value of their work" - Lisa Arthur </i>
 
Over the past decade, information consumption has drastically shot up, generating million terabytes of data every single day. For marketers, this amount of data is a gold mine. If this data could be properly processed and analyzed, it can deliver valuable insights. Data Science is a field that extracts meaningful information from data and helps marketers in discerning the right insights.These insights can be on various marketing aspects such as customer intent, experience, behavior, etc that would help them in efficiently optimizing their marketing strategies and derive maximum revenue.</p>

<p>This project is about marketing campaign of Portuguese bank for term deposits with data of contacted customers in period of 2008 to 2010 and their respond of the calls. The data has 41188 observations of calls with 20 customer’s demographic and transaction features each. Analyzing the customers’ features in correlation with their responses of the calls should lead to identify type of customers which are more likely to make term deposits.

The aim of the project is to build a model which will predict the future response of new targeted customer.
The project is done in few phases:

- [Data Cleaning](#data-cleaning)
- [Features Analysis and Visualization](#features-analysis-and-visualization)
- [Models implementation](#models-implementation)
- [Conclusion](#conclusion)

</small></p>


## Data Cleaning

<p>There is no missing or incomplete values. All data left by clients as inaccessible/incomplete are attached as unknown.
The purpose of our analysis is not to delete the missing data, but to find a correlation between the data and thus fill it.
It is important to note that the unknown values in all features are not more than 5%. Considering this, we can use the correlation for fillment the 'unknown' values.
In the part of outliers, because it is about personal information and we do not have values that are unrealistic, they remain as specific cases. An example in this part are clients with more than 80 years that should not be deleted from the dataset.</p>

<p align="center"><a href="https://github.com/RistovaIvona/BankClassification/commit/93473b465c17e2a4f55da114d3331e901aa02d23">
<img width="75%" height="75%" src="https://github.com/RistovaIvona/BankClassification/blob/master/documentation/missing.png"></a></p>

## Features Analysis and Visualization

<p align="center"><a href="https://github.com/RistovaIvona/BankClassification/commit/fc01a98eaac76965e19f3df831610e07a148a7b3">
<img width="40%" height="40%" src="https://github.com/RistovaIvona/BankClassification/blob/master/documentation/data%20dist.png"></a></p>

<p> Dataset has unbalanced standard distribution ("Yes" - 12% and "No" - 88%). </p>

<p align="center">
<a href="https://github.com/RistovaIvona/BankClassification/commit/fc01a98eaac76965e19f3df831610e07a148a7b3"><img width="45%" height="45%" src="https://github.com/RistovaIvona/BankClassification/blob/master/documentation/pdf%20of%20age.png"></a>
<img width="45%" height="45%" src="https://github.com/RistovaIvona/BankClassification/blob/master/documentation/sub%20vs%20contact%20rate.png"></a>
</p>
 
<p>The majority of the costumers belong into group from 30 to 40 years. Considering the distribution of the class and the age-variable, we divided the customer in the different age-groups in order to make better analysis how age influance on the subscription rate. 
The bank was more effective with 20s and 60s aged group, which should be the next target. Considering that the term deposits are the most liquid and the most secure investment, the pattern is expected.The oldest aged group want to have cash and youngest do not have experience, knowledge and enough money for better and more sophisticated investments. On other hand, the 30s aged group have more loans and less money for savings.</p>

<p align="center"><a href="https://github.com/RistovaIvona/BankClassification/commit/fc01a98eaac76965e19f3df831610e07a148a7b3"><img width="45%" height="45%" src="https://github.com/RistovaIvona/BankClassification/blob/master/documentation/duration.png"></a></p>

<p> Also the "duration" (last contact duration) can be useful feature for predicting the target variable. It is expected because it is already mentioned in the data overview that this field highely affects the target variable and should only be used for benchmark purposes.</p>

<p align="center">
 <a href="https://github.com/RistovaIvona/BankClassification/commit/fc01a98eaac76965e19f3df831610e07a148a7b3"><img width="30%" height="30%" src="https://github.com/RistovaIvona/Bank-Marketing/blob/master/documentation/marital.png"></a>
 <a href="https://github.com/RistovaIvona/BankClassification/commit/fc01a98eaac76965e19f3df831610e07a148a7b3"><img width="28%" height="28%" src="https://github.com/RistovaIvona/Bank-Marketing/blob/master/documentation/education.png"></a>
 <a href="https://github.com/RistovaIvona/BankClassification/commit/fc01a98eaac76965e19f3df831610e07a148a7b3"><img width="30%" height="30%" src="https://github.com/RistovaIvona/Bank-Marketing/blob/master/documentation/housing.png"></a>
</p>

<p>These categorial fueatures (marital status, education and housing) have not impact on subscription rate. Exception from this conclusion is the feature education, because the subscription rate of the illiterate shows higher rate of subscription. This is expected because this group does not have knowledge for better and sophisticated kinds of investment.<p>

<p align="center"><a href="https://github.com/RistovaIvona/BankClassification/commit/fc01a98eaac76965e19f3df831610e07a148a7b3"><img width="60%" height="60%" src="https://github.com/RistovaIvona/BankClassification/blob/master/documentation/sub%20by%20month.png"></a>

<p>The bank’s contact rate and clients’ response rate in each month have diffrent directions. This can be interpret on two ways. Either the bank starts to contact the clients when the demand of deposits starts to decrease or that the bank has bad timing for contacting. The contact rate is the highest in may and august and on other hand, the highest subscription rate occured in march, september and october</p> 

<p>For more :<q>Build a future where people live in harmony with nature.</q></p>

<p align="center"><a href="https://github.com/RistovaIvona/BankClassification/commit/0582900d7e5cf230ac071cd8c1107a9a8b060483"><img width="60%" height="60%" src="https://github.com/RistovaIvona/BankClassification/blob/master/documentation/heatmap.png"></a>

<p>From the above heatmap we can see that there are some numerical features which share a high correlation between them, e.g nr.employed and euribor3m these features share a correlation value of 0.95, and euribor3m and emp.var.rate share a correlation of 0.97, which is very high compared to the other features that we see in the heatmap.

:star: For more visualization and relationships between the features read our file  <a href="https://github.com/RistovaIvona/BankClassification/blob/master/DataVisualization.ipynb"><b>"Data Visualization".</b></a>

## Models implementation 

<p>In order to be able to discuss the models and their accuracy first must be completed, the data processing, reprocessing, cleaning and data analysis. 
To make better results we compare some techniques and here we present the best of them.
Before we build and train models we make feature engineering task and split the data into train and test.
 
One very common step in any feature engineering task is converting categorical features into numerical. This is called encoding and although there are several encoding techniques, there’s one in particular that we use here — mean encoding. 
Unlike label encoding, which gets the work done efficiently but in a random way, mean encoding tries to approach the problem more logically. In a nutshell, it uses the target variable as the basis to generate the new encoded feature. So, this is the first part that we want to present something different from basic encoding, and we get better results.

The problem with this dataset is that we have imbalanced classification problem and we can not use simple split to dataset. The challenge of working with imbalanced datasets is that most machine learning techniques will ignore, and in turn have poor performance on, the minority class, although typically it is performance on the minority class that is most important. One way to solve this problem is to oversample the examples in the minority class. This can be achieved by simply duplicating examples from the minority class in the training dataset prior to fitting a model. This can balance the class distribution but does not provide any additional information to the model. The most widely used approach to synthesizing new examples is called the Synthetic Minority Oversampling Technique, or SMOTE for short. This technique is used in our dataset too and with its usage the results are better.  

Several models are defined and in the next picture, so we can see the progress and improvement of the accuracy of the models.</p>

<p align="center"><a href="https://github.com/RistovaIvona/BankClassification/commit/fc01a98eaac76965e19f3df831610e07a148a7b3"><img width="40%" height="40%" src="https://github.com/RistovaIvona/BankClassification/blob/master/documentation/models.png"></a></p>
 
<p>From what has been shown,<b>it is clear that Gradient Boosting and XGBoost give the best results.</b> For example, XGBoost derived from chain of tree based models and has it roots in the very first Decision Tree Model. Each model had improvements over the previous one, making XGBoost and Gradient Boost most advanced and sophisticated models so far.</p>

<p align="center"><a href="https://github.com/RistovaIvona/BankClassification/commit/fc01a98eaac76965e19f3df831610e07a148a7b3"><img width="50%" height="50%" src="https://github.com/RistovaIvona/BankClassification/blob/master/documentation/roc.png"></a>

<p>Both models have some predefined parameters and using them is not always best practice.
In our case the models with parameter adjustment give some slight improvement less than 0.2. Therefore, models with predefined parameters are used so that a trade-off can be made because the time spent on setup does not give us any significant improvements.</p>

</p>XGBoost gives the best results, but in the end it was able to identify slightly more than a half of positive outcomes, which tells that there must be other ways to improve it. Maybe we need more data or we need to modify what we have. The data science process never ends.</p>

:star: To see all the models that we have tried please read our file <a href="https://github.com/RistovaIvona/BankClassification/blob/master/Models.ipynb"><b>"Models"</b></a>.

## Conclusions and recommendations for future research

<p>
First when you get the datase, it is really important to read and investigate different kind of  papers with marketing analysis. These are links of papers that we have read and helped us: 
 <ul>
   <li><a href="http://media.salford-systems.com/video/tutorial/2015/targeted_marketing.pdf">http://media.salfordsystems.com/video/tutorial/2015/targeted_marketing.pdf</a></li>
   <li><a href="https://pdfs.semanticscholar.org/1999/417377ec21ecf7f7f55af62975065f785fb2.pdf">https://pdfs.semanticscholar.org/1999/417377ec21ecf7f7f55af62975065f785fb2.pdf</a></li>
   <li><a href="http://archive.ics.uci.edu/ml/datasets/Bank+Marketing#">http://archive.ics.uci.edu/ml/datasets/Bank+Marketing#</a></li>
   <li><a href="https://github.com/yfsui/Bank-Telemarketing-ML-Project/blob/master/Portuguese%20Bank%20Telemarketing%20Analysis.ipynb"></a>https://github.com/yfsui/Bank-Telemarketing-ML-Project/blob/master/Portuguese%20Bank%20Telemarketing%20Analysis.ipynb</li>
   <li><a href="https://github.com/naveen-chauhan/Loan-Prediction-Classification/blob/master/Loan%2BPrediction.ipynb">https://github.com/naveen-chauhan/Loan-Prediction-Classification/blob/master/Loan%2BPrediction.ipynb</a></li>
 </ul>

Second, when you will load the data you need to understand each attribute meaning. The meaning of the feature is essential to have view how the feature impact on the data and what you can expect.
Third, clean data. We decided to replace the 'unknown' data. There are so many preprocess ways to clean and it is your way  to decide what you will do, but you have to be sure that the data are good enough for modeling. For this data set preprocessing and feature understanding is the most important step.
And last, try diffrent kind of models and compare the results and time.
 
As George E. P. Box said: “all models are wrong, but some are useful”.
</p>

  
</body>
</html>
