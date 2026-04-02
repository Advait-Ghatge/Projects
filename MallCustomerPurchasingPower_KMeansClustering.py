import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():

    Border = "=" * 50
    
    # ------------------------------------------
    # Step 1 : Load the Dataset
    # ------------------------------------------
        
    print()
    print(Border)
    print("Step 1 : Load the Dataset")
    print(Border)

    df = pd.read_csv("Mall_Customers.csv")

    print("\nFirst few records : ")
    print(df.head())

    print("\nShape of dataset : ")
    print(df.shape)

    print("\nMissing values : ")
    print(df.isnull().sum())

    # ------------------------------------------
    # Step 2 : Select Features (Independent)
    # ------------------------------------------
        
    print()
    print(Border)
    print("Step 2 : Select Features (Independent)")
    print(Border)

    X = df[["AnnualIncome", "SpendingScore"]]

    print("\nSelected Features : ")
    print(X.head())

    print("\nShape of Selected Features : ")
    print(X.shape)

    # ------------------------------------------
    # Step 3 : Scale the Data
    # ------------------------------------------
        
    print()
    print(Border)
    print("Step 3 : Scale the Data")
    print(Border)

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("\nData after scaling : ")
    print(X_scaled[:5])

    # ------------------------------------------
    # Step 4 : Use Elbow Method
    # ------------------------------------------
        
    print()
    print(Border)
    print("Step 4 : Use Elbow Method")
    print(Border)

    WCSS = []

    for i in range(1,11):

        Model = KMeans(n_clusters = i, random_state = 42, n_init = 10)

        Model.fit(X_scaled)

        WCSS.append(Model.inertia_)

    plt.figure(figsize = (8,5))
    plt.plot(range(1,11), WCSS, marker = 'o')

    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")

    plt.grid(True)
    plt.show()

    # ------------------------------------------
    # Step 5 : Train the Model
    # ------------------------------------------
        
    print()
    print(Border)
    print("Step 5 : Train the Model")
    print(Border)

    Model = KMeans(n_clusters = 4, random_state = 42, n_init = 10)
    Clusters = Model.fit_predict(X_scaled)

    df["Clusters"] = Clusters

    print("\nDataset with Clusters :")
    print(df.head(50))

    
if __name__ == "__main__":
    main()