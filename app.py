import streamlit as st
import os

# Dropdown navigation
page_options = [
    "Page 1: Sharpe ratio v Cumulative returns",
    "Page 2: Annualized Returns vs Annualized Volatility",
    "Page 3: Top 3 Portfolio Returns vs S&P",
    "Page 4: Returns vs Standard Deviation",
    "Page 5: Performance Metrics"
]

selected_page = st.selectbox("Select a page", page_options)

st.sidebar.markdown("[GitHub Repo](https://github.com/yourusername/portfolio-analysis-app)")
st.sidebar.markdown("[Download Sample Data](https://example.com/sample_data.zip)")

# Show selected page content
st.title("Portfolio Analysis")

if selected_page == "Page 1: Sharpe ratio v Cumulative returns":
    st.header(selected_page)
    algorithm = st.selectbox("Select Algorithm", ["Algorithm A", "Algorithm B", "Algorithm C"])
    image_path = os.path.join("Resources", f"{algorithm.lower()}_1.jpg")
    st.image(image_path)

elif selected_page == "Page 2: Annualized Returns vs Annualized Volatility":
    st.header(selected_page)
    algorithm = st.selectbox("Select Algorithm", ["Algorithm A", "Algorithm B", "Algorithm C"])
    image_path = os.path.join("Resources", f"{algorithm.lower()}_2.jpg")
    st.image(image_path)

elif selected_page == "Page 3: Top 3 Portfolio Returns vs S&P":
    st.header(selected_page)
    algorithm = st.selectbox("Select Algorithm", ["Algorithm A", "Algorithm B", "Algorithm C"])
    image_path = os.path.join("Resources", f"{algorithm.lower()}_3.jpg")
    st.image(image_path)

elif selected_page == "Page 4: Returns vs Standard Deviation":
    st.header(selected_page)
    algorithm = st.selectbox("Select Algorithm", ["Algorithm A", "Algorithm B", "Algorithm C"])
    image_path = os.path.join("Resources", f"{algorithm.lower()}_4.jpg")
    st.image(image_path)

elif selected_page == "Page 5: Performance Metrics":
    st.header(selected_page)
    algorithm = st.selectbox("Select Algorithm", ["Algorithm A", "Algorithm B", "Algorithm C"])
    image_path = os.path.join("Resources", f"{algorithm.lower()}_5.jpg")
    st.image(image_path)