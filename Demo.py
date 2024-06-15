import streamlit as st

from src.agstyler import PINLEFT, PRECISION_TWO, draw_grid

formatter = {
    'player_name': ('Player', PINLEFT),
    'team': ('Team', {'width': 80}),
    'poss': ('Posessions', {'width': 110}),
    'mp': ('mp', {'width': 80}),
    'raptor_total': ('RAPTOR', {**PRECISION_TWO, 'width': 100}),
    'war_total': ('WAR', {**PRECISION_TWO, 'width': 80}),
    'pace_impact': ('Pace Impact', {**PRECISION_TWO, 'width': 120})
}

row_number = st.number_input('Number of rows', min_value=0, value=20)
data = draw_grid(
    df.head(row_number),
    formatter=formatter,
    fit_columns=True,
    selection='multiple',  # or 'single', or None
    use_checkbox='True',  # or False by default
    max_height=300
)
