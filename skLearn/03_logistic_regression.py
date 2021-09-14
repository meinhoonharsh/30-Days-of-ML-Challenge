# Day 6 of 30 Day of ML Challenge

# Import modules
from sklearn import datasets                            # pip install sklearn
from sklearn.linear_model import LogisticRegression     # pip install sklearn
import numpy as np                                      # pip install numpy
import matplotlib.pyplot as plt                         # pip install matplotlib

# Load data
iris = datasets.load_iris()

# Create X and Y Data
dataset_X = iris.data[:,3:]
dataset_Y = (iris.target == 2).astype(int)

# Create Logistic Regression Model
classifier = LogisticRegression()
classifier.fit(dataset_X, dataset_Y)

# Creating New Test Data
dataset_X_new = np.linspace(0, 3, 1000).reshape(-1, 1)

# Making Predictions 
predictions = classifier.predict_proba(dataset_X_new)
# prediction = classifier.predict([[3.1]])
# print(prediction)

# Plotting the Data
plt.plot(dataset_X_new, predictions[:,1], color='blue', linewidth=3)
plt.show()