@echo off
setlocal enabledelayedexpansion

echo.
echo ========================================
echo Installing dependencies...
echo ========================================
py -m pip install -r requirements.txt
if !ERRORLEVEL! NEQ 0 (
	echo.
	echo ERROR: Failed to install dependencies.
	exit /b 1
)

echo.
echo ========================================
echo Running cleaning script...
echo ========================================
py scripts\cleaning.py
if !ERRORLEVEL! NEQ 0 (
	echo.
	echo ERROR: cleaning.py failed.
	exit /b 1
)

echo.
echo ========================================
echo Running Logistic Regression model...
echo ========================================
py scripts\logistic_regression.py
if !ERRORLEVEL! NEQ 0 (
	echo.
	echo ERROR: logistic_regression.py failed.
	exit /b 1
)

echo.
echo ========================================
echo Running Random Forest model...
echo ========================================
py scripts\random_forest.py
if !ERRORLEVEL! NEQ 0 (
	echo.
	echo ERROR: random_forest.py failed.
	exit /b 1
)

echo.
echo ========================================
echo Running model comparison...
echo ========================================
py scripts\model_comparison.py
if !ERRORLEVEL! NEQ 0 (
	echo.
	echo ERROR: model_comparison.py failed.
	exit /b 1
)

echo.
echo ========================================
echo Pipeline completed successfully!
echo ========================================
echo.
endlocal
exit /b 0