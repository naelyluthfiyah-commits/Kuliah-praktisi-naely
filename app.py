import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="Kuliah Praktisi",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    
)
st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")
st.write("Hello, *World!* :candy:")

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)

