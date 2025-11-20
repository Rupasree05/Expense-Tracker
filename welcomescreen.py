import streamlit as st
import streamlit as st

st.set_page_config(page_title="Smart Expense", layout="centered")

# Center content
st.markdown("""
    <div style="text-align: center; padding-top: 50px;">
        <img src="https://cdn-icons-png.flaticon.com/512/2331/2331949.png" 
             width="100" style="margin-bottom: 20px;" />

        <h1 style="color:#2C3E50; font-size: 40px;">Smart Expense</h1>
        <p style="font-size:18px; color:#555;">
            Track your spending.<br>Grow your savings.
        </p>
    </div>
""", unsafe_allow_html=True)

# Button
if st.button("Get Started"):
    st.switch_page("pages/home_dashboard.py")
