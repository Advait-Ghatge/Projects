from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ---------------------------------------------------------
# Step 1 : Load Dataset
# ---------------------------------------------------------

data = load_breast_cancer()

X = data.data
Y = data.target

print("\nShape of X :", X.shape)
print("\nShape of Y :", Y.shape)

# ---------------------------------------------------------
# Step 2 : Split the dataset
# ---------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# ---------------------------------------------------------
# Step 3 : Create Base Models
# ---------------------------------------------------------

Model_LR = LogisticRegression(max_iter=5000)
Model_DT = DecisionTreeClassifier(random_state=42)
Model_KNN = KNeighborsClassifier(n_neighbors=5)

# ---------------------------------------------------------
# Step 4 : Train Base Models
# ---------------------------------------------------------

Model_LR.fit(X_train, Y_train)
Model_DT.fit(X_train, Y_train)
Model_KNN.fit(X_train, Y_train)

# ---------------------------------------------------------
# Step 5 : Calculate Individual Accuracy
# ---------------------------------------------------------

pred_LR = Model_LR.predict(X_test)
pred_DT = Model_DT.predict(X_test)
pred_KNN = Model_KNN.predict(X_test)

acc_LR = accuracy_score(Y_test, pred_LR)
acc_DT = accuracy_score(Y_test, pred_DT)
acc_KNN = accuracy_score(Y_test, pred_KNN)

print("\nIndividual Model Accuracy :")
print("\nLogistic Regression :", acc_LR)
print("\nDecision Tree Classifier :", acc_DT)
print("\nK Nearest Neighbors :", acc_KNN)