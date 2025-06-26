import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your actual data (assuming it's already in a DataFrame named df)
# For this example, we're reconstructing it manually
data = {
    "Subgroup": list(range(1, 22)),
    "Sample 1": [99.5, 99.5, 99.5, 99.7, 99.5, 99.7, 99.5, 99.5, 99.5, 99.7, 99.6, 99.5, 99.5, 99.5, 99.5, 99.5, 99.5, 99.5, 99.5, 99.6, 99.6],
    "Sample 2": [99.6, 99.4, 99.6, 99.6, 99.5, 99.6, 99.6, 99.4, 99.6, 99.7, 99.5, 99.5, 99.5, 99.6, 99.6, 99.5, 99.6, 99.5, 99.4, 99.6, 99.7],
    "Sample 3": [99.7, 99.6, 99.6, 99.5, 99.5, 99.6, 99.7, 99.4, 99.6, 99.6, 99.6, 99.6, 99.6, 99.7, 99.7, 99.5, 99.7, 99.5, 99.6, 99.5, 99.5],
    "sample 4": [99.6, 99.6, 99.7, 99.5, 99.5, 99.6, 99.5, 99.5, 99.7, 99.5, 99.6, 99.7, 99.7, 99.6, 99.6, 99.5, 99.5, 99.5, 99.6, 99.4, 99.6],
    "Sample 5": [99.5, 99.5, 99.7, 99.6, 99.6, 99.6, 99.6, 99.5, 99.6, 99.6, 99.6, 99.5, 99.6, 99.7, 99.5, 99.6, 99.5, 99.6, 99.7, 99.6, 99.5]
}
df = pd.DataFrame(data)

# Calculate means and ranges
df['Mean'] = df.iloc[:, 1:6].mean(axis=1)
df['Range'] = df.iloc[:, 1:6].max(axis=1) - df.iloc[:, 1:6].min(axis=1)

# Constants for n = 5
A2 = 0.58
d3 = 0
d4 = 2.11

# Compute control limits for X-bar chart
X_bar_bar = df['Mean'].mean()
R_bar = df['Range'].mean()
X_LCL = X_bar_bar - A2 * R_bar
X_UCL = X_bar_bar + A2 * R_bar

# Process Capability Calculations
# Estimate standard deviation from R-bar
sigma_hat = R_bar / d4

# Use control limits as USL and LSL
USL = X_UCL
LSL = X_LCL

# Calculate process capability metrics
mean_process = X_bar_bar
std_dev = sigma_hat
real_variation_6sigma = 6 * std_dev
sigma_3_limit = 3 * std_dev
tolerance = USL - LSL

# Process Capability Indices
Cp = tolerance / real_variation_6sigma
Cpu = (USL - mean_process) / (3 * std_dev)
Cpl = (mean_process - LSL) / (3 * std_dev)
Cpk = min(Cpu, Cpl)

# Display the results
print("=" * 60)
print("PROCESS CAPABILITY ANALYSIS")
print("=" * 60)
print(f"Mean\t{mean_process:.7f}")
print(f"Standard Deviation (σ)\t{std_dev:.9f}")
print(f"Real Variation (6σ)\t{real_variation_6sigma:.9f}")
print(f"3σ Limit\t{sigma_3_limit:.8f}")
print(f"USL (Upper Spec Limit)\t{USL:.7f}")
print(f"LSL (Lower Spec Limit)\t{LSL:.7f}")
print(f"Tolerance (USL - LSL)\t{tolerance:.7f}")
print(f"Cp\t{Cp:.8f}")
print(f"Cpu / Cpk (Upper)\t{Cpu:.8f}")
print(f"Cpk (min of Cpu, Cpl)\t{Cpk:.8f}")
print("=" * 60)

# Plot X̄ chart
plt.figure(figsize=(10, 5))
plt.plot(df['Subgroup'], df['Mean'], marker='o', label='mean', color='blue')
plt.axhline(y=X_UCL, color='darkorange', linestyle='-', linewidth=2, label='UCL X')  # Upper Control Limit
plt.axhline(y=X_bar_bar, color='gray', linestyle='-', linewidth=2, label='CL X')     # Center Line
plt.axhline(y=X_LCL, color='gold', linestyle='-', linewidth=2, label='LCL X')       # Lower Control Limit
plt.title('X CHART', fontsize=14)
plt.xlabel('Subgroup')
plt.ylabel('Mean Value')
plt.xticks(df['Subgroup'])  # Use actual subgroup numbers on x-axis
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Use previously calculated values
R_bar = df['Range'].mean()
R_LCL = d3 * R_bar
R_UCL = d4 * R_bar

# Plot R Chart
plt.figure(figsize=(10, 5))
plt.plot(df['Subgroup'], df['Range'], marker='o', color='blue', label='range')
plt.axhline(y=R_UCL, color='darkorange', linestyle='-', linewidth=2, label='UCL R')  # UCL
plt.axhline(y=R_bar, color='gray', linestyle='-', linewidth=2, label='CL R')         # CL
plt.axhline(y=R_LCL, color='gold', linestyle='-', linewidth=2, label='LCL R')        # LCL
plt.title('R CHART', fontsize=14)
plt.xlabel('Subgroup')
plt.ylabel('Range')
plt.xticks(df['Subgroup'])  # Use subgroup numbers as x-axis labels
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Gage R&R Data
import numpy as np

# Operator data
operator_ranges = [0.12, 0.10, 0.10]  # Operator 1, 2, 3 average ranges
operator_averages = [99.58, 99.52, 99.60]

# Piece averages
piece_averages = [99.54, 99.54, 99.58, 99.56, 99.58]

# Constants
K1 = 0.5908
K2 = 0.5231
K3 = 0.403
n = 5  # pieces
r = 3  # repetitions
nr = n * r

# 1.Average Range (R̄)
R_bar = np.mean(operator_ranges)

# 2.Range of Means (X_diff)
X_diff = max(operator_averages) - min(operator_averages)

# 3.Average Range of Parts
R_promedio = max(piece_averages) - min(piece_averages)

# 4. Repeatability (Repet)
Repet = K1 * R_bar

# 5. Reproducibility (VO)
VO = np.sqrt((X_diff * K2) ** 2 - (Repet ** 2) / nr)

# 6. GRR (Gage R&R)
GRR = np.sqrt(Repet ** 2 + VO ** 2)

# 7. PV (Part Variation)
PV = R_promedio * K3

# 8. VT (Total Variation)
VT = np.sqrt(GRR ** 2 + PV ** 2)

# 9. NDC (Number of Distinct Categories)
NDC = 1.41 * (PV / GRR) if GRR != 0 else np.nan

# Percent variation calculations
repeatability_percent = (Repet / VT) * 100 if VT != 0 else np.nan
reproducibility_percent = (VO / VT) * 100 if VT != 0 else np.nan
grr_percent = (GRR / VT) * 100 if VT != 0 else np.nan
pv_percent = (PV / VT) * 100 if VT != 0 else np.nan

print("\n" + "=" * 60)
print("GAGE R&R ANALYSIS")
print("=" * 60)
print(f"Average Range (R̄):\t{R_bar:.4f}")
print(f"Range of Means (X_diff):\t{X_diff:.4f}")
print(f"Average Range of Parts (R_promedio):\t{R_promedio:.4f}")
print(f"Repeatability (Repet):\t{Repet:.4f}")
print(f"Reproducibility (VO):\t{VO:.4f}")
print(f"GRR:\t{GRR:.4f}")
print(f"Part Variation (PV):\t{PV:.4f}")
print(f"Total Variation (VT):\t{VT:.4f}")
print(f"NDC:\t{NDC:.4f}")
print(f"Repeatability %: {repeatability_percent:.3f}%")
print(f"Reproducibility %: {reproducibility_percent:.3f}%")
print(f"GRR %: {grr_percent:.3f}%")
print(f"Part Variation %: {pv_percent:.3f}%")
print("=" * 60)