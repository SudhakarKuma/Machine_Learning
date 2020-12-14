# Question 2: Perform classification using decision tree and linear support vector machine for the threedimensional data.
# Output required:
# a.) A plot of three-dimensional decision boundaries of the two classifiers
# b.) Confusion Matrix for the two classifiers

# ==============================================================================

# Load the libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset for first question
df = pd.read_csv("183236001@iitb.ac.in_Q2.csv")

# View the first five datapoints of the data 
print(df.head())
print('\n\n')

# Visualize the relation between the predictor and the target 
fig = plt.figure(figsize = (10, 10)) 
ax = plt.axes(projection ='3d') 
ax.scatter(df['X1'], df[' X2'], df[' X3'], c = df[' Class']) 

# Check the number of levels in the target variable
df[' Class'].value_counts() # Multi-class classification 

# Extract the predictor and the target from the dataframe df
X = que2.iloc[:,[0, 1, 2]]
y = que2.iloc[:, 3]

# ======================== Apply a decision tree ===============================

# Import the necessary libraries 
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import metrics
from sklearn.model_selection import train_test_split 

# Split the dataframe into training and testing datasets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, 
                                                    stratify = y, 
                                                    random_state = 42)

# Fit a Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'gini', max_depth = 4, random_state = 42)
classifier.fit(X_train, y_train)

# Evaluate the performance of the model on training set
y_pred_train = classifier.predict(X_train)
accuracy = metrics.accuracy_score(y_train, y_pred_train)
print("Accuracy: {:.2f}".format(accuracy))
print('\n')
cm = confusion_matrix(y_train, y_pred_train)
print('Confusion Matrix: \n', cm)
print('\n\n')

# Evaluate the performance of the model on testing set
y_pred_test = classifier.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred_test)
print("Accuracy: {:.2f}".format(accuracy))
print('\n')
cm = confusion_matrix(y_test, y_pred_test)
print('Confusion Matrix: \n', cm)
print('\n')

# ======================== Apply a Support Vector Machine ======================

# Import the necessary library
from sklearn.svm import SVC 

# Fit an SVM model 
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train) 

# Evaluate the performance of the SVM model on training set
y_pred_train = svm_model_linear.predict(X_train)
accuracy = metrics.accuracy_score(y_train, y_pred_train)
print("Accuracy: {:.2f}".format(accuracy))
print('\n')
cm = confusion_matrix(y_train, y_pred_train)
print('Confusion Matrix: \n', cm)
print('\n\n')

# Evaluate the performance of the model on testing set
y_pred_test = svm_model_linear.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred_test)
print("Accuracy: {:.2f}".format(accuracy))
print('\n')
cm = confusion_matrix(y_test, y_pred_test)
print('Confusion Matrix: \n', cm)

