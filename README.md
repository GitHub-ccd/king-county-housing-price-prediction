# 🏡 King County Housing Price Prediction

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://king-county-housing-prediction.streamlit.app)
[![Portfolio Showcase](https://img.shields.io/badge/Portfolio-CCD_Portfolio-purple.svg)](https://github.com/GitHub-ccd/ccdportfolio)

> **Predictive real estate valuation model and interactive analytics web application for residential properties in Seattle & King County, Washington.**

---

## 📌 Project Overview & Backstory

Accurately evaluating residential property values is a cornerstone of real estate analytics, mortgage underwriting, and urban planning. Properties in King County, WA (which includes Seattle, Bellevue, and surrounding regions) display significant price variance driven by structural attributes, property grade, waterfront access, and hyper-local geographic factors.

This project was originally developed as a data science regression study and has been modernly refactored to incorporate advanced ensemble modeling (`LightGBM`), regularized linear algorithms (Ridge/Lasso), and a live interactive **Streamlit web application** for real-time price estimation.

---

## 🎯 Key Objectives

1. **Exploratory Data Analysis (EDA)**: Uncover the primary physical, temporal, and spatial drivers influencing house sales prices across 21,597 residential properties.
2. **Feature Engineering**: Address non-linearities via log transformations, engineer distance-to-center geo-spatial metrics, and eliminate multicollinearity through diagnostic VIF pruning.
3. **Multi-Model Benchmarking**: Compare classical Ordinary Least Squares (OLS) regression against Ridge, Lasso, and Gradient Boosted Decision Trees (`LightGBM`).
4. **Interactive Deployment**: Provide non-technical users and homebuyers with an intuitive Streamlit interface to estimate house prices interactively.

---

## 🏗️ Technical Architecture & Pipeline

```
├── data/
│   └── kc_house_data.csv        # King County housing sales dataset (~21,600 rows)
├── notebooks/
│   ├── student.ipynb            # Ingestion, EDA, missing value handling & distribution analysis
│   ├── modeling.ipynb           # Feature engineering, log transforms, OLS & LightGBM benchmarking
│   └── analysis.ipynb           # Model diagnostics, residual analysis & business takeaways
├── app.py                       # Lightweight Streamlit interactive web application
├── PORTFOLIO_HANDOFF.md         # Integration payload for ccdportfolio showcase
├── requirements.txt             # Project dependencies
└── README.md                    # Comprehensive documentation
```

### Pipeline Workflow:
1. **Data Preprocessing**: Outlier removal, missing value imputation, log-transforming skewed variables (`price`, `sqft_living`, `sqft_lot`).
2. **Feature Engineering**: 
   - Distance calculation to downtown Seattle coordinates.
   - Categorical one-hot encoding for `waterfront`, `view`, and `zipcode` groups.
   - Construction of physical ratio features (e.g., `sqft_living / sqft_lot`, `bed_to_bath_ratio`).
3. **Model Training & Evaluation**:
   - 5-Fold Cross-Validation across models.
   - Metrics: $R^2$, Root Mean Squared Error (RMSE), Mean Absolute Error (MAE).

---

## 📊 Model Performance & Benchmarks

| Model | $R^2$ Score | RMSE ($) | Key Advantages |
| :--- | :---: | :---: | :--- |
| **Baseline OLS (`Statsmodels`)** | 0.751 | ~$168,000 | Highly interpretable coefficients & statistical $p$-values |
| **Ridge Regression ($\alpha=1.0$)** | 0.753 | ~$167,200 | Penalizes large coefficients, handles multicollinearity |
| **Lasso Regression ($\alpha=0.01$)** | 0.752 | ~$167,500 | Automatic feature selection via L1 sparsity |
| **LightGBM Regressor** *(Modernized)* | **0.875** | **~$118,500** | Captures non-linear interactions & geographic clusters |

---

## 🖼️ Key Findings & Visualizations

### 1. Model Residual Diagnostics & Prediction Accuracy
![Model Summary](img/model_3_summary.png)

### 2. Actual vs. Predicted Housing Prices
![Actual vs Predicted](img/Pred_vs_real.png)

---

## 🚀 Interactive Streamlit Web Application

The project includes an interactive web micro-app built with **Streamlit**. Users can adjust house attributes (square footage, bedrooms, bathrooms, construction grade, and zip code) to receive an instant price valuation along with confidence ranges.

### Running the App Locally:

```bash
# 1. Clone the repository
git clone https://github.com/GitHub-ccd/king-county-housing-price-prediction.git
cd king-county-housing-price-prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit application
streamlit run app.py
```

---

## 🛠️ Tech Stack & Tools

* **Core Language**: Python 3.10+
* **Data Manipulation & Analysis**: `pandas`, `numpy`, `scipy`
* **Machine Learning & Modeling**: `scikit-learn`, `statsmodels`, `lightgbm`
* **Visualization**: `matplotlib`, `seaborn`
* **Web App & UI**: `streamlit`
* **Portfolio Integration**: [Healthcare Data Scientist Portfolio (`ccdportfolio`)](https://github.com/GitHub-ccd/ccdportfolio)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE.md).
