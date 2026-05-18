import streamlit as st
import pandas as pd
import plotly.express as px

# Page Setup
st.set_page_config(page_title="Food Waste Dashboard", layout="wide")

st.title("🍽 Analysis of food waste in restaurants")

# -----------------------------
# Survey Results Data
# -----------------------------

prepared_data = {
    "Category": ["<50", "50-100", "100-200", ">200"],
    "Responses": [2, 2, 1, 2]
}

sold_data = {
    "Category": ["<50", "50-100", "100-200", ">200"],
    "Responses": [2, 2, 2, 1]
}

waste_data = {
    "Category": ["<5%", "5-10%", "10-20%", ">20%"],
    "Responses": [2, 4, 1, 0]
}

food_type_data = {
    "Category": ["Chicken", "Meat", "Rice/Pasta", "Desserts"],
    "Responses": [1, 3, 2, 1]
}

# Convert to DataFrames
prepared_df = pd.DataFrame(prepared_data)
sold_df = pd.DataFrame(sold_data)
waste_df = pd.DataFrame(waste_data)
food_df = pd.DataFrame(food_type_data)

# -----------------------------
# KPIs
# -----------------------------

col1, col2, col3 = st.columns(3)

col1.metric("Surveyed Restaurants", 7)
col2.metric("Highest Waste Category", "5-10%")
col3.metric("Most Wasted Food", "Meat")

st.divider()

# -----------------------------
# Charts
# -----------------------------

col4, col5 = st.columns(2)

# Prepared Meals Chart
fig1 = px.bar(
    prepared_df,
    x="Category",
    y="Responses",
    title="Prepared Meals Per Day"
)
col4.plotly_chart(fig1, use_container_width=True)

# Sold Meals Chart
fig2 = px.pie(
    sold_df,
    values="Responses",
    names="Category",
    title="Sold Meals Per Day"
)
col5.plotly_chart(fig2, use_container_width=True)

# Waste Percentage Chart
fig3 = px.bar(
    waste_df,
    x="Category",
    y="Responses",
    title="Food Waste Percentage"
)
st.plotly_chart(fig3, use_container_width=True)

# Food Type Waste Chart
fig4 = px.pie(
    food_df,
    values="Responses",
    names="Category",
    title="Most Wasted Food Types"
)
st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# Insights
# -----------------------------
st.subheader("📌 Insights")
st.write("""
- Most restaurants reported food waste between 5% and 10%.
- Meat meals had the highest waste percentage.
- Many restaurants do not regularly track food waste.
- High raw material prices affect restaurant pricing.
- Some restaurants suffer from low demand and lack of delivery services.
""")
