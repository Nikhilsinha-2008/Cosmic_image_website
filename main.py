import streamlit as st
import requests

API_KEY = "Yyx3ocHnePp8hkjlQZ5G4ncxtUL4BVfMgAaEt7df"
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3"
    " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(URL, headers=headers)
content = response.json()

image_url = content["hdurl"]
image_response = requests.get(image_url)
with open("image.png", "wb") as file:
    file.write(image_response.content)

st.title("My Galaxy Image")
st.subheader(content["title"])
st.image("image.png")
st.write(content["date"])
st.write(content["explanation"])
