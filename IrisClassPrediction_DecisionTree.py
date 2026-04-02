import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-" * 60

############################################################
# Step 1 : Load the dataset
############################################################

print()
print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataSetPath = "iris.csv"

df = pd.read_csv(DataSetPath)

print()
print("Dataset gets loaded successfully...")

print()
print("Initial entries from dataset are : ")
print(df.head())

############################################################
# Step 2 : Data Analysis (EDA)
############################################################

print()
print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print()
print("Shape of dataset :", df.shape)

print()
print("Column Names :", list(df.columns))

print()
print("Missing Values (Per Column) : ")
print(df.isnull().sum())

print()
print("Class Distribution (Species Count)")
print(df["species"].value_counts())

print()
print("Statistical Report of Dataset : ")
print(df.describe())

############################################################
# Step 3 : Decide Independent and Dependent Variables
############################################################

print()
print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X : Independent Variables / Features
# Y : Dependent Variables / Labels

Features_Cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[Features_Cols]
Y = df["species"]

print()
print("X Shape :", X.shape)

print()
print("Y Shape :", Y.shape)

############################################################
# Step 4 : Visualization of Dataset
############################################################

print()
print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)

# Scatter Plot

plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)

plt.title("Iris : Petal Length v/s Petal Width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True)
plt.show()

############################################################
# Step 5 : Splitting the Dataset for Training and Testing
############################################################

print()
print(Border)
print("Step 5 : Splitting the Dataset for Training and Testing")
print(Border)

# Test size = 20 %
# Train size = 80 %

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.5,
    random_state = 42
)

print()
print("Data Splitting Activity Completed")

print()
print("X - Independent :", X.shape)     # 150, 4
print("Y - Dependent :", Y.shape)       # 150,
print("X_train :", X_train.shape)       # 120, 4
print("X_test :", X_test.shape)         # 30, 4
print("Y_train :", Y_train.shape)       # 120,
print("Y_test :", Y_test.shape)         # 30,

############################################################
# Step 6 : Build the Model
############################################################

print()
print(Border)
print("Step 6 : Build the Model")
print(Border)

print()
print("We are going to use - DecisionTreeClassifier")

Model = DecisionTreeClassifier(
    criterion = "gini",
    max_depth = 5,
    random_state = 42
)

print()
print("Model created successfully :", Model)

############################################################
# Step 7 : Train the Model
############################################################

print()
print(Border)
print("Step 7 : Train the Model")
print(Border)

Model.fit(X_train, Y_train)

print()
print("Model Training Completed")

############################################################
# Step 8 : Evaluate the Model
############################################################

print()
print(Border)
print("Step 8 : Evaluate the Model")
print(Border)

Y_pred = Model.predict(X_test)

print()
print("Model Evaluation (Testing) Completed")

print()
print(Y_pred.shape)

print()
print("Expected Answers : ")
print(list(Y_test))

print()
print("Predicted Answers : ")
print(Y_pred)

############################################################
# Step 9 : Evaluate the Model Performance
############################################################

print()
print(Border)
print("Step 9 : Evaluate the Model Performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)

print()
print("Accuracy of model is :", accuracy * 100)

cm = confusion_matrix(Y_test, Y_pred)

print()
print("Confusion Matrix : ")
print(cm)

print()
print("Classification Report : ")
print(classification_report(Y_test, Y_pred))

############################################################
# Step 10 : Plotting Confusion Matrix
############################################################

print()
print(Border)
print("Step 10 : Plotting Confusion Matrix")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = Model.classes_)

data.plot()
plt.title("Confusion Matrix of Iris Dataset")
plt.show()