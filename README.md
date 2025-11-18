# Loan Default Classifier – Machine Learning System

## Overview
This repository contains a machine learning system designed to estimate the probability of loan default for individual applicants.
The solution provides a data-driven approach to credit risk assessment, supporting decision processes such as loan approval, risk segmentation, and portfolio optimization.

The project includes all core components of an end-to-end ML workflow: data preparation, feature engineering, model training, validation, and reporting.

## Business Context
Credit institutions process large volumes of loan applications and require accurate tools to identify applicants with an elevated probability of delinquency.
A predictive model for default risk enables:

- Improved risk-adjusted pricing
- Reduction of non-performing loans
- Support to underwriting and credit policy decisions
- More efficient allocation of credit limits

This system is designed to integrate into existing analytical pipelines or support credit risk teams in developing decision frameworks.

## Project Objectives
- Develop a binary classification model to estimate default risk with robust predictive performance.
- Build a structured preprocessing pipeline for missing values, outliers, and categorical variables.
- Engineer risk-relevant features to improve model accuracy and interpretability.
- Evaluate multiple model families, comparing baseline and advanced approaches.
- Produce risk-oriented insights, including threshold recommendations and feature importance.
- Ensure reproducibility and clarity through a modular and maintainable project structure.

## Methodology

### Data Preparation & Feature Engineering
- Missing value imputation
- Outlier handling
- Categorical encoding (one-hot or target-based)
- Creation of financial ratios and aggregated variables
- Class imbalance management via model weighting strategies

### Modeling Approaches
Two families of models are implemented:

**1. Baseline Model**  
- Logistic Regression for interpretability and as a reference benchmark.

**2. Gradient Boosting Models**  
- LightGBM, XGBoost, or CatBoost, selected for their ability to capture non-linear relationships and interaction effects.

### Evaluation Metrics
- ROC AUC
- Precision–Recall AUC
- Confusion Matrix and optimized decision threshold
- Feature importance (SHAP optional)

The evaluation framework emphasizes early identification of high-risk applicants while preserving acceptable approval rates.

## Data Source

This project uses the *Home Credit Default Risk* dataset, originally released as part of a Kaggle competition.

Dataset page:  
https://www.kaggle.com/competitions/home-credit-default-risk/data

To access the dataset you must:

1. Create a Kaggle account  
2. Accept the competition rules  
3. Download the files manually or via the Kaggle API  
4. Place all CSV files inside the following directory:

```
data/raw/
```

The dataset is not included in this repository to comply with licensing and distribution restrictions.  
Only the directory structure is provided to enable correct integration with the project’s data loading pipeline.

## How to Run

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Add raw data
Place the dataset files into:

```
data/raw/
```

### 3. Execute the workflow
- Run the Jupyter notebooks in order
  or
- Use the modular functions inside `src/` to integrate preprocessing and modeling steps into your environment.

## Results Documentation
Performance metrics, model comparisons, and calibration analyses will be documented in:

- reports/results.md
- reports/figures/ (ROC curves, PR curves, calibration plots)

Metrics include validation ROC AUC, threshold-based performance, and recommended cutoffs for specific risk policies.

## Future Enhancements
- Unified training pipeline (`train.py`)
- Model calibration (Platt scaling, isotonic regression)
- Drift monitoring and model stability tracking
- Optional containerization (Docker)
- Integration with a scoring API (FastAPI)

## Compliance
No proprietary data is included in this repository.
All processing components are adaptable to different datasets and risk environments.
