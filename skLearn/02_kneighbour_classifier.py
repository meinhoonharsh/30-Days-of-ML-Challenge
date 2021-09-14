# Day 4 of 30 Days of ML Challenge

# Imports
from sklearn import datasets                        # pip install sklearn
from sklearn.neighbors import KNeighborsClassifier  # pip install sklearn

# Load data
iris = datasets.load_iris()

# Creating Features and Labels
features = iris.data
labels = iris.target

# Create Classifier
classifier = KNeighborsClassifier()
classifier.fit(features, labels)

# Predicting Results
predict = classifier.predict([[3, 5, 4, 2], [5, 4, 3, 2]])
print(predict)
