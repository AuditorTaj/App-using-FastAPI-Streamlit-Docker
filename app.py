import streamlit as st
import requests

# Define API URL
API_URL = "http://localhost:8000"

# Define Streamlit App
def main():
    st.title("Application using FastAPI & Streamlit")

    # Make a request to the FastAPI backend
    response = requests.get(API_URL)
    data = response.json()

    # Display response
    st.write("Response from FastAPI Backend:")
    st.write(data)

if __name__ == "__main__":
    main()
