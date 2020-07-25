<b>Bank Marketing (with social/economic context)</b>

## Introduction

Marketing campaigns these days are necessary in every business, so it is the case in the financial services market too. In order to make the campaign successful it is mandatory to make analysis of customers’ needs and behaviors which will help to target customers and make the marketing campaigns more effective.

This project is about telemarketing campaign of Portuguese bank for term deposits with data of contacted customers in period of 2008 to 2010 and their respond of the calls. The data has 41188 observations of calls with 20 customer’s demographic and transaction features each. Analyzing the customers’ features in correlation with their responses of the calls should lead to identify type of customers which are more likely to make term deposits.

The aim of the project is to build a model which will predict the future response of new targeted customer.
The project is done in few phases:
1. Data Cleaning
2. Features Analysis and Visualization
3. Models implementation
4. Models Summary
5. Conclusion

### Data Cleaning

When analyzing the data, we do not have values that are missing or incomplete. All data left by clients as inaccessible/incomplete are attached as unknown.
The purpose of our analysis is not to delete the missing data, but to find a correlation between the data and thus fill it.
It is important to note that the unknown values in all features are not more than 5%, so some correlation can be made and filling in all the missing values.
In the part of outliers, because it is about personal information and we do not have values that are unrealistic, they remain as specific cases. An example in this part are clients with more than 80 years that we really have and should not be deleted from the dataset.

### Features Analysis and Visualization

Dataset has unbalansed standard distribution ("Yes" - 12% and "No" - 88%). 
The majority of the costumers belong into group from 30 to 40 years. Knowing of the distribution of the class and the age-variable we divided the customer in the different age group in order to make better analysis how to age influance on the subscription rate. The bank was more effective with 20s and 60s aged group, which should be the next target. Considering that the term deposits are the most liquid and the most secure investment, the pattern is expected.The oldest aged group want to have cash and youngest do not have experience, knowledge and enough money for better and more sophisticated investments. On other hand, the 30s aged group have more loans and less money for savings.
Also the "duration" (last contact duration) can be useful feature for predicting the target variable. It is expected because it is already mentioned in the data overview that this field highely affects the target variable and should only be used for benchmark purposes.

These categorial fueatures (marital status, education and houseing) have not impact on supcription rate. Exception from this conclusion is the feature education, becouse the subcription rate of the iliterate shows higer rate of subscription. This is expected becouse this group dose not have knowlage for better and sofisticated kinds of investment. 

The bank’s contact rate and clients’ response rate in each month have diffrent directions. This can be interpret on two ways. Either the bank starts to contact the clients when the demand of deposits starts to decrease or that the bank has bad timing for contacting. The contact rate is the highest in may and august and on other hand, the highest subscription rate occured in march, september and october (link.......... za data vizualizacijaaaaaa)

In corr matrix we add one categoric value to be as numerci, day_of_week as day_int so we can see that there is no correlation between categoric and numeric values as we expected to be. From the above heatmap we can see that there are some numerical features which share a high correlation between them, e.g nr.employed and euribor3m these features share a correlation value of 0.95, and euribor3m and emp.var.rate share a correlation of 0.97, which is very high compared to the other features that we see in the heatmap.

<p align="center"> <img src = "https://media.macphun.com/img/uploads/customer/how-to/579/15531840725c93b5489d84e9.43781620.jpg?q=85&w=1340" width="50%" height="50%"/> </p>



### Models implementation

Models Overview:
In order to be able to discuss the models and their accuracy first must be completed, the data processing, reprocessing, cleaning and data analysis. In this section we divide the test and training data and define the models that can solve this classification problem.
In our case, several models are defined and in the next picture we can see the progress and improvement of the accuracy of the models.
//слика нова
 
From what has been shown, it is clear that Gradient Boosting and XGBoost give the best results. For example, XGBoost derived from chain of tree based models and has it roots in the very first Decision Tree Model. Each model had improvements over the previous one, making XGBoost and Gradient Boost most advanced and sophisticated models so far.
//слика од двата модели со roc curve
Both models have some predefined parameters and using them is not always best practice.
In our case the models with parameter adjustment give some slight improvement less than 0.2. Therefore, models with predefined parameters are used so that a trade-off can be made because the time spent on setup does not give us any significant improvements.
//opis na roc curve
Conclusion
XGBoost gives the best results, but in the end it was able to identify slightly more than a half of positive outcomes, which tells me there must be ways to improve it. Maybe I need more data or modify what I have. The data science process never ends.

### Models Summary

### Conclusion


As George E. P. Box said: “all models are wrong, but some are useful”.

  






















