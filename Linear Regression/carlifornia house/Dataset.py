"""DESCRIPTION

The US Census Bureau has published California Census Data which has 10 types of metrics such as the population, median income, median housing price, and so on for each block group in California. The dataset also serves as an input for project scoping and tries to specify the functional and nonfunctional r requirements for it.

Problem Objective:
The project aims at building a model of housing prices to predict median house values in California using the provided dataset. This model should learn from the data and be able to predict the median housing price in any district, given all the other metrics.

Districts or block groups are the smallest geographical units for which the US Census Bureau publishes sample data (a block group typically has a population of 600 to 3,000 people). There are 20,640 districts in the project dataset.

Domain: Finance and Housing

Analysis Tasks:

Build a model of housing prices to predict median house values in California using the provided dataset.
Train the model to learn from the data to predict the median housing price in any district, given all the other metrics.
Predict housing prices based on median_income and plot the regression chart for it.
Load the data :
• Read the “housing.csv” file from the folder into the program.
• Print first few rows of this data.
• Extract input (X) and output (Y) data from the dataset.

Handle missing values :
• Fill the missing values with the mean of the respective column.

Encode categorical data :
• Convert categorical column in the dataset to numerical data.

Split the dataset :
• Split the data into 80% training dataset and 20% test dataset.

Standardize data :
• Standardize training and test datasets.

Perform Linear Regression :
• Perform Linear Regression on training data.
• Predict output for test dataset using the fitted model.
• Print root mean squared error (RMSE) from Linear Regression.
[ HINT: Import mean_squared_error from sklearn.metrics ]

Bonus exercise: Perform Linear Regression with one independent variable :
• Extract just the median_income column from the independent variables (from X_train and X_test).
• Perform Linear Regression to predict housing values based on median_income.
• Predict output for test dataset using the fitted model.
• Plot the fitted model for training data as well as for test data to check if the fitted model satisfies the test data.

Dataset Size: 20640 rows x 10 columns"""