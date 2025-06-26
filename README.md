# Improvement-Plan-with-Six-Sigma-in-the-ArcelorMittal-Oxygen-Plant-Mexico

## Overview

This repository contains Python tools for Six Sigma analysis and statistical process control (SPC) specifically designed for the ArcelorMittal Oxygen Plant improvement plan. The tools provide comprehensive analysis capabilities including X-bar and R control charts, process capability analysis, and Gage R&R studies.

## Features

### 📊 Statistical Process Control (SPC)
- **X-bar Chart**: Monitors process central tendency
- **R Chart**: Monitors process variability
- **Control Limits**: Calculated using industry-standard constants (A2, d3, d4)

### 📈 Process Capability Analysis
- **Process Capability Indices**: Cp, Cpu, Cpl, Cpk
- **Process Statistics**: Mean, Standard Deviation, 6σ variation, 3σ limits
- **Specification Limits**: USL, LSL, and tolerance calculations

### 🔍 Gage R&R Analysis
- **Repeatability**: Equipment variation assessment
- **Reproducibility**: Operator variation assessment
- **GRR**: Combined gage repeatability and reproducibility
- **Part Variation (PV)**: Component variation analysis
- **Total Variation (VT)**: Overall process variation
- **NDC**: Number of Distinct Categories
- **Percent Variation**: Breakdown of variation sources

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/dianadeliz/Improvement-Plan-with-Six-Sigma-in-the-ArcelorMittal-Oxygen-Plant-Mexico.git
   cd Improvement-Plan-with-Six-Sigma-in-the-ArcelorMittal-Oxygen-Plant-Mexico
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Analysis

Execute the main analysis script:
```bash
python xrchart.py
```

### Output

The script generates:
1. **Process Capability Analysis**: Detailed statistics and capability indices
2. **X-bar Chart**: Visual representation of process central tendency
3. **R Chart**: Visual representation of process variability
4. **Gage R&R Analysis**: Comprehensive measurement system analysis

### Sample Output

```
============================================================
PROCESS CAPABILITY ANALYSIS
============================================================
Media (Mean)	99.566667
Standard Deviation (σ)	0.083503
Real Variation (6σ)	0.501016
3σ Limit	0.250508
USL (LCS / ES)	99.6714571
LSL (LCI / EI)	99.4632095
Tolerance (USL - LSL)	0.2082476
Cp	0.42335797
Cpu / Cpk (Upper)	0.42072542
Cpk (min of Cpu, Cpl)	0.42599052
============================================================

============================================================
GAGE R&R ANALYSIS
============================================================
Average Range (R̄):	0.1067
Range of Means (X_diff):	0.1000
Average Range of Parts (R_promedio):	0.0400
Repeatability (Repet):	0.0631
Reproducibility (VO):	0.0497
GRR:	0.0803
Part Variation (PV):	0.0161
Total Variation (VT):	0.0819
NDC:	0.2827
Repeatability %: 77.05%
Reproducibility %: 60.68%
GRR %: 98.05%
Part Variation %: 19.66%
============================================================
```

## Technical Details

### Constants Used
- **A2 = 0.58**: For n = 5 (sample size)
- **d3 = 0**: For n = 5
- **d4 = 2.11**: For n = 5
- **K1 = 0.5908**: Gage R&R constant
- **K2 = 0.5231**: Gage R&R constant
- **K3 = 0.403**: Gage R&R constant

### Data Structure
The analysis uses sample data with:
- **21 subgroups** of measurements
- **5 samples** per subgroup
- **3 operators** for Gage R&R analysis
- **5 parts** for measurement system evaluation

### Formulas

#### Process Capability
- **Cp = (USL - LSL) / (6σ)**
- **Cpu = (USL - μ) / (3σ)**
- **Cpl = (μ - LSL) / (3σ)**
- **Cpk = min(Cpu, Cpl)**

#### Gage R&R
- **Repeatability = K1 × R̄**
- **Reproducibility = √[(X_diff × K2)² - (Repeatability²/nr)]**
- **GRR = √(Repeatability² + Reproducibility²)**
- **PV = R_promedio × K3**
- **VT = √(GRR² + PV²)**
- **NDC = 1.41 × (PV/GRR)**

## Project Structure

```
├── xrchart.py          # Main analysis script
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Dependencies

- **matplotlib**: For chart generation and visualization
- **pandas**: For data manipulation and analysis
- **numpy**: For numerical computations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is part of the ArcelorMittal Oxygen Plant improvement initiative.

## Contact

For questions or support regarding this Six Sigma analysis tool, please contact the project maintainers.

---

**Note**: This tool is specifically designed for Six Sigma analysis in manufacturing environments and follows industry-standard methodologies for statistical process control and measurement system analysis.