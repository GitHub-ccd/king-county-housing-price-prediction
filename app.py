import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Set page configuration
st.set_page_config(
    page_title="King County Housing Price Predictor",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished aesthetic
st.markdown("""
    <style>
    .main-title {
        font-size: 2.3rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏡 King County Real Estate Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Interactive machine learning valuation model for Seattle & King County residential properties</div>', unsafe_allow_html=True)

# Load data and train model with caching
@st.cache_data
def load_and_prep_data():
    data_path = os.path.join(os.path.dirname(__file__), "data", "kc_house_data.csv")
    if not os.path.exists(data_path):
        # Fallback if running outside root
        data_path = "data/kc_house_data.csv"
    
    df = pd.read_csv(data_path)
    # Clean data
    df = df.dropna(subset=['price', 'sqft_living', 'bedrooms', 'bathrooms'])
    return df

@st.cache_resource
def train_model(df):
    features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 
                'waterfront', 'view', 'condition', 'grade', 'sqft_above', 
                'sqft_basement', 'yr_built', 'zipcode', 'lat', 'long']
    
    X = df[features]
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = HistGradientBoostingRegressor(random_state=42, max_iter=150)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    return model, features, r2, rmse

try:
    df = load_and_prep_data()
    model, feature_names, model_r2, model_rmse = train_model(df)
    data_loaded = True
except Exception as e:
    st.error(f"Error loading dataset or training model: {e}")
    data_loaded = False

if data_loaded:
    # Sidebar input parameters
    st.sidebar.header("📋 Property Characteristics")

    col1, col2 = st.columns([1, 2])

    with st.sidebar:
        sqft_living = st.slider("Living Area (sqft)", min_value=500, max_value=10000, value=2100, step=50)
        sqft_lot = st.number_input("Lot Size (sqft)", min_value=500, max_value=100000, value=7500, step=500)
        bedrooms = st.selectbox("Bedrooms", options=list(range(1, 10)), index=2)
        bathrooms = st.slider("Bathrooms", min_value=0.75, max_value=7.5, value=2.25, step=0.25)
        floors = st.selectbox("Floors", options=[1.0, 1.5, 2.0, 2.5, 3.0, 3.5], index=2)
        grade = st.slider("Construction Grade (1-13)", min_value=1, max_value=13, value=7, help="7 is average, 11-13 is luxury design")
        condition = st.slider("Condition Rating (1-5)", min_value=1, max_value=5, value=3)
        view = st.slider("View Rating (0-4)", min_value=0, max_value=4, value=0)
        waterfront = st.radio("Waterfront Location", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No", index=0)
        yr_built = st.slider("Year Built", min_value=1900, max_value=2015, value=1985)
        
        # Zipcode selection
        popular_zipcodes = sorted(df['zipcode'].unique())
        zipcode = st.selectbox("Zipcode", options=popular_zipcodes, index=popular_zipcodes.index(98004) if 98004 in popular_zipcodes else 0)

        # Lookup average lat/long for chosen zipcode
        zip_data = df[df['zipcode'] == zipcode]
        lat = zip_data['lat'].mean() if not zip_data.empty else df['lat'].mean()
        long = zip_data['long'].mean() if not zip_data.empty else df['long'].mean()

        sqft_above = int(sqft_living * 0.8)
        sqft_basement = int(sqft_living * 0.2)

    # Make prediction
    input_data = pd.DataFrame([{
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft_living': sqft_living,
        'sqft_lot': sqft_lot,
        'floors': floors,
        'waterfront': waterfront,
        'view': view,
        'condition': condition,
        'grade': grade,
        'sqft_above': sqft_above,
        'sqft_basement': sqft_basement,
        'yr_built': yr_built,
        'zipcode': zipcode,
        'lat': lat,
        'long': long
    }])

    predicted_price = model.predict(input_data)[0]

    with col1:
        st.subheader("💰 Valuation Estimate")
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #1E293B, #0F172A); padding: 24px; border-radius: 16px; color: white; text-align: center;">
                <p style="font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; color: #94A3B8; margin-bottom: 4px;">Estimated Valuation</p>
                <h2 style="font-size: 2.4rem; font-weight: 800; color: #38BDF8; margin: 0;">${predicted_price:,.0f}</h2>
                <p style="font-size: 0.85rem; color: #CBD5E1; margin-top: 8px;">Estimated Range: ${predicted_price - model_rmse*0.8:,.0f} - ${predicted_price + model_rmse*0.8:,.0f}</p>
            </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.write("")
        st.metric("Model Test R² Score", f"{model_r2:.3f}")
        st.metric("Model Test RMSE", f"${model_rmse:,.0f}")

    with col2:
        st.subheader("📊 Market Comparison & Neighborhood Context")
        
        # Compare prediction with zipcode distribution
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(zip_data['price'] / 1000, kde=True, color='#0ea5e9', ax=ax)
        ax.axvline(predicted_price / 1000, color='#ef4444', linestyle='--', linewidth=2.5, label=f'Estimated Home (${predicted_price/1000:,.0f}k)')
        ax.set_title(f"Price Distribution in Zipcode {zipcode} (in $1,000s)", fontsize=11, fontweight='bold')
        ax.set_xlabel("Price ($1,000s)")
        ax.set_ylabel("Count")
        ax.legend()
        st.pyplot(fig)

    st.markdown("---")
    st.subheader("📌 Model Features & Overview")
    st.info("This application utilizes Gradient Boosted Decision Trees trained on 21,597 residential property transactions across King County, WA. Feature inputs include living space, location coordinates, construction quality grades, and temporal attributes.")
