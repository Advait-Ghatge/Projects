import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

def Marvellous_Classifier(Datapath):

    Border = "-" * 70

    # Step 1 : Loading the dataset from CSV File
    
    print()
    print(Border)
    print("Step 1 : Loading the dataset from CSV File")
    print(Border)

    df = pd.read_csv(Datapath)

    print()
    print("Some entries from dataset are : \n")
    print(df.head())

    # Step 2 : Clean the dataset by removing empty rows
    
    print()
    print(Border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace = True)

    print()
    print("Total records :", df.shape[0])
    print("Total columns :", df.shape[1])

    # Step 3 : Separate Independent and Dependent Variables
    
    print()
    print(Border)
    print("Step 3 : Separate Independent and Dependent Variables")
    print(Border)

    X = df.drop(columns = ['Class'])
    Y = df['Class']

    print()
    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    print()
    print("Input Columns :", X.columns.tolist())
    print("Output Column :", "Class")

    # Step 4 : Split the dataset for Training and Testing
    
    print()
    print(Border)
    print("Step 4 : Split the dataset for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42, stratify = Y)

    print()
    print("Information of Training and Testing Data : ")

    print()
    print("Shape of X_train :", X_train.shape)

    print()
    print("Shape of Y_train :", Y_train.shape)

    print()
    print("Shape of X_test :", X_test.shape)

    print()
    print("Shape of Y_test :", Y_test.shape)

    # Step 5 : Feature Scaling
    
    print()
    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    Scaler = StandardScaler()

    # Independent Variable Scaling

    X_train_scaled = Scaler.fit_transform(X_train)
    X_test_scaled = Scaler.fit_transform(X_test)

    print()
    print("Feature Scaling completed!")

    # Step 6 : Exploring multiple values of K
    # Hyperparameter tuning (K)
    
    print()
    print(Border)
    print("Step 6 : Exploring multiple values of K")
    print(Border)

    accuracy_scores = []

    K_values = range(1, 21)

    for k in K_values:

        Model = KNeighborsClassifier(n_neighbors = k)

        Model.fit(X_train_scaled, Y_train)

        Y_pred = Model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_scores.append(accuracy)

    print()
    print("Accuracy Report of all K Values from 1 to 20 : ")
    print()

    for value in accuracy_scores:
        print(value)


    # Step 7 : Plotting graph of K v/s accuracy
    
    print()
    print(Border)
    print("Step 7 : Plotting graph of K v/s accuracy")
    print(Border)

    plt.figure(figsize = (8,5))
    plt.plot(K_values, accuracy_scores, marker = 'o')
    plt.grid(True)

    plt.title("K Values v/s Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")

    plt.xticks(list(K_values))
    plt.show()

    # print()
    # print("plt.show() is commented hence no graph is shown")


    # Step 8 : Finding best value of K
    
    print()
    print(Border)
    print("Step 8 : Finding best value of K")
    print(Border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print()
    print("Best value of K is :", best_k)


    # Step 9 : Building final model using best value of K
    
    print()
    print(Border)
    print("Step 9 : Building final model using best value of K")
    print(Border)

    final_model = KNeighborsClassifier(n_neighbors = best_k)

    final_model.fit(X_train_scaled, Y_train)

    Y_pred = final_model.predict(X_test_scaled)


    # Step 10 : Calculating final accuracy
    
    print()
    print(Border)
    print("Step 10 : Calculating final accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print()
    print("Accuracy of the final model is :", accuracy * 100)


    # Step 11 : Display Confusion Matrix
    
    print()
    print(Border)
    print("Step 11 : Display Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test, Y_pred)

    print()
    print("Confusion Matrix is : ")
    print()
    print(cm)

    # Step 12 : Display Classification Report
    
    print()
    print(Border)
    print("Step 12 : Display Classification Report")
    print(Border)

    print()
    print("Classification Report is : ")
    print()
    print(classification_report(Y_test, Y_pred))


def main():
    
    Border = "-" * 70

    print()
    print(Border)
    print("--------------------- Wine Classifier using KNN ----------------------")
    print(Border)

    Marvellous_Classifier("WinePredictor.csv")

if __name__ == "__main__":
    main()