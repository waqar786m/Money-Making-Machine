import streamlit as st
import random
import time
import requests

st.set_page_config(page_title="Money Making Machine", page_icon="💰")
st.title("💸 Money Making Machine 💸")

# Function to generate random money amount
def generate_money():
    return random.randint(1, 1000)

st.subheader("💰 Instant Cash Generator")
if st.button("💵 Generate Money"):
    with st.spinner("Counting your money..."):
        time.sleep(1)
        amount = generate_money()
    st.success(f"🎉 You made ${amount}!")

# Function to fetch side hustle ideas
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return "Freelancing"
    except:
        return "Something went wrong"

st.subheader("🚀 Side Hustle Ideas")
if st.button("🎯 Generate Hustle"):
    with st.spinner("Finding the best side hustle for you..."):
        time.sleep(1)
        idea = fetch_side_hustle()
    st.success(f"💡 {idea}")

# Function to fetch motivational money quotes
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quote = response.json()
            return quote["money_quote"]
        else:
            return "Money is the root of all evil"
    except:
        return "Something went wrong"

st.subheader("💡 Money-Making Motivation")
if st.button("📢 Get Inspired"):
    with st.spinner("Fetching an inspirational money quote..."):
        time.sleep(1)
        quote = fetch_money_quote()
    st.info(f"💭 {quote}")
