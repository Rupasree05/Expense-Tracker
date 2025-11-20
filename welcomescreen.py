import streamlit as st
import streamlit as st

st.set_page_config(page_title="Smart Expense", layout="centered")

# Center content

st.markdown("""
<h1 style="color:#2C3E50; font-size: 40px;">Smart Expense</h1>
<p style="font-size:18px; color:#555;">
    Track your spending.<br>Grow your savings.
</p>
""", unsafe_allow_html=True)


# Button
if st.button("Get Started"):
    st.switch_page("pages/home_dashboard.py")
