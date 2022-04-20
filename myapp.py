import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

chart_data = pd.Dataframe(np.random.randn(20, 3), columns=['a', 'b', 'c', 'd'])

st.image("Logo-KDT-JU.png")
st.write("My first web app")
st.write(chart_data)
