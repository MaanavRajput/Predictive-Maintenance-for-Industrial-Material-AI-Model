# -*- coding: utf-8 -*-
"""Predictive Maintenance AI.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tn8QBcwc13Rla-t1d4MfLVxu09KIZKOP

#Predictive AI model

##Connecting to gdrive
"""

from google.colab import drive
drive.mount('/content/drive')

"""##Uploading Data set"""

import pandas as pd
data = pd.read_csv('/content/drive/MyDrive/machine failure.csv')
data.head()

"""##Model Building

###Data Splliting
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]',
            'Torque [Nm]', 'Tool wear [min]']

X = data[features]  # input features
y = data['Machine failure']  # Target (1 = failure, 0 = no failure)

# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""###Scalling features"""

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""##Models in use

###Logistic Regression
"""

from sklearn.linear_model import LogisticRegression

# Initialize the logistic regression model
logreg = LogisticRegression()

# Train the model on the training data
logreg.fit(X_train_scaled, y_train)

"""Prdiction"""

y_pred = logreg.predict(X_test_scaled)
print(y_pred[2])

"""##Accuracy testing"""

from sklearn.metrics import accuracy_score, classification_report

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print accuracy
print(f"Accuracy: {accuracy:.4f}")

# Print classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

"""##Hyperparameter Tuning"""

from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [0.1, 1, 10, 100],  # Regularization strength
    'penalty': ['l1', 'l2'],  # Regularization type
    'solver': ['liblinear', 'saga']  # Algorithm for optimization
}

# Initialize grid search
grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5)

# Perform grid search
grid_search.fit(X_train_scaled, y_train)

# Best hyperparameters found by grid search
print("Best Hyperparameters:", grid_search.best_params_)

"""##Importing with pickle"""

import pickle

with open('Logistic_model.pkl', 'wb') as model_file:
    pickle.dump(logreg, model_file)

# Save the scaler as well
with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)
