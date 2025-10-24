import streamlit as st

pages = {
    "Plots": [
        st.Page("routes/plot1.py", url_path="plot1", title="Plot 1 - Slider"),
        st.Page("routes/plot2.py", url_path="plot2", title="Plot 2 - Dropdown")
    ],
    "Groupfor other": [st.Page("routes/other.py", url_path="other", title="Other")]
}


nav = st.navigation(pages, position="sidebar")
nav.run()
