from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
import pandas as pd

# Generate and dataset for Logistic Regression
x, y = make_classification(
    n_samples=100,
    n_features=1,
    n_classes=2,
    n_clusters_per_class=1,
    flip_y=0.03,
    n_informative=1,
    n_redundant=0,
    n_repeated=0
)

# Create a scatter plot
plt.scatter(x, y, c=y, cmap='rainbow')
plt.title('Scatter Plot of Logistic Regression')
plt.title('__By Abhijeet Maity')
plt.show()

# Split the dataset into training and test dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

# Create a Logistic Regression Object, perform Logistic Regression
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)

# Show to Coeficient and Intercept
print("\n Coefficient_")
print(log_reg.coef_)
print("\n Intercept")
print(log_reg.intercept_)

# Perform prediction using the test dataset
y_pred = log_reg.predict(x_test)

# Show the Confusion Matrix
from sklearn.metrics import confusion_matrix
print("\n Confusion Matrix")
print(confusion_matrix(y_test, y_pred))
print('__By Abhijeet Maity')


