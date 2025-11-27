#!/bin/bash

echo "========================================"
echo "   Student Performance ML Pipeline"
echo "========================================"

echo ""
echo ">>> Step 1: Installing Dependencies"
pip install -r requirements.txt

echo ""
echo ">>> Step 2: Running Data Cleaning"
python scripts/cleaning.py

echo ""
echo ">>> Step 3: Training Logistic Regression"
python scripts/logistic_regression.py

echo ""
echo ">>> Step 4: Training Random Forest"
python scripts/random_forest.py

echo ""
echo ">>> Step 5: Running Model Comparison"
python scripts/model_comparison.py

echo ""
echo "========================================"
echo " Pipeline Completed Successfully"
echo " Output files saved in /output/"
echo "========================================"
