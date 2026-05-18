# Statistical Characterization of a Piecewise Nonlinear Transformation of a Laplacian Distribution

**Author:** Parth Dineshbhai Pandya  
**Institution:** Tennessee State University — Department of Electrical & Computer Engineering  
**Course:** Probability & Statistics / Stochastic Systems  
**Email:** ppandya@my.tnstate.edu

---

## Overview

This project presents a detailed analytical and simulation-based study of a **nonlinear transformation** applied to a Laplacian (double-exponential) random variable.

The input random variable **X** follows a Laplacian distribution:

```
fX(x) = (1/2) * e^(−|x|),   −∞ < x < ∞
```

A **piecewise transformation** is applied:

```
Y = g(X) = { X,    if X ≥ 0
           { 2X²,  if X < 0
```

The project derives the output PDF analytically, validates it via Monte Carlo simulation with **1,000,000 samples**, and compares theoretical vs. empirical statistics.

---

## Table of Contents

- [Theory](#theory)
- [Results](#results)
- [Simulation](#simulation)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Usage](#usage)
- [References](#references)

---

## Theory

### CDF of the Laplacian Input X

```
FX(x) = { (1/2) * e^x,          x < 0
         { 1 − (1/2) * e^(−x),  x ≥ 0
```

### Inverse CDF Sampling (Generating X from U ~ Uniform(0,1))

```
X = { ln(2U),          0 < U < 0.5
    { −ln(2(1 − U)),   0.5 ≤ U < 1
```

This method is **exact**, **efficient** (no rejection sampling), and **scalable** for large simulations.

### PDF of the Transformed Variable Y

Using the function-of-a-random-variable formula across both branches:

**Branch 1** (X ≥ 0, Y = X):
```
contribution = (1/2) * e^(−y),   y ≥ 0
```

**Branch 2** (X < 0, Y = 2X²):
```
contribution = (1 / (4√(2y))) * e^(−√(y/2)),   y > 0
```

**Final PDF:**
```
fY(y) = (1/2)*e^(−y) + (1/(4√(2y)))*e^(−√(y/2)),   y > 0
        0,                                             y ≤ 0
```

### Moments of Y

| Moment | Value |
|--------|-------|
| Mean E[Y] | **2.5** |
| Variance Var(Y) | **42.75** |
| Standard Deviation σY | **≈ 6.5383** |

---

## Results

### Statistical Comparison: Simulation vs. Theory

| Variable | Sample Mean | Theory Mean | Sample Std | Theory Std |
|----------|------------|------------|-----------|-----------|
| U ~ Uniform(0,1) | ~0.500 | 0.500 | ~0.288 | 0.2887 |
| X ~ Laplacian | ~0 | 0 | ~1.414 | 1.4142 |
| Y (transformed) | ~2.5 | 2.5 | ~6.55 | 6.538 |

> ✅ **All simulated statistics match theoretical values**, confirming the correctness of the analytical derivations.

### Key Observations

- **U (Uniform):** Flat histogram across [0, 1], matching fU(u) = 1
- **X (Laplacian):** Symmetric exponential decay with peak at fX(0) = 0.5
- **Y (Transformed):**
  - Sharp peak near zero (singularity from the 1/√y term)
  - Long right tail (heavy-tailed behavior inherited from Laplacian)
  - Strictly non-negative support
  - Strong match with theoretical PDF fY(y)

### Integral Verification

```
∫₀^∞ fY(y) dy = 1.000000   ✓
```

### Plots

The simulation generates three side-by-side histogram panels:

| Plot | Description |
|------|-------------|
| **Fig. 1** | Histogram of U ~ Uniform(0,1) vs. fU(u) = 1 |
| **Fig. 2** | Histogram of X (Laplacian) vs. fX(x) = ½e^(−\|x\|) |
| **Fig. 3** | Histogram of Y vs. theoretical fY(y) |

All plots are saved to `simulation_results.png` upon running the script.

---

## Simulation

### Setup

| Parameter | Value |
|-----------|-------|
| Samples N | 1,000,000 |
| Random seed | 42 (reproducible) |
| Tools | NumPy, Matplotlib, SciPy |
| Method | Inverse Transform Sampling |

### Algorithm

```
1. Generate U ~ Uniform(0, 1)
2. Map U → X using inverse CDF:
      if U < 0.5:  X = ln(2U)
      else:        X = −ln(2(1−U))
3. Apply piecewise transformation:
      if X ≥ 0:   Y = X
      else:        Y = 2X²
4. Plot and compare histograms against theoretical PDFs
5. Print summary statistics
```

---

## Repository Structure

```
laplacian-transformation/
├── simulation.py           # Full Python simulation script
└── README.md               # Project documentation
```

---

## Requirements

- Python 3.8+
- NumPy
- Matplotlib
- SciPy

Install dependencies:

```bash
pip install numpy matplotlib scipy
```

---

## Usage

```bash
python simulation.py
```

**Expected output:**
```
Integral of f_Y = 1.000000
U: mean=0.5000, std=0.2887
X: mean=0.0001, std=1.4142
Y: mean=2.5003, std=6.5383
```

The plot is saved as `simulation_results.png` in the working directory.

---

## References

1. A. Papoulis and S. U. Pillai, *Probability, Random Variables, and Stochastic Processes*, 4th ed., McGraw-Hill, 2002.
2. H. Stark and J. W. Woods, *Probability and Random Processes with Applications to Signal Processing*, 4th ed., Prentice Hall, 2012.
3. S. M. Ross, *A First Course in Probability*, 10th ed., Pearson, 2019.
4. L. Devroye, *Non-Uniform Random Variate Generation*, Springer, 1986.
5. R. Y. Rubinstein and D. P. Kroese, *Simulation and the Monte Carlo Method*, 3rd ed., Wiley, 2017.
6. S. Mallat, *A Wavelet Tour of Signal Processing*, 3rd ed., Academic Press, 2009.
7. NumPy Developers, "NumPy Reference Guide." https://numpy.org
8. SciPy Developers, "SciPy Reference Guide." https://scipy.org