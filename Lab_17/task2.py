'''
Generate a code that satisfies the following requirements:
- Handle missing values in closing_price and volume.
- Create lag features (1-day, 7-day returns).
- Normalize volume column using log-scaling.
- Detect outliers in closing_price using IQR method.

'''
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("financial_data.csv")
# -----------------------------------------
# 1. HANDLE MISSING VALUES
# -----------------------------------------

# Fill missing closing_price with forward fill, then backward fill
df["closing_price"] = df["closing_price"].fillna(method="ffill").fillna(method="bfill")

# Fill missing volume with median
df["volume"] = df["volume"].fillna(df["volume"].median())

# -----------------------------------------
# 2. CREATE LAG FEATURES (1-day, 7-day returns)
# -----------------------------------------
df["return_1d"] = df["closing_price"].pct_change(1)
df["return_7d"] = df["closing_price"].pct_change(7)

# Handling NaN after pct_change
df[["return_1d", "return_7d"]] = df[["return_1d", "return_7d"]].fillna(0)

# -----------------------------------------
# 3. NORMALIZE VOLUME USING LOG-SCALING
# -----------------------------------------
df["volume_log"] = np.log1p(df["volume"])   # log(1 + volume)
# -----------------------------------------
# 4. OUTLIER DETECTION USING IQR (closing_price)
# -----------------------------------------
Q1 = df["closing_price"].quantile(0.25)
Q3 = df["closing_price"].quantile(0.75)
IQR = Q3 - Q1
# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Create an outlier flag column
df["closing_price_outlier"] = ((df["closing_price"] < lower_bound) |
                               (df["closing_price"] > upper_bound)).astype(int)
# -----------------------------------------
# 5. Save cleaned dataset
# -----------------------------------------
df.to_csv("financial_data_cleaned.csv", index=False)
print("Dataset cleaned successfully!")
