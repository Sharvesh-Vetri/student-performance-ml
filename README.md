# Student Performance ML

This repository contains scripts and notebooks for a student performance machine learning project. The project runs all steps via a Windows batch file `run.bat`.

## Project Structure

- `data/` - raw CSV files (`student-mat.csv`, `student-por.csv`)
- `scripts/` - Python scripts: `cleaning.py`, `logistic_regression.py`, `random_forest.py`, `model_comparison.py`
- `notebooks/` - exploratory and model notebooks
- `output/` - generated outputs (plots, model files, metrics)
- `requirements.txt` - Python dependencies
- `run.bat` - Windows batch to run the full pipeline

## Quick Setup (PowerShell)

Run these commands from the project root in PowerShell:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the pipeline:

```
.\run.bat
```


