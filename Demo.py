import streamlit as st
import pandas as pd

data = {
    'Fruit': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Quantity': [10, 15, 20, 25, 30],
    'Price': [0.5, 0.25, 0.75, 1.0, 2.0]
}
df = pd.DataFrame(data)

st.dataframe(df)
