import streamlit as st
import datetime
import random

st.set_page_config(page_title="EcoCycle AI", page_icon="🚲", layout="wide")

# --- Welcome Section ---
st.title("🚲 EcoCycle AI - Smart Cycle Sharing System")
st.markdown("""
A fully **solar-powered**, AI-integrated cycle system made for **everyone**, including **differently-abled users**.  
EcoCycle enhances **mobility, sustainability, safety**, and real-time **intelligent decision making**.
""")

st.image("https://images.unsplash.com/photo-1595902203456-96caaac5392b", use_column_width=True)

# --- Video Demonstration ---
st.header("🎥 Live Demo")
st.video("https://youtu.be/fu7VLfcLf6Y")

# --- AI & Tech Features ---
st.header("🧠 AI & Tech Features")
features = {
    "🧭 AI-Powered Route Optimization": "Suggests shortest & safest paths using real-time traffic data.",
    "♿ Adaptive Technology": "Voice guidance, adjustable pedals, and posture support for differently-abled users.",
    "👥 Dual Seating & Safety": "Ergonomic double seating with seatbelts, rear

