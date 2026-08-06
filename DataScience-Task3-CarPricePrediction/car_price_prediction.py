import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("cars_data_clean.csv")

# Select Required Columns
car_df = df[['myear',
             'body',
             'transmission',
             'fuel',
             'km',
             'owner_type',
             'listed_price']].copy()

print(car_df.head())

print("\nShape:")
print(car_df.shape)

print("\nMissing Values:")
print(car_df.isnull().sum())
# Remove Missing Values
car_df = car_df.dropna()

print("\nShape After Cleaning:")
print(car_df.shape)
from sklearn.preprocessing import LabelEncoder

# Label Encoding
encoder = LabelEncoder()

car_df["body"] = encoder.fit_transform(car_df["body"])
car_df["transmission"] = encoder.fit_transform(car_df["transmission"])
car_df["fuel"] = encoder.fit_transform(car_df["fuel"])
car_df["owner_type"] = encoder.fit_transform(car_df["owner_type"])

print("\nEncoded Dataset:")
print(car_df.head())
from sklearn.model_selection import train_test_split

# Features and Target
X = car_df.drop("listed_price", axis=1)
y = car_df["listed_price"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTrain Shape:", X_train.shape)
print("Test Shape:", X_test.shape)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# Train Linear Regression Model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predictions
y_pred_lr = lr_model.predict(X_test)

# Evaluation
print("\n========== Linear Regression ==========")
print("R2 Score :", round(r2_score(y_test, y_pred_lr), 4))
print("MAE      :", round(mean_absolute_error(y_test, y_pred_lr), 2))
print("RMSE     :", round(np.sqrt(mean_squared_error(y_test, y_pred_lr)), 2))
from sklearn.ensemble import RandomForestRegressor

# Train Random Forest Model
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

# Predictions
y_pred_rf = rf_model.predict(X_test)

# Evaluation
print("\n========== Random Forest ==========")
print("R2 Score :", round(r2_score(y_test, y_pred_rf), 4))
print("MAE      :", round(mean_absolute_error(y_test, y_pred_rf), 2))
print("RMSE     :", round(np.sqrt(mean_squared_error(y_test, y_pred_rf)), 2))

plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred_lr, alpha=0.5)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Linear Regression Prediction")
plt.savefig("output1.png")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred_rf, alpha=0.5)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Random Forest Prediction")
plt.savefig("output2.png")
plt.show()

importance = rf_model.feature_importances_

plt.figure(figsize=(8,6))
plt.bar(X.columns, importance)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output3.png")
plt.show()