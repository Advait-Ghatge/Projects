import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ---------------------------------------------------
# Step 1 - Load The Dataset
# ---------------------------------------------------

df = pd.read_csv("California_Housing.csv")

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
# Step 4 - Create Gradient Boosting Model
# ---------------------------------------------------

boost_model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42)

# ---------------------------------------------------
# Step 5 - Train Boosting Model
# ---------------------------------------------------

boost_model.fit(X_train, Y_train)

# ---------------------------------------------------
# Step 6 - Test Boosting Model
# ---------------------------------------------------

Y_pred = boost_model.predict(X_test)

# ---------------------------------------------------
# Step 7 - Evaluate Boosting Model
# ---------------------------------------------------

print("\nMean Squared Error :", mean_squared_error(Y_pred, Y_test))
print("\nR-square :", r2_score(Y_test, Y_pred))