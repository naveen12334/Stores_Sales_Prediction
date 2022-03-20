# STORES_SALES_PREDICTION
Predicting sales of unique products which belongs to different stores with their weight and establishment year through connecting SQL Server Database and Power Bi Dashboard and deploy it on Heroku.

# Input values:
![](https://github.com/naveen12334/Stores_Sales_Prediction/blob/main/Input_Values.PNG)

# Result:
![](https://github.com/naveen12334/Stores_Sales_Prediction/blob/main/Result.PNG)

# PROBLEM STATEMENT:
Nowadays, shopping malls and Big Marts keep track of individual item sales data in order to forecast future client demand and adjust inventory management. In a data warehouse, these data stores hold a significant amount of consumer information and particular item details. By mining the data store from the data warehouse, more anomalies and common patterns can be discovered.

# Goal:
the goal is to predict the sales of the different stores of Big Mart according to the provided dataset based on the product,price.

# Approach:
The classical machine learning tasks like Data Exploration, Data Cleaning,Feature Engineering, Model Building and Model Testing. Try out different machine learning algorithms that’s best fit for the above case.

# Dataset:
https://www.kaggle.com/brijbhushannanda1979/bigmart-sales-data

# Project Various Steps:
# Data Transformation and Extraction:
Data is transformed into SQL Server from csv files and extract in python notebook from SQL Server through making a connection with pyodbc library.

# Train data:
![](https://github.com/naveen12334/Stores_Sales_Prediction/blob/main/SQL/sql_train.PNG)

# Test data:
![](https://github.com/naveen12334/Stores_Sales_Prediction/blob/main/SQL/SQL_test.PNG)

# Data Exploration:
I started exploring datasets using pandas, NumPy,matplotlib and seaborn.

# Model Selection:
Made many Models But selected RandomForest Regressor.

# Hyperparameter Optimization:
Using Randomizedsearch CV to select the best parameter for training the model

# Model Dump:
As per selected trained model is dumped to pickled format for app development

# Model Accuracy 
# Training : 70%
# Testing  : 59%

# Export data with predicted result back to SQL Server:
![](https://github.com/naveen12334/Stores_Sales_Prediction/blob/main/SQL/sql_pred.PNG)

# PowerBI Report:
![](https://github.com/naveen12334/Stores_Sales_Prediction/blob/main/Power%20Bi/Store_sale_powerbi_dashboard.PNG)

# Deployed:
Deployed on Heroku -- https://flightfprediction.herokuapp.com/









