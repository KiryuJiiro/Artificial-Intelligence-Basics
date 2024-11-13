from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Input features: age and salary
x = np.array([[42, 1900],
              [31, 50000],
              [37, 3000],
              [34, 225000],
              [50, 81000],
              [52, 30400],
              [37, 52000],
              [31, 71000],
              [32, 50000],
              [30, 130000]])

# Target labels (0 or 1)
y = np.array([0, 1, 0, 1, 1, 1, 0, 0, 0, 1])

# Split the dataset into training and testing sets (80% train, 20% test)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(xtrain, ytrain)

# New data point for prediction
xnew = np.array([[40, 200000]])
new_prediction = model.predict(xnew)

# Print the prediction for the new data point
print(f"Prediction for input {xnew[0]}: {new_prediction[0]}")

# Predict on the test set
y_pred = model.predict(xtest)

# Calculate accuracy of the model
accuracy = accuracy_score(ytest, y_pred)
print(f"Accuracy of the model: {accuracy:.2f}")