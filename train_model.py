import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# ----------------------------
# Load Final Dataset
# ----------------------------
df = pd.read_csv("data/final_laptop_data.csv")

# Features
X = df[[
    "Company",
    "TypeName",
    "Ram",
    "Weight",
    "Inches",
    "CPU Brand",
    "GPU Brand",
    "SSD",
    "HDD",
    "OS"
]]

# Target
y = df["Price"]

# Categorical columns
categorical = [
    "Company",
    "TypeName",
    "CPU Brand",
    "GPU Brand",
    "OS"
]

# Numerical columns
numerical = [
    "Ram",
    "Weight",
    "Inches",
    "SSD",
    "HDD"
]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ("num", "passthrough", numerical)
    ]
)

# Model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ))
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
score = r2_score(y_test, predictions)

print("Model Accuracy (R²):", round(score, 3))

# Save model
joblib.dump(model, "model.pkl")

print("\n Random Forest Model Trained Successfully!")
print("model.pkl Updated")