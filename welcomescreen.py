import streamlit as st

st.set_page_config(page_title="Smart Expense", layout="centered")

# Show your custom image
st.image("C:/Users/User/Desktop/Rupa Sree/expense_Tracker_Image.png")

# Text content
st.markdown("""
<h1 style="color:#2C3E50; font-size: 40px; text-align:center;">
    Smart Expense
</h1>

<p style="font-size:18px; color:#555; text-align:center;">
    Track your spending.<br>Grow your savings.
</p>
""", unsafe_allow_html=True)

# Get Started Button
if st.button("Get Started"):
    st.switch_page("pages/home_dashboard.py")
