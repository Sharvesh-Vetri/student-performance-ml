# 🎓 Student Performance Prediction (Machine Learning Project)

This project predicts whether a student will **pass or fail** based on demographic, social, and academic factors from the UCI Student Performance dataset.  

Two machine learning models are implemented:

- **Logistic Regression**
- **Random Forest Classifier**

The project is fully **reproducible**, **automated**, and uses a clean folder structure with separate scripts for data cleaning, modeling, and evaluation.

---

# 📁 Project Structure

student-performance-ml/
│
├── data/ # Raw datasets
│ ├── student-mat.csv
│ └── student-por.csv
│
├── output/ # Generated outputs (auto-created)
│ ├── cleaned_student-mat.csv
│ ├── cleaned_student-por.csv
│ ├── lr_results.txt
│ ├── rf_results.txt
│ ├── comparison_results.txt
│ ├── logreg_model.joblib
│ └── rf_model.joblib
│
├── scripts/ # Executable pipeline scripts
│ ├── cleaning.py
│ ├── logistic_regression.py
│ ├── random_forest.py
│ └── model_comparison.py
│
├── notebooks/ # Jupyter notebooks for analysis
│ ├── EDA_and_Cleaning.ipynb
│ ├── LogReg_model.ipynb
│ ├── RandomForest_model.ipynb
│ └── Model_comparisson.ipynb
│
├── requirements.txt # Dependencies
├── run.sh
└── README.md

---

# 🚀 How to Run the Entire Pipeline

The entire project runs automatically using **one command**.

## **Mac/Linux**
```bash
chmod +x run.sh
./run.sh

