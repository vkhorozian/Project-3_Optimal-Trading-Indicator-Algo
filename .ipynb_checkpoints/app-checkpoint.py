
# Imports
import streamlit as st

# @TODO: # From main.ipynb file in p2 algo import function we will need to call to display data
from main import generate_plot

################################################################################
# Streamlit Code

# Streamlit application "navbar"
page = st.selectbox("Choose a page", ["Page 1", "Page 2", "Page 3"])


if page == "Page 1":
    st.header("Current Active Balance Page")
    # Add your content here
    st.markdown("## Welcome to the Crypto Cat Shop")
    st.markdown("### Buy a kitten")

    st.sidebar.markdown("## text goes here")
    st.sidebar.markdown("---------")
    

    st.sidebar.markdown("##  Name")
    st.sidebar.markdown("##  Price")

# w3.eth.accounts[0]

elif page == "Page 2":
    st.header("Push the Button Header")
    st.write("find button below")
    st.text("\n\n")
    ## try to show the plot here from the import function from main.py above


    # @TODO
    # Create a button that calls the `send_transaction` function and returns the transaction hash
    if st.button("Push to Plot Button"):
        st.markdown("## Button was pushed")
        st.text("\n\n")
        generate_plot()



else:
    st.header("Welcome to Page 3")
    # Add your content here
    st.write("This is page 2 Hello world!!!!")