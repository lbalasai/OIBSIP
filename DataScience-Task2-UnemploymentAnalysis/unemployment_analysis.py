import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# -----------------------------
# Average Unemployment Rate by State
# -----------------------------
plt.figure(figsize=(12, 6))

state_avg = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean().sort_values()

state_avg.plot(kind="bar", color="skyblue")

plt.title("Average Unemployment Rate by State")
plt.xlabel("State")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=90)

plt.tight_layout()
plt.savefig("output1.png", dpi=300, bbox_inches="tight")
plt.show()

# -----------------------------
# Monthly Unemployment Trend
# -----------------------------
plt.figure(figsize=(10, 5))

monthly = df.groupby("Date")["Estimated Unemployment Rate (%)"].mean()

plt.plot(monthly.index, monthly.values,
         marker="o",
         color="red")

plt.title("Monthly Unemployment Trend")
plt.xlabel("Date")
plt.ylabel("Average Unemployment Rate (%)")
plt.grid(True)

plt.tight_layout()
plt.savefig("output2.png", dpi=300, bbox_inches="tight")
plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8, 5))

numeric_df = df.select_dtypes(include=["number"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("output3.png", dpi=300, bbox_inches="tight")
plt.show()

print("\nAnalysis Completed Successfully!")