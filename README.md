# Bank Marketing (with social/economic context)

## Introduction

Marketing campaigns these days are necessary in every business, so it is the case in the financial services market too. In order to make the campaign successful it is mandatory to make analysis of customers’ needs and behaviors which will help to target customers and make the marketing campaigns more effective.
This project is about telemarketing campaign of Portuguese bank for term deposits with data of contacted customers in period of 2008 to 2010 and their respond of the calls. The data has 41188 observations of calls with 20 customer’s demographic and transaction features each. Analyzing the customers’ features in correlation with their responses of the calls should lead to identify type of customers which are more likely to make term deposits.

The aim of the project is to build a model which will predict the future response of new targeted customer.
The project is done in few phases:
    Data Cleaning
    Features Analysis and Visualization
    Models implementation
    Models Summary
    Conclusion

VISUALIZATION

"" from matplotlib import pyplot as plt
sns.countplot(x=data['y'])
plt.title('Distribution of classes')
plt.xlabel('Target class') ""

Comment: According to data distribution (two classes "yes" and "no") there is an unbalance data distribution. "Yes'es" is 88% and "No's" are 12%. For better understanding the data..... Since he....

#"Age" variable explanation:

"sns.FacetGrid(data, hue='y', size=5) \
.map(sns.distplot, 'age') \
.add_legend()
plt.title('PDF of age for target variable y')"

This graph shows the distribution of customers' age is left-side distributed which means that in data the majority of the costumers belong into group from 30 to 40 years.

Knowing of the distribution of the class and the age-variable we divided the customer in the different age group in order to make better analysis how to age influance on the subscription rate.

"lst = [data]
for column in lst:
    column.loc[column["age"] < 30,  'age_group'] = 30
    column.loc[(column["age"] >= 30) & (column["age"] <= 44), 'age_group'] = 40
    column.loc[(column["age"] >= 45) & (column["age"] <= 59), 'age_group'] = 50
    column.loc[column["age"] >= 60, 'age_group'] = 60"
    
    
"print('Success rate and total clients contacted for different age_groups:')
print('Clients age < 30 contacted: {}, Success rate: {}'.format(len(data[data['age_group'] == 30]), data[data['age_group'] == 30].y.value_counts()[1]/len(data[data['age_group'] == 30])))
print('Clients of age 30-45 contacted: {}, Success rate: {}'.format(len(data[data['age_group'] == 40]), data[data['age_group'] == 40].y.value_counts()[1]/len(data[data['age_group'] == 40])))
print('Clients of age 40-60 contacted: {}, Success rate: {}'.format(len(data[data['age_group'] == 50]), data[data['age_group'] == 50].y.value_counts()[1]/len(data[data['age_group'] == 50])))
print('Clients of 60+ age contacted: {}, Success rate: {}'.format(len(data[data['age_group'] == 60]), data[data['age_group'] == 60].y.value_counts()[1]/len(data[data['age_group'] == 60])))"

"age = pd.DataFrame(data['age_group'].value_counts())
age['% Contacted'] = age['age_group']*100/age['age_group'].sum()
age['% Subscribed a term deposit'] = count_age_y['yes']
age.drop('age_group',axis = 1,inplace = True)
age['age'] = [30,40,50,20,60]
age = age.sort_values('age',ascending = True)

plot_age = age[['% Subscribed a term deposit','% Contacted']].plot(kind = 'bar',
                                              figsize=(8,6), color = ('green','red'))
plt.xlabel('Age Group')
plt.ylabel('Subscription Rate')
plt.xticks(np.arange(5), ('<30', '30-39', '40-49', '50-59', '60+'),rotation = 'horizontal')
plt.title('Subscription vs. Contact Rate by Age')
plt.show()"

This graph indicates that the bank was focused on the 30s aged group(red bar), but this group has lower subscription rates(green bar) compared to the others aged groups.The bank was more effective with 20s and 60s aged group, which should be the next target. Considering that the term deposits are the most liquid and the most secure investment, the pattern is expected.The oldest aged group want to have cash and youngest do not have experience, knowledge and enough money for better and more sophisticated investments. On other hand, the 30s aged group have more loans and less money for savings.

#"Duration" variable explanation

"sns.boxplot(data=data, x="y", y="duration")
plt.show()"

From the above plot it is clear that, the duration (last contact duration) of a customer can be useful for predicting the target variable. It is expected because it is already mentioned in the data overview that this field highely affects the target variable and should only be used for benchmark purposes.

#"Marital, Loan and House" 

"Marriage=pd.crosstab(data["marital"],data['y'])
Marriage.div(Marriage.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))

Loan=pd.crosstab(data["loan"],data['y'])
Loan.div(Loan.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))

House=pd.crosstab(data["housing"],data['y'])
House.div(House.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))

Education=pd.crosstab(data["education"],data['y'])
Education.div(Education.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))"

These categorial fueatures (marital status, education and houseing) have not impact on supcription rate. Exception from this conclusion is the feature education, becouse the subcription rate of the iliterate shows higer rate of subscription. This is expected becouse this group dose not have knowlage for better and sofisticated kinds of investment. 

#Sesion, month subcription rate
"lst = [data]
for column in lst:
    column.loc[column["month"] == "jan", "month_int"] = 1
    column.loc[column["month"] == "feb", "month_int"] = 2
    column.loc[column["month"] == "mar", "month_int"] = 3
    column.loc[column["month"] == "apr", "month_int"] = 4
    column.loc[column["month"] == "may", "month_int"] = 5
    column.loc[column["month"] == "jun", "month_int"] = 6
    column.loc[column["month"] == "jul", "month_int"] = 7
    column.loc[column["month"] == "aug", "month_int"] = 8
    column.loc[column["month"] == "sep", "month_int"] = 9
    column.loc[column["month"] == "oct", "month_int"] = 10
    column.loc[column["month"] == "nov", "month_int"] = 11
    column.loc[column["month"] == "dec", "month_int"] = 12"
"count_month_y = pd.crosstab(data['y'],data['month_int']).apply(lambda x: x/x.sum() * 100)
count_month_y = count_month_y.transpose()

month = pd.DataFrame(data['month_int'].value_counts())
month['% Contacted'] = month['month_int']*100/month['month_int'].sum()
month['% Subscribed a term deposit'] = count_month_y['yes']
month.drop('month_int',axis = 1,inplace = True)
month['Month'] = [5,7,8,6,11,4,10,9,3,12]
month = month.sort_values('Month',ascending = True)


plot_month = month[['% Subscribed a term deposit','% Contacted']].plot(kind ='line',
                                                          figsize = (10,6),
                                                          marker = 'o')
plt.title('Subscribed a term deposit vs. Contact Rate by Month')
plt.ylabel('Subscription and Contact Rate')
plt.xlabel('Month')
ticks = np.arange(1,13,1)
plt.xticks(ticks)

# Annotation: peak of contact
y = month['% Contacted'].max()
x = month['% Contacted'].idxmax()
plt.annotate('May: Peak of contact', xy=(x+0.1, y+0.1), xytext=(x+1,y+4), arrowprops=dict(facecolor='black', headwidth=6, width=1, headlength=4), horizontalalignment='left', verticalalignment='top')
# Annotation: peak of subscription rate
y = month['% Subscribed a term deposit'].max()
x = month['% Subscribed a term deposit'].idxmax()
plt.annotate('March: Peak Subscription rate', xy=(x+0.1, y+0.1), xytext=(x+1,y+1), arrowprops=dict(facecolor='black', headwidth=6, width=1, headlength=4), horizontalalignment='left', verticalalignment='top')
plt.show()"

The graphic above shows the bank’s contact rate and clients’ response rate in each month.The trends of the lines have diffrent directions. This can be interpret on two ways. Either the bank starts to contact the clients when the demand of deposits starts to decrease or that the bank has bad timing for contacting. The contact rate is the highest in may and august and on other hand, the highest subscription rate occured in march, september and october.


#Correlation"

#Change 'day' from words to numbers for easier analysis
#"mon","tue","wed","thu","fri"
lst = [data]
for column in lst:
    column.loc[column["day_of_week"] == "mon", "day_int"] = 1
    column.loc[column["day_of_week"] == "tue", "day_int"] = 2
    column.loc[column["day_of_week"] == "wed", "day_int"] = 3
    column.loc[column["day_of_week"] == "thu", "day_int"] = 4
    column.loc[column["day_of_week"] == "fri", "day_int"] = 5"
    
    
"lst = [data]
for column in lst:
    column.loc[column["age"] < 30,  'age_group'] = 20
    column.loc[(column["age"] >= 30) & (column["age"] <= 39), 'age_group'] = 30
    column.loc[(column["age"] >= 40) & (column["age"] <= 49), 'age_group'] = 40
    column.loc[(column["age"] >= 50) & (column["age"] <= 59), 'age_group'] = 50
    column.loc[column["age"] >= 60, 'age_group'] = 60"
    
    
"def drawheatmap(df):
    matrix = data.corr()
    f, ax = plt.subplots(figsize=(15, 15))
    sns.heatmap(matrix, vmax=.8, square=True, cmap='YlGnBu', ax=ax, annot=True, linewidth=0.1)"
    
  In corr matrix we add one categoric value to be as numerci, day_of_week as day_int so we can see that there is no correlation between categoric and numeric values as we expected to be. From the above heatmap we can see that there are some numerical features which share a high correlation between them, e.g nr.employed and euribor3m these features share a correlation value of 0.95, and euribor3m and emp.var.rate share a correlation of 0.97, which is very high compared to the other features that we see in the heatmap.

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

As George E. P. Box said: “all models are wrong, but some are useful”.





















