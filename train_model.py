import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

# 1. Load the processed dataset
try:
    df = pd.read_csv('data/final_laptop_data.csv')
except FileNotFoundError:
    # If the combined folder data isn't generated yet, fallback to reading raw data
    df = pd.read_csv('data/laptop_data.csv')

# Ensure target transformation column exists
X = df.drop(columns=['Price'])
y = np.log(df['Price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=2)

# 2. Setup the Pipeline Transformers matching index positions
step1 = ColumnTransformer(transformers=[
    ('col_tnf', OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore'), [0, 1, 7, 10, 11])
], remainder='passthrough')

step2 = RandomForestRegressor(n_estimators=100, random_state=3, max_samples=0.5, max_features=0.75, max_depth=15)

# Build a complete scikit-learn pipeline object
pipe = Pipeline([
    ('step1', step1),
    ('step2', step2)
])

pipe.fit(X_train, y_train)

# 3. Evaluate Performance
y_pred = pipe.predict(X_test)
print(f"Model Accuracy (R²): {r2_score(y_test, y_pred):.3f}")

# 4. Save the full pipeline object safely using standard binary pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(pipe, f, protocol=4)

print("\n Random Forest Pipeline Trained & Saved Successfully as model.pkl!")


























