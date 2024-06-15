import streamlit as st
import ppandas as pd
from st_aggrid import Agrid

data = {
    'Fruit': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Quantity': [10, 15, 20, 25, 30],
    'Price': [0.5, 0.25, 0.75, 1.0, 2.0]
}

AgGrid(df)
