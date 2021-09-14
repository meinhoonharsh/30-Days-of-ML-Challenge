# Day 2 of 30 Days of ML Challenge

# Import modules
import numpy as np                                     # pip install numpy
import matplotlib.pyplot as plt                        # pip install matplotlib
from sklearn import datasets, linear_model             # pip install scikit-learn
from sklearn.metrics import mean_squared_error as mse  # pip install sklearn.metrics

# Load datasets 
diabetes = datasets.load_diabetes()

# With multiple features for more accuracy
diabetes_X = diabetes.data[:, np.newaxis, 2]
# With only one feature for linear regression Graph
# diabetes_X = diabetes.data

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Generate linear regression Model 
model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_y_train)

# Predictions
diabetes_y_pred = model.predict(diabetes_X_test)

# Print the results
print('Mean Squared Error: ', mse(diabetes_y_test, diabetes_y_pred))
print('Weight: ', model.coef_)
print('Intercept: ', model.intercept_)


# Plot the results
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='green', linewidth=3)
plt.show()