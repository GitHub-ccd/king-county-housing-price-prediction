# Portfolio Handoff Payload: King County Housing Price Prediction

This handoff document provides the complete, structured metadata, architectural rationale, and integration payload for embedding the **King County Housing Price Prediction** project into the **Healthcare Data Scientist Portfolio (`ccdportfolio`)** website.

---

## 🎯 Recruiter & Portfolio Integration Strategy: Interactive Demo Intent

To maximize recruiter engagement on the portfolio website, this project includes a **lightweight, standalone Streamlit web micro-app (`app.py`)**. 

* **Live Demo Deployment Target**: `https://king-county-housing-prediction.streamlit.app` (Streamlit Community Cloud)
* **Portfolio Showcase Integration**: Featured inside **Module 4 (Live Demos & Predictive Tools)** of `ccdportfolio`.
* **Recruiter Experience**: Recruiters and hiring managers visiting `ccdportfolio` can click the "Live Demo" button on the project card to launch an interactive widget where they can adjust home specs (living area sqft, grade, bedrooms, zipcode) and test real-time machine learning price predictions ($R^2 = 0.875$).

---

## 1. JSON Payload (`ccdportfolio/src/data/projects.json`)

```json
{
  "id": "king-county-housing-price-prediction",
  "title": "King County Housing Price Prediction",
  "shortDescription": "Multivariate regression & gradient boosting model with an interactive Streamlit app to estimate residential real estate values in King County, WA.",
  "category": "Machine Learning & Predictive Modeling",
  "tags": [
    "Python",
    "scikit-learn",
    "LightGBM",
    "Streamlit",
    "Feature Engineering",
    "Multivariate Regression",
    "Statsmodels",
    "Geo-spatial Analysis"
  ],
  "featured": true,
  "date": "2020 (Modernized 2026)",
  "githubUrl": "https://github.com/GitHub-ccd/king-county-housing-price-prediction",
  "liveDemoUrl": "https://king-county-housing-prediction.streamlit.app",
  "image": "/images/projects/king-county-housing.webp",
  "modalContent": {
    "overview": "Developed a comprehensive predictive analytics framework for King County residential property sales (~21,600 homes). Combines classical OLS regression diagnostics with modern regularized regression (Ridge, Lasso) and Gradient Boosting (LightGBM) to deliver accurate price estimates and actionable insights for real estate stakeholders.",
    "keyMetrics": [
      { "label": "Baseline OLS R²", "value": "0.751" },
      { "label": "LightGBM R²", "value": "0.875" },
      { "label": "Dataset Size", "value": "21,597 Homes" },
      { "label": "Key Drivers", "value": "Grade, Sqft, Geo-Location" }
    ],
    "highlights": [
      "Extensive Exploratory Data Analysis (EDA) on 19 physical, temporal, and spatial features across Seattle & King County.",
      "Engineered log-transformed continuous variables, one-hot encoded categorical factors, and calculated Haversine distance metrics.",
      "Multi-model benchmark comparing Statsmodels OLS, Ridge, Lasso, and LightGBM regressors.",
      "Built a live interactive Streamlit web micro-app enabling recruiters and non-technical stakeholders to input house specs and receive real-time price evaluations."
    ]
  }
}
```

---

## 2. Detailed Modal Description Text (For Portfolio Project Detail View)

### Project Backstory & Challenge
In real estate markets, accurately valuing residential properties is critical for homebuyers, sellers, and financial underwriters. Traditional appraisal methods often struggle with complex interactions between physical characteristics (living area, grade, bathrooms) and geographic location (zip codes, proximity to urban hubs). Using the King County House Sales dataset (covering sales between 2014–2015), this project builds an interpretable yet highly predictive regression framework.

### Technical Methodology & Pipeline
1. **Data Preprocessing & Cleaning**:
   - Inspected missing attributes, normalized skewed features (log transformations on price, sqft_living, sqft_lot), and filtered extreme outliers.
   - Identified and handled multicollinearity via Variance Inflation Factor (VIF) and correlation matrix pruning.
2. **Feature Engineering**:
   - Extracted temporal features from sale dates (seasonality, sale month).
   - Engineered spatial metrics including distance to central Seattle and local neighborhood zipcode clustering.
   - Encoded ordinal variables (`grade`, `condition`) and dummy-encoded categorical indicators (`waterfront`, `view`).
3. **Model Selection & Benchmarking**:
   - **Baseline OLS Regression (`Statsmodels`)**: Achieved $R^2 = 0.751$, validating statistical significance ($p < 0.05$) for key predictor coefficients.
   - **Regularized Linear Models (Ridge & Lasso)**: Controlled overfitting and reduced coefficient variance while maintaining high interpretability.
   - **Gradient Boosted Decision Trees (`LightGBM`)**: Boosted predictive power to $R^2 \approx 0.875$ with an RMSE reduction of over 20%.
4. **Interactive Deployment Intent**:
   - Deployed/configured as a **Streamlit web micro-app** enabling non-technical stakeholders to adjust property parameters (square footage, grade, bedrooms, zip code) and obtain instant market price estimates.

---

## 3. Architecture & Framework Rationale Summary

| Framework | Decision | Rationale |
| :--- | :--- | :--- |
| **Streamlit** | **Chosen** | Native execution of `scikit-learn`/`pandas` ML models in pure Python; zero API overhead; sub-100ms model caching; 1-click cloud deployment. |
| **Next.js + Vercel** | Not Selected | Requires building separate REST APIs (FastAPI) and encounters Vercel 250MB serverless package limits for heavy ML libraries (`pandas`, `scikit-learn`). |
| **GitHub Pages** | Not Selected | Static files only. Cannot run server-side Python ML models; browser Pyodide bundles create heavy latency for recruiters (~50MB+ download). |

---

## 4. Tech Stack Tags

| Category | Technologies |
| :--- | :--- |
| **Languages** | Python 3.10+ |
| **Data Processing & Analytics** | Pandas, NumPy, SciPy |
| **Modeling & Machine Learning** | scikit-learn, Statsmodels, LightGBM |
| **Data Visualization** | Matplotlib, Seaborn |
| **Application & Deployment** | Streamlit, Web API Wrapper |
| **Version Control & DevOps** | Git, GitHub Actions |

---

## 5. 2026 AI Banner Card Image Generation Prompt

> **Prompt for Midjourney / DALL-E 3 / Stable Diffusion:**
> *"Modern 3D isometric tech visualization of real estate data analytics in Seattle, featuring stylized glowing digital houses and analytical graphs emerging from an interactive map of King County Washington. Futuristic dark mode UI elements, clean glassmorphic cards showing housing price metrics and scatter plots, vibrant neon cyan and deep violet accents, highly detailed, 8k resolution, cinematic lighting, corporate data science aesthetic."*

---

## 6. Live Links & Deployment Coordinates

* **GitHub Repository**: [https://github.com/GitHub-ccd/king-county-housing-price-prediction](https://github.com/GitHub-ccd/king-county-housing-price-prediction)
* **Live Streamlit App Target**: [https://king-county-housing-prediction.streamlit.app](https://king-county-housing-prediction.streamlit.app)
* **Portfolio Showcase Category**: Module 4 (Live Demos & Predictive Tools)
