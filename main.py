import streamlit as st
import pandas as pd
import numpy as np
import os
import requests
import json
import datetime
import matplotlib.pyplot as plt

# this will contain code that connects app.py with the function from the main file for P2



def generate_plot():
    # Generate your plot using Matplotlib
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 30, 40, 50]
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Display the plot using Streamlit
    st.pyplot(fig)
