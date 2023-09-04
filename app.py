import streamlit as st
import os

# Dropdown navigation
page_options = [
    "Project 1 Portfolio Update",
    "Project 1 Portfolio vs Algo",
    "Algo 1 Deep Dive",
    "Algo 2 Deep Dive",
    "Summary"
]

selected_page = st.selectbox("Select a page", page_options)

st.sidebar.markdown("[GitHub Repo](https://github.com/yourusername/portfolio-analysis-app)")

# Show selected page content
st.title("Portfolio Analysis")

if selected_page == "Project 1 Portfolio Update":
    st.header(selected_page)

    st.write('This is an update on the portfolio we showcased in Project 1')
    st.write('The return calculation is hence from May 10th 2023 to present day')

    st.image('Resources/p1_cumulative.png')
    st.write('Average index return since that period : 13%')
    st.write('Portfolio return since that period : 15%')
    st.write(r'2% difference is not an insignificant amount, but it becomes greater if we look at the risk profile')

    st.image('Resources/p1_sharpe.png')
    st.image('Resources/p1_sortino.png')

    st.write('Indices: 2.81 Sharpe. Portfolio: 3.53 Sharpe')
    st.write('Indices: 4.89 Sortino. Portfolio: 7.37 Sortino')

    st.header('Combined chart of Return vs Volatility')

    st.write('Orange: Indices. Green: Portfolio.')

    st.image('Resources/p1_combined.png')

elif selected_page == "Project 1 Portfolio vs Algo":
    st.header(selected_page)

    st.write('Here we compare the performance of our portfolio with best algos from Project 2')
    st.write('The return calculation is from the beginning of 2017 to present day')

    st.image('Resources/p1algo_cu.png')
    
    st.image('Resources/p1algo_sharpe.png')

    st.write('While algo was able to bring a much greater return, it also increased volatility')

    st.header('Combined chart of Return vs Volatility')

    st.write('Green: Indices. Orange: Portfolio. Cyan: Algo 1. Black: Algo 2')

    st.image('Resources/p1algo_combined.png')

elif selected_page == "Algo 1 Deep Dive":
    st.header(selected_page)
    st.image('Resources/bnh_algo_cu.png')
    st.image('Resources/bnh_algo_sharpe_volatility.png')
    st.image('Resources/bnh_algo_cu_volat.png')

elif selected_page == "Algo 2 Deep Dive":
    st.header(selected_page)
    st.image('Resources/bnh_algo2_cu.png')
    st.image('Resources/bnh_algo2_sharpe_volatility.png')
    st.image('Resources/bnh_algo2_cu_volat.png')
    
elif selected_page == "Summary":
    st.header(selected_page)