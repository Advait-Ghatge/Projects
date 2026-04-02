A professional collection of end-to-end Machine Learning implementations using Python and scikit-learn. 
This suite demonstrates the complete ML lifecycle, including Exploratory Data Analysis (EDA), data cleaning, feature engineering, model training, and performance evaluation.

## 🍷 1. Wine Quality Classifier (KNN)
**Algorithm:** `KNeighborsClassifier`
* **Data Processing:** Implements `StandardScaler` for feature scaling to ensure distance-based calculations are accurate.
* **Hyperparameter Tuning:** Systematically iterates through $K$ values (1–20) and uses `matplotlib` to visualize the accuracy trend to find the optimal $K$.
* **Evaluation:** Uses Confusion Matrices and Classification Reports to measure precision across multiple wine classes.

## 🚢 2. Titanic Survivor Predictor (Logistic Regression)
**Algorithm:** `LogisticRegression`
* **Data Sanitization:** Features a robust `CleanTitanicData` function to handle missing values via median/mode imputation and drop redundant columns like `Passengerid` and `Cabin`.
* **Model Preservation:** Implements `joblib` for model serialization, allowing the trained model to be saved as a `.pkl` file and reloaded for future predictions.
* **Interpretability:** Extracts model coefficients to identify which features (e.g., Age, Sex, Fare) most heavily influenced survival outcomes.

## 🌸 3. Iris Species Predictor (Decision Tree)
**Algorithm:** `DecisionTreeClassifier`
* **Exploratory Data Analysis (EDA):** Includes visual data analysis using `matplotlib` scatter plots to identify clusters within petal and sepal measurements.
* **Model Configuration:** Uses the Gini Impurity criterion to build a tree with a maximum depth of 5, preventing overfitting while maintaining high interpretability.
* **Visualization:** Utilizes `ConfusionMatrixDisplay` to provide a graphical representation of model performance and classification accuracy.

## 🛍️ 4. Mall Customer Segmentation (K-Means)
**Algorithm:** `KMeans` Clustering
* **Unsupervised Insight:** Analyzes unlabeled data (Annual Income vs. Spending Score) to discover hidden segments in consumer behavior.
* **Optimal Clustering:** Employs the **Within-Cluster Sum of Squares (WCSS)** and the Elbow Method to mathematically determine the ideal number of clusters.
* **Feature Engineering:** Scales high-variance income data using `StandardScaler` to ensure the clustering algorithm treats both dimensions with equal weight.
