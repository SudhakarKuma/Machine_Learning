# Question 1: Fit a non-linear regression (for degree = 2, 3, 4, 5, and 6) model for the predictor (X) in the data. 
# Compare the non-linear regression model with the KNN (for k = 1, 2, 3, 5, 7). Use LOOCV to calculate MSE for this comparison.
# Output required:
# a) A plot of mean squared error (for both training and testing) vs. degree of the polynomial for the polynomial regression
# b) A plot of mean squared error (for both training and testing) vs. k for KNN regression 

# ==============================================================================
# Load the libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset for first question
df = pd.read_csv('183236001@iitb.ac.in_Q1.csv')

# View the first five datapoints of the data 
print(df.head())

# Visualize the relation between the predictor and the target 
plt.figure(figsize = (12, 8))
plt.scatter(df['X'], df['Y'], s = 60, c = 'g')

# ============= Fit a standard linear regression to the data ===================

# Load the libraries required for fitting a regression model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Instantiate a linear regression model
lin_reg = LinearRegression(normalize = True)

# Extract the predictor and the target from the dataframe df
X_lin = df.drop('Y', axis = 1)
y_lin = df['Y']

# Fit the linear regression model
lin_reg.fit(X_lin, y_lin)

# Predict the output from the model 
y_pred_lin = lin_reg.predict(X_lin)

# Find the mean-squared error 
print("Mean-squared error of linear model:", mean_squared_error(y_pred_lin, y_lin))

# Plot the linear regression line
plt.figure(figsize = (12, 8))
plt.xlabel("Predicted value with linear fit", fontsize = 20)
plt.ylabel("Actual y-values", fontsize = 20)
plt.grid(1)
plt.scatter(y_pred_lin, y_lin, edgecolors = (0, 0, 0), lw = 2, s = 80)
plt.plot(y_pred_lin, y_pred_lin, 'k--', lw = 3)

# ================== Fit a polynomial regression model =========================

# Load the library required for feature engineering
from sklearn.preprocessing import PolynomialFeatures

# Extract the predictor from the dataframe df
X = df.iloc[:, 0:1].values 

# Calculate the MSE with a polynomial with varying degrees
degrees = [2, 3, 4, 5, 6, 7, 8, 9]
mse = []
for degree in degrees:
  poly = PolynomialFeatures(degree, include_bias = False)
  X_poly = poly.fit_transform(X)
  X_poly_feature_name = poly.get_feature_names(['Feature' + str(l) for l in range(1, 6)])
  df_poly = pd.DataFrame(X_poly, columns = X_poly_feature_name)  
  df_poly['y'] = df['Y']
  X_train = df_poly.drop('y',axis = 1)
  y_train = df_poly['y']
  poly = LinearRegression(normalize = True)
  model_poly = poly.fit(X_train, y_train)
  y_poly = poly.predict(X_train)
  mse.append(mean_squared_error(y_poly, y_train))

# Analyze the MSE with a polynomial with varying degrees
plt.figure(figsize = (12, 8))
plt.xlabel("Degrees", fontsize = 20)
plt.ylabel("Mean-squared Eror", fontsize = 20)
plt.grid(1)
plt.scatter(degrees, mse, edgecolors = (0, 0, 0), lw = 2, s = 80)
plt.plot(degrees, mse, 'k--', lw = 2)
