import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ---------------------------------------------------
# Step 1 - Load The Dataset
# ---------------------------------------------------

df = pd.read_csv("Breast_Cancer.csv")

print("\nShape of Dataset is :", df.shape)

print("\nFirst 5 records :")
print(df.head())

# ---------------------------------------------------
# Step 2 - Separate Features and Labels
# ---------------------------------------------------

X = df.drop("target", axis=1)
Y = df["target"]

# ---------------------------------------------------
# Step 3 - Split Dataset for Training and Testing
# ---------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# ---------------------------------------------------
# Step 4 - Create Base Model
# ---------------------------------------------------

base_model = DecisionTreeClassifier(random_state=42)

# ---------------------------------------------------
# Step 5 - Create Bagging Model
# ---------------------------------------------------

bagging_model = BaggingClassifier(
    estimator = base_model,
    n_estimators = 10,
    random_state = 42
    )

# ---------------------------------------------------
# Step 6 - Train Bagging Model
# ---------------------------------------------------

bagging_model.fit(X_train, Y_train)

# ---------------------------------------------------
# Step 7 - Test Bagging Model
# ---------------------------------------------------

Y_pred = bagging_model.predict(X_test)

# ---------------------------------------------------
# Step 8 - Evaluate Bagging Model
# ---------------------------------------------------

print("\nBagging Accuracy :", accuracy_score(Y_test, Y_pred))
print("\nConfusion Matrix :\n", confusion_matrix(Y_test, Y_pred))