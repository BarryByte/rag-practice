import streamlit as st
import langchain_helper

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app to find cool restaurant name and cuisine.")
st.button("Click Me!")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Chinese", "Afganisthani", "Arabic", "European","American", "Mexican"))




if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")


    st.write("**MENU ITEMS**")
    for item in menu_items:
        st.write("-", item)