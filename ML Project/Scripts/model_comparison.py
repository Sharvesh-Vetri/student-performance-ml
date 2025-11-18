# ================================================================
# model_comparison.py : Compare LR and RF results
# ================================================================

import os

OUTPUT_PATH = "output/"
LR_FILE = OUTPUT_PATH + "lr_results.txt"
RF_FILE = OUTPUT_PATH + "rf_results.txt"

print("Reading model results...")

with open(LR_FILE, "r") as f:
    lr_text = f.read()

with open(RF_FILE, "r") as f:
    rf_text = f.read()

comparison_output = OUTPUT_PATH + "comparison_results.txt"

with open(comparison_output, "w") as f:
    f.write("========== LOGISTIC REGRESSION ==========\n")
    f.write(lr_text)
    f.write("\n\n========== RANDOM FOREST ==========\n")
    f.write(rf_text)

print("Comparison complete.")
print(f"Saved comparison to {comparison_output}")
