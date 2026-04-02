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
# Step 5 : Hard Voting Classification
# ---------------------------------------------------------

hard_model = VotingClassifier(
    estimators=[
        ('lr', Model_LR),
        ('dt', Model_DT),
        ('knn', Model_KNN)
    ],
    voting='hard'
)

hard_model.fit(X_train, Y_train)

pred_hard = hard_model.predict(X_test)

acc_hard = accuracy_score(Y_test, pred_hard)

print("\nHard Voting Accuracy :", acc_hard)