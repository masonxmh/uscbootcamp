# machine-learning-challenge

## Background

Over a period of nine years in deep space, the NASA Kepler space telescope has been out on a planet-hunting mission to discover hidden planets outside of our solar system.

### Preprocess the Data

* Preprocess the dataset prior to fitting the model.
* Perform feature selection and remove unnecessary features.
* Use `MinMaxScaler` to scale the numerical data.
* Separate the data into training and testing data.

### Tune Model Parameters

* Use `GridSearch` to tune model parameters.
* Tune and compare at least two different classifiers.

- - -

## Resources

* [Exoplanet Data Source](https://www.kaggle.com/nasa/kepler-exoplanet-search-results)

## Analysis

---
### Feature Selection

* The first step after reading the data to a dataframe is to decide which features to keep for the model. By using Filter Method filter and take only the subset of the relevant features. The model is built after selecting the features. The filtering here is done using correlation matrix and it is most commonly done using Pearson correlation.

* Here we will first plot the Pearson correlation heatmap and see the correlation of independent variables with the output variable MEDV. We will only select features which has correlation of above 0.01 (taking absolute value) with the output variable.

* The correlation coefficient has values between -1 to 1
— A value closer to 0 implies weaker correlation (exact 0 implying no correlation)
— A value closer to 1 implies stronger positive correlation
— A value closer to -1 implies stronger negative correlation

* One of the assumptions of linear regression is that the independent variables need to be uncorrelated with each other. If these variables are correlated with each other, then we need to keep only one of them and drop the rest. So I check the correlation of selected features with each other.

* Selecting columns based on p-value, we will be selecting the columns based on how they affect the p-value. We are the removing the column diagnosis because it is the column we are trying to predict

### Model-1 SVM

* After deciding which features to keep next step was assigning X and y values for the model to perform split data to get train and test data for the model.

* Next step is to scale and normalize the data to create more accurate model that has less gap between data points so they all have acurate weights for the model. Initially, using MinMaxScaler to scale the data with SVM model, the training and testing scores were around 0.85. Chaning to StandardScaler to scale the data resulted better numbers for the scores, Training Training Data Score: 0.8481785237459469 and Testing Data Score: 0.8558352402745996

* Using GridSearchCV to tune the model's parameters and changing the grid parameters kernel, C and gamma then get best parameters:
{'C': 200, 'gamma': 1e-05, 'kernel': 'linear'}
 0.8640077063579273

### Model-2 Logistic Regression
* For this model, data cleaning and preprocessing steps were the same as SVM model.

* Using MinMaxScaler to scale and normalize the data.

* The scores for training and testing data was :Training Data Score: 0.8458897577722678 and Testing Data Score: 0.8627002288329519

* Using GridSearchCV to tune the model's parameters, and changing C values, and increasing the number of iterations max_iter then get the best parameter:
{'C': 800, 'max_iter': 200}
0.8632459849074727

### Conclusion
* As a result, the two models SVM and LogisticRegression didn't have any significant difference between them for this data. We can say SVM model performs sligtly better.