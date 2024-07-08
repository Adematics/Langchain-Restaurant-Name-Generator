import streamlit as st

# Import the helper function (assuming it's in a module named langchain_helper)
from langchain_helper import generate_resturant_name_and_items

# Streamlit app title
st.title("Restaurant Name Generator")

# Sidebar for selecting cuisine type
cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "Mexican", "British", "American"))

# Generate the restaurant name when a cuisine is selected
if cuisine:
    response = generate_resturant_name_and_items(cuisine)
    
    # Display the restaurant name
    st.header(response)
