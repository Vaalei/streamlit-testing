import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def f(x):
    y = x**2
    return np.random.normal(y, y/10)

def g(x):
    y = x**3
    return np.random.normal(y, y/10)

x_axis = [x/100 for x in range(1000)]


df = pd.DataFrame(
    {
        "x_axis": x_axis,
        "f": [f(x) for x in x_axis],
        "g": [g(x) for x in x_axis]
    }
)


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x = x_axis,
        y = [f(x) for x in x_axis],
        mode="markers"
    )
)
fig.add_trace(
    go.Scatter(
        x = x_axis,
        y = [g(x) for x in x_axis],
        mode="markers"
    )
)

st.plotly_chart(fig)



value = st.slider("Slider", min_value=1, max_value=100, value=10)
fig2 = px.scatter(
    df,
    x = df["f"] * value,
    y = "g",
    color = "g",
    size = "g"
)
st.plotly_chart(fig2)
