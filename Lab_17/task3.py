'''Clean and preprocess IoT temperature and humidity logs.
Instructions:
- Handle missing values using forward fill.
- Remove sensor drift (apply rolling mean).
- Normalize readings using standard scaling.
- Encode categorical sensor IDs.'''
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
df = pd.read_csv("iot_sensor.csv")

# -----------------------------
# 1. Handle missing values (Forward Fill)
# -----------------------------
df = df.fillna(method="ffill")

# -----------------------------
# 2. Remove sensor drift using rolling mean (window = 3)
# -----------------------------
df["temperature_smooth"] = df["temperature"].rolling(window=3, min_periods=1).mean()
df["humidity_smooth"] = df["humidity"].rolling(window=3, min_periods=1).mean()

# -----------------------------
# 3. Normalize values (Standard Scaling)
# -----------------------------
scaler = StandardScaler()

df[["temperature_scaled", "humidity_scaled"]] = scaler.fit_transform(
    df[["temperature_smooth", "humidity_smooth"]]
)

# -----------------------------
# 4. Encode categorical sensor IDs
# -----------------------------
encoder = LabelEncoder()
df["sensor_id_encoded"] = encoder.fit_transform(df["sensor_id"])

# -----------------------------
# Save cleaned output
# -----------------------------
df.to_csv("iot_sensor_cleaned.csv", index=False)

print("Cleaning complete! File saved as iot_sensor_cleaned.csv")