import streamlit as st
import plotly.graph_objects as go

x_axis = [x / 10 for x in range(100)]

if "data" not in st.session_state:
    st.session_state.data = {
        "x_axis": x_axis,
        "y_axis": x_axis,
    }


def generate_data(dict):
    add = 0
    multi = 1
    exponent = 1
    for e in dict:
        num = float(e[2:])
        if "x+" in e:
            add += num
        elif "x^" in e:
            if exponent <= 1 and exponent >= -1:
                if num > 0:
                    exponent += num - 1
                else:
                    exponent += num + 1
            else:
                exponent += num
        elif "x*" in e:
            multi *= num
        elif "x/" in e:
            multi /= num
    st.session_state.data["y_axis"] = [
        add + (x**exponent) * multi for x in st.session_state.data["x_axis"]
    ]


if "options" not in st.session_state:
    st.session_state.options = []
if "show_ref" not in st.session_state:
    st.session_state.show_ref = True

st.multiselect(
    "Choose modules",
    ["x^2", "x+10", "x*3", "x^0.25", "x/2"],
    key="options",
)

fig1 = go.Figure()
fig1.add_trace(
    go.Scatter(x=st.session_state.data["x_axis"], y=st.session_state.data["y_axis"], name="Line")
)

if st.session_state.show_ref:
    fig1.add_trace(
        go.Scatter(x=st.session_state.data["x_axis"], y=st.session_state.data["x_axis"], name="Reference Line")
    )


st.plotly_chart(fig1)
st.session_state.show_ref = st.checkbox("Show reference line (f(x)=x)", value = True)

if st.button("Generate"):
    generate_data(st.session_state.options)
    st.rerun()
