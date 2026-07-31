# 🚀 Streamlit Architecture & Deployment Guide

This document details the architectural rationale for choosing **Streamlit** over alternative frontend frameworks (such as Next.js/Vercel or GitHub Pages) for this predictive machine learning application, alongside step-by-step instructions for deploying and maintaining the live web app.

---

## 🏗️ Architectural Decision Record (ADR): Framework Selection

### Comparison Matrix

| Criteria | **Streamlit** (Chosen) | **Next.js + Vercel** | **GitHub Pages** |
| :--- | :--- | :--- | :--- |
| **Python ML Integration** | **Native** (Direct execution of `scikit-learn` & `pandas`) | Requires separate Python API (FastAPI) or ONNX export | Cannot execute Python server-side |
| **Backend & Compute** | Stateful Python server session | Serverless Node.js edge functions (package size limits) | Static files only (client-side JS) |
| **Development Velocity** | **Fastest** (~100 lines of pure Python) | Slower (Requires API routes, TS/JS UI, state management) | Fast for static text, N/A for live ML models |
| **Data Visualization** | Native `matplotlib`, `seaborn`, `plotly` rendering | Requires client-side chart libraries (Chart.js, Recharts) | Static images only |
| **Model Caching** | Built-in `@st.cache_resource` / `@st.cache_data` | Requires Redis / External caching tier | N/A |
| **Hosting Cost** | **Free** (Streamlit Cloud / Hugging Face) | Free tier on Vercel (limited serverless execution time) | Free (Static only) |

---

### Rationale for Selecting Streamlit

#### 1. Native Python Machine Learning Ecosystem
Our regression pipeline relies on `pandas`, `scikit-learn` (`HistGradientBoostingRegressor`), `numpy`, and `matplotlib`. Streamlit executes directly within the Python runtime, eliminating the need to compile models into JavaScript/ONNX or build intermediate REST API endpoints.

#### 2. Why Not GitHub Pages?
GitHub Pages only serves static assets (HTML/CSS/JS). It cannot execute server-side Python code or handle ML inference. While client-side Python runtimes like Pyodide exist, loading a 50MB+ Python WebAssembly bundle in a visitor's browser results in severe latency, high initial load times, and poor user experience for recruiters.

#### 3. Why Not Next.js + Vercel?
Next.js is ideal for production SaaS platforms and complex UI state management. However, deploying a machine learning model on Vercel requires hosting a separate Python backend (e.g., FastAPI on Render or AWS Lambda) because Vercel serverless functions have strict 250MB package limits that conflict with heavy ML libraries (`pandas`, `scikit-learn`, `lightgbm`). Streamlit provides an all-in-one Python full-stack solution with zero infrastructure overhead.

#### 4. Sub-Second Reactive Inference & Built-in Caching
Streamlit's `@st.cache_resource` loads the 21,597-row dataset and fits the ensemble regressor into memory once upon startup. Subsequent user input adjustments (`sqft_living`, `grade`, `zipcode`) trigger sub-100ms reactive predictions without re-reading disk files.

---

## 📦 Deployment Instructions

### Option 1: Streamlit Community Cloud (Recommended — Free & 1-Click)

Streamlit Community Cloud connects directly to your GitHub repository and automatically deploys the app upon code commits.

#### Step-by-Step Walkthrough:
1. Navigate to [share.streamlit.io](https://share.streamlit.io/) and log in using your GitHub account (`GitHub-ccd`).
2. Click the **"Create app"** button.
3. Configure the deployment settings:
   * **Repository**: `GitHub-ccd/king-county-housing-price-prediction`
   * **Branch**: `master`
   * **Main file path**: `app.py`
   * **App URL (Custom Subdomain)**: `king-county-housing-prediction.streamlit.app`
4. Click **"Deploy!"**.
5. *Verification*: Streamlit Cloud automatically reads `requirements.txt`, installs Python 3.10+ dependencies, loads `data/kc_house_data.csv`, and launches the app in under 2 minutes.

---

### Option 2: Hugging Face Spaces (Alternative Free Host)

If deploying to Hugging Face Spaces:
1. Create a new Space on [huggingface.co/spaces](https://huggingface.co/spaces).
2. Select **Streamlit** as the Space SDK.
3. Link your GitHub repository or push the repository files (`app.py`, `requirements.txt`, `data/`).
4. Hugging Face will build the container and provide an embeddable iframe URL for the portfolio.

---

### 💻 Local Execution & Development

To run and test the interactive web application on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/GitHub-ccd/king-county-housing-price-prediction.git
cd king-county-housing-price-prediction

# 2. Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Launch the Streamlit application
streamlit run app.py
```

Upon launching, Streamlit will open local browser preview at `http://localhost:8501`.
