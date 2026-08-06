# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts the price of used cars using Machine Learning algorithms. The dataset was cleaned, preprocessed, and analyzed before training prediction models. The project compares the performance of Linear Regression and Random Forest Regression models.

---

## 🎯 Objective

The objective of this project is to build a machine learning model that can predict the selling price of a used car based on features such as:

- Manufacturing Year
- Body Type
- Transmission Type
- Fuel Type
- Kilometers Driven
- Owner Type

---

## 📂 Dataset

**Dataset Name:** Cars Details Dataset

Selected Features:

- myear
- body
- transmission
- fuel
- km
- owner_type
- listed_price (Target Variable)

---

## 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- VS Code

---

## ⚙ Project Workflow

### 1. Data Loading

- Loaded the dataset using Pandas.

### 2. Data Cleaning

- Removed missing values.
- Selected important features.
- Converted price values into numeric format.

### 3. Data Preprocessing

- Label Encoding for categorical columns.
- Train-Test Split (80% Training, 20% Testing)

### 4. Machine Learning Models

- Linear Regression
- Random Forest Regressor

### 5. Model Evaluation

The models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

## 📊 Model Performance

### Linear Regression

- R² Score: **0.3393**
- MAE: **382389.98**
- RMSE: **830092.31**

### Random Forest Regressor

- R² Score: **-2.2613**
- MAE: **335086.70**
- RMSE: **1844191.07**

---

## 📈 Output Graphs

### Graph 1

Actual Price vs Predicted Price (Linear Regression)

**File:** output1.png

---

### Graph 2

Actual Price vs Predicted Price (Random Forest)

**File:** output2.png

---

### Graph 3

Feature Importance Graph

**File:** output3.png

---

## 📁 Project Structure

```
DataScience-Task3-CarPricePrediction
│
├── car_price_prediction.py
├── cars_data_clean.csv
├── cars_details_merges.csv
├── feature_dictionary.csv
├── output1.png
├── output2.png
├── output3.png
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Run the Project

```bash
python car_price_prediction.py
```

---

## 📚 Learning Outcomes

Through this project, I learned:

- Data Cleaning
- Feature Selection
- Label Encoding
- Train-Test Split
- Linear Regression
- Random Forest Regression
- Model Evaluation
- Data Visualization
- Machine Learning Workflow

---

## ✅ Conclusion

This project demonstrates how Machine Learning can be used to predict used car prices based on important vehicle features. The complete workflow includes data preprocessing, model building, evaluation, and visualization. It provides hands-on experience in implementing regression algorithms using Python and Scikit-learn.

---

## 👨‍💻 Author

**L. Bala Sai**

Oasis Infobyte Internship

Task 3 – Car Price Prediction with Machine Learning