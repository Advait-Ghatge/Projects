import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# --------------------------------------------------------------
# Function Name :   LoadPreservedModel
# Description :     It is used to load preserved model
# Parameters :      File name
# Return :          Model
# Date :            14/03/2026
# Author :          Advait Rahul Ghatge
# --------------------------------------------------------------

def LoadPreservedModel(FileName):

    loaded_model = joblib.load(FileName)

    print("\nModel loaded successfully!")

    return loaded_model

# --------------------------------------------------------------
# Function Name :   PreserveModel
# Description :     It is used to preserve model on secondary
# Parameters :      Model, File name
# Return :          None
# Date :            14/03/2026
# Author :          Advait Rahul Ghatge
# --------------------------------------------------------------

def PreserveModel(Model, FileName):
    
    joblib.dump(Model, FileName)

    print("\nModel preserved successfully with name :", FileName)


# --------------------------------------------------------------
# Function Name :   TrainTitanicModel
# Description :     It does splitting of X, Y, training data and testing data
# Parameters :      df
#                   df ->       Pandas dataframe object
# Return :          None
# Date :            14/03/2026
# Author :          Advait Rahul Ghatge
# --------------------------------------------------------------

def TrainTitanicModel(df):

    # Split features and labels

    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    print("\nFeatures :\n")
    print(X.head())

    print("\nLabels :\n")
    print(Y.head())

    print("\nShape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

    print("\nShape of X_train :", X_train.shape)
    print("Shape of Y_train :", Y_train.shape)
    print("Shape of X_test :", X_test.shape)
    print("Shape of Y_test :", Y_test.shape)

    Model = LogisticRegression(max_iter = 1000)

    Model.fit(X_train, Y_train)

    print("\nModel Trained successfully!")

    print("\nIntercept of Model is :\n", Model.intercept_)
    print("\nCoefficients of Model are :")

    for feature, coefficient in zip(X.columns, Model.coef_[0]):
        print(feature, ":", coefficient)

    PreserveModel(Model, "MarvellousTitanic.pkl")

    loaded_model = LoadPreservedModel("MarvellousTitanic.pkl")

    Y_pred = loaded_model.predict(X_test)

    accuracy = accuracy_score(Y_pred, Y_test)

    print("\nAccuracy is :", accuracy)

    cm = confusion_matrix(Y_pred, Y_test)

    print("\nConfusion Matrix is :")
    print(cm)

# --------------------------------------------------------------
# Function Name :   DisplayInfo
# Description :     It helps display the formatted title
# Parameters :      Title (str)
# Return :          None
# Date :            14/03/2026
# Author :          Advait Rahul Ghatge
# --------------------------------------------------------------

def DisplayInfo(Title):

    print("\n" + "=" * 70)
    print(Title)
    print("=" * 70)

# --------------------------------------------------------------
# Function Name :   ShowData
# Description :     It shows basic information about dataset
# Parameters :      df
#                   df ->       Pandas dataframe object
#                   Message
#                   Message ->  Heading text to display
# Return :          None
# Date :            14/03/2026
# Author :          Advait Rahul Ghatge
# --------------------------------------------------------------

def ShowData(df, message):

    DisplayInfo(message)

    print("\nFirst 5 rows of dataset are :\n")
    print(df.head(5))

    print("\nShape of Dataset :\n")
    print(df.shape)

    print("\nColumn names :\n")
    print(df.columns.tolist())

    print("\nMissing values in each column :\n")
    print(df.isnull().sum())

# --------------------------------------------------------------
# Function Name :   CleanTitanicData
# Description :     It does preprocessing
#                   It removes unnecessary columns
#                   It handles missing values
#                   It converts text data to numeric format
#                   It does encoding to categorical columns
# Parameters :      df ->   Pandas dataframe
# Return :          df ->   Clean Pandas dataframe
# Date :            14/03/2026
# Author :          Advait Rahul Ghatge
# --------------------------------------------------------------

def CleanTitanicData(df):
    
    DisplayInfo("Step 2 : Original Data")

    print("\n", df.head())

    # Removing unnecessary columns

    drop_columns = ["Passengerid", "zero", "Name", "Cabin"]

    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to be dropped : \n")
    print(existing_columns)

    # Drop the unwanted columns

    df = df.drop(columns = existing_columns)

    DisplayInfo("Step 2 : Data after column(s) removal")
    print(df.head())

    # Handle age column

    if "Age" in df.columns:

        print("\nAge column before preprocessing :")
        print(df["Age"].head(10))

        # coerce -> Invalid value gets converted as NaN

        df["Age"] = pd.to_numeric(df["Age"], errors = "coerce")

        age_median = df["Age"].median()

        print("\nMedian of Age column is :", age_median)

        # Replace missing values with median

        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge column after preprocessing :")
        print(df["Age"].head(10))


    # Handle Fare column

    if "Fare" in df.columns:
        print("\nFare column before preprocessing :")
        print(df["Fare"].head(10))

        df["Fare"] = pd.to_numeric(df["Fare"], errors = "coerce")

        fare_median = df["Fare"].median()

        print("\nMedian of Fare column is :", fare_median)

        # Replace missing values with median

        df["Fare"] = df["Fare"].fillna(fare_median)

        print("\nFare column after preprocessing :")
        print(df["Fare"].head(10))

    
    # Handle Embarked column

    if "Embarked" in df.columns:
        print("\nEmbarked column before preprocessing :")
        print(df["Embarked"].head(10))

        # Converting the data into string

        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Remove missing values

        df["Embarked"] = df["Embarked"].replace(['nan', 'None', ''], np.nan)

        # Getting most frequent value

        embarked_mode = df["Embarked"].mode()[0]

        print("\nMode of embarked column :", embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked column after preprocessing :")
        print(df["Embarked"].head(10))

    
    # Handle Sex column

    if "Sex" in df.columns:
        print("\nSex column before preprocessing :")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"], errors = "coerce")

        print("\nSex column after preprocessing :")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing :")
    print(df.head())

    print("\nMissing values after preprocessing :")
    print(df.isnull().sum())

    # Encode embarked column

    df = pd.get_dummies(df,columns=["Embarked"], drop_first = True)

    print("\nData after encoding\n")

    print(df.head())
    print("\nShape of Dataset :")
    print(df.shape)

    # Convert Boolean Columns into Integer

    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\nData after encoding\n")

    print(df.head())
    print("\nShape of Dataset :")
    print(df.shape)

    return df

# --------------------------------------------------------------
# Function Name :   MarvellousTitanicLogistic
# Description :     This is main pipeline controller
#                   It loads the dataset, shows raw data
#                   It preprocesses the dataset and trains the model
# Parameters :      Data path of dataset file
# Return :          None
# Date :            14/03/2026
# Author :          Advait Rahul Ghatge
# --------------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):
    
    DisplayInfo("Step 1 : Loading the dataset")
    
    df = pd.read_csv(DataPath)

    ShowData(df, "Initial Dataset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)

# --------------------------------------------------------------
# Function Name :   main
# Description :     Starting point of the application
# Parameters :      None
# Return :          None
# Date :            14/03/2026
# Author :          Advait Rahul Ghatge
# --------------------------------------------------------------

def main():
    
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()