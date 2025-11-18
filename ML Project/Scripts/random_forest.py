# ================================================================
# random_forest.py : Train Random Forest model
# ================================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

DATASET = "output/cleaned_student-mat.csv"   # Change when needed
OUTPUT_PATH = "output/"

os.makedirs(OUTPUT_PATH, exist_ok=True)

print(f"Loading dataset: {DATASET}")
df = pd.read_csv(DATASET)

# Target
y = df["passed"]

# Drop leakage (G2, G3)
drops = ["passed", "G2", "G3"]
drops = [c for c in drops if c in df.columns]
X = df.drop(columns=drops)

# Encode categorical features
X = pd.get_dummies(X, drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Random Forest model
rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    min_samples_split=2,
    random_state=42
)
rf.fit(X_train, y_train)

# Predictions
y_pred = rf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Save report
with open(OUTPUT_PATH + "rf_results.txt", "w") as f:
    f.write(f"Dataset: {DATASET}\n")
    f.write(f"Accuracy: {acc}\n\n")
    f.write(report)

# Save model
joblib.dump(rf, OUTPUT_PATH + "rf_model.joblib")

print(f"Random Forest complete. Accuracy = {acc}")
print("Saved: rf_results.txt, rf_model.joblib")
