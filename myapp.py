import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

chart_data = pd.Dataframe(np.random.randn(20, 3), columns=['a', 'b', 'c', 'd'])

image = Image.open("Logo-KDT-JU.webp")
st.image(image)
st.write("My first web app")

st.cache

st.write(chart_data)
