A deep dive into high-performance machine learning using Ensemble methods to solve complex real-world problems. This repository features two primary case studies: a Breast Cancer Diagnostic Classifier utilizing Bagging (Random Forest) and AdaBoost to maximize recall, and a California Housing Price Regressor employing Gradient Boosting (XGBoost) and Stacking to handle non-linear spatial data and minimize RMSE.

🎀 **1. Breast Cancer Diagnostic Classification**

Keywords - Ensemble Learning, Bagging, Random Forest, AdaBoost, Gradient Boosting, Scikit-Learn

Project Overview -
This project implements a diagnostic tool to classify tumors as Malignant or Benign using the Wisconsin Breast Cancer Dataset. By leveraging Bagging (Random Forest) and Boosting (AdaBoost/Gradient Boosting), the model achieves superior stability and recall compared to single-tree architectures.

Key Features -
Bagging Implementation: Utilizes Random Forest to reduce variance and prevent overfitting on high-dimensional clinical features.

Boosting Implementation - Employs AdaBoost and XGBoost to iteratively correct misclassification errors, maximizing the sensitivity (Recall) for malignant cases.

Performance Metrics - Evaluated using Area Under the ROC Curve (AUC-ROC), F1-Score, and Confusion Matrices to minimize False Negatives.

Feature Importance - Identifies key nuclear features (e.g., concave points, radius) that contribute most to diagnostic accuracy.

Technical Stack
Language: Python (Pandas, NumPy)

ML Libraries: Scikit-Learn, XGBoost

Algorithms: Random Forest Classifier, AdaBoost, Gradient Boosting Machine (GBM)


🏠 **2. California Housing Price Regression**

Keywords - Regression Analysis, XGBoost, Stacking, Feature Engineering, Hyperparameter Tuning

Project Overview -
A predictive modeling project aimed at estimating median house values across California districts. 
The project focuses on handling non-linear spatial data and skewed distributions using advanced Boosting techniques and Weighted Ensembles.

Key Features -

a. Gradient Boosting (XGBoost/CatBoost): Implements state-of-the-art boosting algorithms to handle non-linear relationships between location (Lat/Long) and price.

b. Hyperparameter Optimization: Uses GridSearchCV and RandomizedSearchCV to fine-tune learning rates, tree depth, and subsampling ratios.

c. Ensemble Stacking: Combines multiple base learners (Linear Regression, Ridge, and Decision Trees) into a meta-regressor for a "Best-of-All" prediction.

d. Evaluation: Optimized for Root Mean Squared Error (RMSE) and $R^2$ Score to ensure high predictive power.

Technical Stack
Language: Python (Matplotlib, Seaborn)

ML Libraries: Scikit-Learn, XGBoost, CatBoost

Algorithms: Random Forest Regressor, XGBRegressor, StackingRegressor
