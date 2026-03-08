# ==========================================================
# European Bank Churn Analytics Dashboard — Final Version
# Includes: 5 KPIs, 4 Core Modules, Drill-Down, Logos, Styling
# ==========================================================

import os
import base64
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# ------------------------ PAGE CONFIG ------------------------
st.set_page_config(page_title="European Bank - Customer Segmentation & Churn Pattern Analytics", page_icon="💳", layout="wide")

# ------------------------ GLOBAL STYLING ------------------------
st.markdown("""
    <style>
    body {
        background-color: #f4f6fa;
        color: #1e1e1e;
        font-family: "Segoe UI", sans-serif;
    }
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 1rem;
    }
    h1, h2, h3 {
        color: #003366;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------ LOGO HANDLING ------------------------
def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def render_header():
    # Use your provided logo paths
    bank_logo_path = r"C:\Users\HP1\Desktop\streamlit_project\bank_logo (1).png"
    unified_logo_path = r"C:\Users\HP1\Desktop\streamlit_project\unified_logo.png"

    bank_logo_html = unified_logo_html = ""

    if os.path.exists(bank_logo_path):
        b64_bank = image_to_base64(bank_logo_path)
        bank_logo_html = f"<img src='data:image/png;base64,{b64_bank}' width='110'/>"
    else:
        st.warning(f"⚠️ Bank logo not found: {bank_logo_path}")

    if os.path.exists(unified_logo_path):
        b64_unified = image_to_base64(unified_logo_path)
        unified_logo_html = f"<img src='data:image/png;base64,{b64_unified}' width='110'/>"
    else:
        st.warning(f"⚠️ Unified logo not found: {unified_logo_path}")

    # Top banner with logos and gradient background
    
    st.markdown(f"""
        <div style="
            background: linear-gradient(90deg, #002b5b 0%, #004b8d 60%, #0066b2 100%);
            padding: 20px 0;
            border-radius: 12px;
            width: 100%;
        ">
            <div style="
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 95%;
                margin: auto;
            ">
                <div>{bank_logo_html}</div>
                <div style="text-align: center; flex-grow: 1;">
                    <h2 style='color: white; font-size: 28px; margin: 0; letter-spacing: 0.5px;'>
                        European Bank — Customer Segmentation & Churn Pattern Analytics
                    </h2>
                </div>
                <div>{unified_logo_html}</div>
            </div>
        </div>

    """, unsafe_allow_html=True)

# ------------------------ LOAD DATA ------------------------
@st.cache_data
def load_data():
    return pd.read_csv("processed_cleaned.csv")

df = load_data()
render_header()

# ------------------------ FILTERS ------------------------
st.sidebar.header("🎯 Segment Filters")
geo = st.sidebar.multiselect("🌍 Geography", df["Geography"].unique(), df["Geography"].unique())
age = st.sidebar.multiselect("👥 Age Group", df["AgeGroup"].unique(), df["AgeGroup"].unique())
tenure = st.sidebar.multiselect("📆 Tenure Group", df["TenureGroup"].unique(), df["TenureGroup"].unique())

filtered = df[(df["Geography"].isin(geo)) & (df["AgeGroup"].isin(age)) & (df["TenureGroup"].isin(tenure))]

# ------------------------ KPI CALCULATIONS ------------------------
overall_churn = filtered["Exited"].mean() if len(filtered) else 0
threshold = filtered["CustomerValue"].quantile(0.8) if len(filtered) else 0
high_value_df = filtered[filtered["CustomerValue"] >= threshold]
high_value_churn = high_value_df["Exited"].mean() if len(high_value_df) else 0
geo_churn = filtered.groupby("Geography")["Exited"].mean()
geo_risk_index = geo_churn / overall_churn if overall_churn > 0 else geo_churn * 0
active_churn = filtered[filtered["IsActiveMember"] == 1]["Exited"].mean() if len(filtered) else 0
inactive_churn = filtered[filtered["IsActiveMember"] == 0]["Exited"].mean() if len(filtered) else 0
engagement_drop = inactive_churn / active_churn if active_churn > 0 else np.nan

# ------------------------ KPI DISPLAY ------------------------
st.markdown("### 📊 Key Performance Indicators")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Overall Churn Rate", f"{overall_churn*100:.2f} %")
col2.metric("High-Value Churn", f"{high_value_churn*100:.2f} %")
col3.metric("Top Geo Risk Index", f"{geo_risk_index.max():.2f}×" if not geo_risk_index.empty else "n/a")
col4.metric("Avg Geo Risk Index", f"{geo_risk_index.mean():.2f}×" if not geo_risk_index.empty else "n/a")
col5.metric("Engagement Drop", f"{engagement_drop:.2f}×" if not np.isnan(engagement_drop) else "n/a")
st.markdown("<hr>", unsafe_allow_html=True)

# ------------------------ COLOR PALETTE ------------------------
COLORS = ["#0077b6", "#0096c7", "#00b4d8", "#48cae4", "#90e0ef"]

# ------------------------ CORE MODULES ------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🌍 Geography Churn", 
    "👥 Age & Tenure", 
    "💰 High-Value Customers", 
    "📈 Summary & Risk Index"
])

# ========== TAB 1: GEOGRAPHY + DRILL-DOWN ==========
with tab1:
    st.subheader("🌍 Churn Rate by Geography")

    geo_df = filtered.groupby("Geography")["Exited"].mean().reset_index()
    fig_geo = px.bar(geo_df, x="Geography", y="Exited", color="Geography",
                     color_discrete_sequence=COLORS,
                     text=(geo_df["Exited"]*100).round(2),
                     title="Churn Rate by Geography (%)")
    fig_geo.update_traces(textposition="outside")
    fig_geo.update_layout(plot_bgcolor="#f4f6fa", paper_bgcolor="#f4f6fa", font_color="#002b5b")
    st.plotly_chart(fig_geo, use_container_width=True)

    # Drill-down: Select a country → view age-group churn
    st.markdown("### 🔍 Drill-Down: Churn by Age Group per Country")
    selected_country = st.selectbox("Select Country for Drill-Down", sorted(df["Geography"].unique()))
    subset = filtered[filtered["Geography"] == selected_country]
    if len(subset) > 0:
        age_geo = subset.groupby("AgeGroup")["Exited"].mean().reset_index()
        fig_drill = px.bar(age_geo, x="AgeGroup", y="Exited", color="AgeGroup",
                           color_discrete_sequence=px.colors.sequential.Blues,
                           text=(age_geo["Exited"]*100).round(2),
                           title=f"Churn by Age Group — {selected_country}")
        fig_drill.update_traces(textposition="outside")
        st.plotly_chart(fig_drill, use_container_width=True)
    else:
        st.info("No data for the selected country under current filters.")

# ========== TAB 2: AGE & TENURE ==========
with tab2:
    st.subheader("👥 Churn by Age Group & Tenure")
    age_ten = filtered.groupby(["AgeGroup", "TenureGroup"])["Exited"].mean().reset_index()
    fig_age = px.bar(age_ten, x="AgeGroup", y="Exited", color="TenureGroup", barmode="group",
                     color_discrete_sequence=COLORS,
                     title="Churn by Age & Tenure (%)")
    fig_age.update_traces(texttemplate="%{y:.1%}", textposition="outside")
    st.plotly_chart(fig_age, use_container_width=True)

# ========== TAB 3: HIGH-VALUE CUSTOMERS ==========
with tab3:
    st.subheader("💰 High-Value Customer Explorer")
    if len(high_value_df) > 0:
        fig_hv = px.scatter(high_value_df, x="Balance", y="EstimatedSalary", color="Exited",
                            color_continuous_scale=px.colors.sequential.Blues,
                            hover_data=["CustomerId", "Geography", "AgeGroup"],
                            title="Balance vs Salary — High-Value Customers")
        st.plotly_chart(fig_hv, use_container_width=True)
    else:
        st.info("No high-value customers in the selected filters.")

# ========== TAB 4: SUMMARY & RISK INDEX ==========
with tab4:
    st.subheader("📈 Regional Risk Index Summary")
    risk_df = geo_risk_index.reset_index()
    risk_df.columns = ["Geography", "RiskIndex"]
    fig_risk = px.bar(risk_df, x="Geography", y="RiskIndex", color="Geography",
                      text=risk_df["RiskIndex"].round(2),
                      color_discrete_sequence=COLORS,
                      title="Regional Risk Index (>1 = Above-Average Churn Risk)")
    fig_risk.update_traces(textposition="outside")
    st.plotly_chart(fig_risk, use_container_width=True)

st.markdown("---")
st.caption("© 2026 European Bank Analytics | Built by: Poorvi Malvi | Unified Mentor Internship")