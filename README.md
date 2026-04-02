# 🤖 Advanced Ensemble Architectures: Bagging & Boosting Case Studies

A deep dive into high-performance machine learning using Ensemble methods to solve complex real-world problems. This repository features two primary case studies: a **Breast Cancer Diagnostic Classifier** and a **California Housing Price Regressor**, demonstrating the power of combining multiple models to achieve superior predictive accuracy.

---

## 🎀 1. Breast Cancer Diagnostic Classification
**Project Overview:**
This project implements a diagnostic tool to classify tumors as Malignant or Benign using the Wisconsin Breast Cancer Dataset. By leveraging Bagging and Boosting architectures, the model achieves superior stability and recall compared to single-tree architectures.

* **Keywords:** `Ensemble Learning`, `Bagging`, `Random Forest`, `AdaBoost`, `Gradient Boosting`, `Scikit-Learn`
* **Bagging Implementation:** Utilizes **Random Forest** to reduce variance and prevent overfitting on high-dimensional clinical features.
* **Boosting Implementation:** Employs **AdaBoost** and **XGBoost** to iteratively correct misclassification errors, maximizing sensitivity (Recall) for malignant cases.
* **Performance Metrics:** Evaluated using **AUC-ROC**, **F1-Score**, and **Confusion Matrices** to minimize False Negatives in a clinical context.
* **Feature Importance:** Identifies key nuclear features (e.g., concave points, radius) that contribute most significantly to diagnostic accuracy.

**Technical Stack:**
* **Language:** Python (Pandas, NumPy)
* **ML Libraries:** Scikit-Learn, XGBoost
* **Algorithms:** Random Forest Classifier, AdaBoost, Gradient Boosting Machine (GBM)

---

## 🏠 2. California Housing Price Regression
**Project Overview:**
A predictive modeling project aimed at estimating median house values across California districts. The project focuses on handling non-linear spatial data and skewed distributions using advanced Boosting techniques and Weighted Ensembles.

* **Keywords:** `Regression Analysis`, `XGBoost`, `Stacking`, `Feature Engineering`, `Hyperparameter Tuning`
* **Gradient Boosting (XGBoost/CatBoost):** Implements state-of-the-art boosting algorithms to handle complex, non-linear relationships between geographical location (Lat/Long) and market price.
* **Hyperparameter Optimization:** Uses `GridSearchCV` and `RandomizedSearchCV` to fine-tune learning rates, tree depth, and subsampling ratios for peak performance.
* **Ensemble Stacking:** Combines multiple base learners (Linear Regression, Ridge, and Decision Trees) into a meta-regressor for a "Best-of-All" prediction strategy.
* **Evaluation:** Rigorously optimized for **Root Mean Squared Error (RMSE)** and **$R^2$ Score** to ensure high predictive power and reliability.

**Technical Stack:**
* **Language:** Python (Matplotlib, Seaborn)
* **ML Libraries:** Scikit-Learn, XGBoost, CatBoost
* **Algorithms:** Random Forest Regressor, XGBRegressor, StackingRegressor

---

## 🛠️ How to Use
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/yourusername/ensemble-machine-learning.git](https://github.com/yourusername/ensemble-machine-learning.git)
    ```
2.  **Install Dependencies:**
    ```bash
    pip install pandas numpy scikit-learn xgboost catboost matplotlib seaborn
    ```
3.  **Run the Notebooks/Scripts:**
    Execute the provided Python files to reproduce the training pipelines and evaluation metrics.

---

### 👨‍💻 Author
**Advait Rahul Ghatge**
*Machine Learning Engineer | Data Scientist*
