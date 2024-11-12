# RNA Structure Quality Assessment with Custom Coarse-Grained RMSD

## Project Overview
This project aims to assess the quality of RNA structure predictions by computing a custom coarse-grained Root Mean Square Deviation (RMSD) and comparing its correlation with three established metrics: **RMSD**, **MCQ** (Mean of Circular Quantities), and **TM-Score**. The goal is to identify which coarse-grained representation best correlates with these metrics, providing insights into the structural accuracy of predicted RNA models.

## Table of Contents
- [Background](#background)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Code Structure](#code-structure)
- [Usage](#usage)
- [Results](#results)
- [Limitations and Future Work](#limitations-and-future-work)
- [Contributors](#contributors)

## Background
In structural biology, accurately predicting RNA structures is essential for understanding their functions. Standard metrics such as RMSD, MCQ, and TM-Score are used to evaluate how well predicted structures align with native structures. This project develops a coarse-grained RMSD metric, considering selected atoms per nucleotide, and evaluates its effectiveness by comparing it with the established metrics. The comparison is based on **Spearman** and **Pearson** correlation coefficients.

## Dataset
The project uses datasets derived from the [RNA-Puzzles](https://github.com/RNA-Puzzles) community challenge:
- **Native Structures** (`NATIVE`): Reference RNA structures in `.pdb` format.
- **Predicted Structures** (`PREDS`): Predicted RNA structures from various models in `.pdb` format.
- **Metrics** (`SCORES`): Precomputed scores (RMSD, MCQ, and TM-Score) between native and predicted structures.

## Methodology
1. **Atom Selection for Coarse-Grained RMSD**:
   - We explore several atom representations per nucleotide (e.g., **P, C3', O5'**).
   - For each representation, we compute a custom RMSD.

2. **Structure Alignment**:
   - Predicted structures are aligned to native structures before computing RMSD to ensure accurate spatial comparison.

3. **Coarse-Grained RMSD Calculation**:
   - Using the selected atoms, we calculate RMSD for each predicted-native structure pair.

4. **Correlation Analysis**:
   - Correlate each custom RMSD representation with the three established metrics using Pearson and Spearman correlations.

## Code Structure
- `src/`: Contains the main Python code for the project.
  - `alignment.py`: Functions to align predicted structures with native structures.
  - `custom_rmsd.py`: Functions to compute coarse-grained RMSD based on different atom representations.
  - `correlation_analysis.py`: Code to compute Pearson and Spearman correlations between custom RMSD and given metrics.
- `data/`: Folder for dataset files (native structures, predictions, and scores).
- `results/`: Stores correlation results and analysis figures.
- `README.md`: Project documentation.
- `requirements.txt`: Python dependencies for the project.

## Usage
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
