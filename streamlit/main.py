import streamlit as st
import pandas as pd


products = pd.read_csv("products-100.csv")



st.set_page_config("Data Analysis", layout="wide")
st.header("Building a Data Analysis Dashboard in Python")


st.header("Products")
st.header("Building a Data Analysis Dashboard In Python")

st.header("Products")
st.dataframe(products, hide_index = True)

# Basic Dataset Information
st.write("Rows and Columns", products.shape)

st.write("You can type here")
name = st.text_input("Enter you Name Here")

st.write(name)
st.button("Submit Button")

data= {
    "Name": ["Sara", "Usman", "Ali"],
    "Age": [19, 20, 21]
}

st.table(data)
st.dataframe(data)
st.sidebar.header("Sidebar")
st.sidebar.subheader("Sidebar")