<!DOCTYPE html>
<html>
 <head>
 </head>
<body>

<h2>Bank Marketing (with social/economic context)</h2>

:star: Star us on GitHub — it helps!

<h3>Introduction </h3>

<small><p>
 <i>"Data-driven marketing is the engine behind improved marketing results and it creates measurable internal accountability as marketers become more effective in planning, executing and proving the value of their work" - Lisa Arthur </i>
 
Over the past decade, information consumption has drastically shot up, generating million terabytes of data every single day. For marketers, this amount of data is a gold mine. If this data could be properly processed and analyzed, it can deliver valuable insights. Data Science is a field that extracts meaningful information from data and helps marketers in discerning the right insights.These insights can be on various marketing aspects such as customer intent, experience, behavior, etc that would help them in efficiently optimizing their marketing strategies and derive maximum revenue.</p>

<p>This project is about marketing campaign of Portuguese bank for term deposits with data of contacted customers in period of 2008 to 2010 and their respond of the calls. The data has 41188 observations of calls with 20 customer’s demographic and transaction features each. Analyzing the customers’ features in correlation with their responses of the calls should lead to identify type of customers which are more likely to make term deposits.

The aim of the project is to build a model which will predict the future response of new targeted customer.
The project is done in few phases:

- [Data Cleaning](#data-cleaning)
- [Features Analysis and Visualization](#feature-analysis-and-visualization)
- [Models implementation](#models-implementation)
- [Conclusion](#conclusion)

</small></p>


## Data Cleaning

<p>There is no missing or incomplete values. All data left by clients as inaccessible/incomplete are attached as unknown.
The purpose of our analysis is not to delete the missing data, but to find a correlation between the data and thus fill it.
It is important to note that the unknown values in all features are not more than 5%. Considering this, we can use the correlation for fillment the 'unknown' values.
In the part of outliers, because it is about personal information and we do not have values that are unrealistic, they remain as specific cases. An example in this part are clients with more than 80 years that should not be deleted from the dataset.</p>

## Features Analysis and Visualization

<img width="300" height="300" src="https://github.com/RistovaIvona/BankClassification/blob/master/data%20dist.png">

<p> Dataset has unbalanced standard distribution ("Yes" - 12% and "No" - 88%). </p>

<div>
 <img width="300" height="300" src="https://github.com/RistovaIvona/BankClassification/blob/master/pdf%20of%20age.png">
 <img width="300" height="300" src="https://github.com/RistovaIvona/BankClassification/blob/master/sub%20vs%20contact%20rate.png">
</div>
 
<p>The majority of the costumers belong into group from 30 to 40 years. Considering the distribution of the class and the age-variable, we divided the customer in the different age-groups in order to make better analysis how age influance on the subscription rate. 
The bank was more effective with 20s and 60s aged group, which should be the next target. Considering that the term deposits are the most liquid and the most secure investment, the pattern is expected.The oldest aged group want to have cash and youngest do not have experience, knowledge and enough money for better and more sophisticated investments. On other hand, the 30s aged group have more loans and less money for savings.</p>

<img width="300" height="300" src="https://github.com/RistovaIvona/BankClassification/blob/master/duration.png"> 

<p> Also the "duration" (last contact duration) can be useful feature for predicting the target variable. It is expected because it is already mentioned in the data overview that this field highely affects the target variable and should only be used for benchmark purposes.</p>

<div>
 <img width="220" height="200" src="https://github.com/RistovaIvona/BankClassification/blob/master/marital.png">
 <img width="220" height="220" src="https://github.com/RistovaIvona/BankClassification/blob/master/education%20(1).png">
 <img width="220" height="220" src="https://github.com/RistovaIvona/BankClassification/blob/master/housing.png">
</div>

<p>These categorial fueatures (marital status, education and houseing) have not impact on supcription rate. Exception from this conclusion is the feature education, becouse the subcription rate of the iliterate shows higer rate of subscription.This is expected because this group does not have knowledge for better and sofisticated kinds of investment. <p>

<img width="350" height="350" src="https://github.com/RistovaIvona/BankClassification/blob/master/sub%20by%20month.png">

<p>The bank’s contact rate and clients’ response rate in each month have diffrent directions. This can be interpret on two ways. Either the bank starts to contact the clients when the demand of deposits starts to decrease or that the bank has bad timing for contacting. The contact rate is the highest in may and august and on other hand, the highest subscription rate occured in march, september and october</p> 

<p>For more :<q>Build a future where people live in harmony with nature.</q></p>

<p>From the above heatmap we can see that there are some numerical features which share a high correlation between them, e.g nr.employed and euribor3m these features share a correlation value of 0.95, and euribor3m and emp.var.rate share a correlation of 0.97, which is very high compared to the other features that we see in the heatmap.

## Models implementation 

<p>In order to be able to discuss the models and their accuracy first must be completed, the data processing, reprocessing, cleaning and data analysis. In this section we divide the test and training data and define the models that can solve this classification problem.
In our case, several models are defined and in the next picture we can see the progress and improvement of the accuracy of the models.</p>

<img width="300" height="300" src="https://github.com/RistovaIvona/BankClassification/blob/master/models.png">
 
<p>From what has been shown, it is clear that Gradient Boosting and XGBoost give the best results. For example, XGBoost derived from chain of tree based models and has it roots in the very first Decision Tree Model. Each model had improvements over the previous one, making XGBoost and Gradient Boost most advanced and sophisticated models so far.</p>

<img width="300" height="300" src="https://github.com/RistovaIvona/BankClassification/blob/master/roc.png">

<p>Both models have some predefined parameters and using them is not always best practice.
In our case the models with parameter adjustment give some slight improvement less than 0.2. Therefore, models with predefined parameters are used so that a trade-off can be made because the time spent on setup does not give us any significant improvements.</p>

</p>XGBoost gives the best results, but in the end it was able to identify slightly more than a half of positive outcomes, which tells that there must be other ways to improve it. Maybe we need more data or we need to modify what we have. The data science process never ends.</p>


## Conclusion

<p>As George E. P. Box said: “all models are wrong, but some are useful”.</p>

  
</body>
</html>
