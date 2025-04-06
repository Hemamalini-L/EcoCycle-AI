import streamlit as st

# Page configuration
st.set_page_config(page_title="EcoCycle-AI", layout="centered")

# Title & Intro
st.title("🚲 EcoCycle-AI: Smart Cycle Sharing System")
st.subheader("AI-powered cycle sharing platform for smarter, safer commuting.")

# Booking button
if st.button("Book a Cycle Now"):
    st.success("✅ Booking feature will be available soon!")

# Video demo section
st.header("🎥 How It Works")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Replace with your actual demo video URL

# Features section
st.header("🚴‍♂️ Key Features")
st.markdown("""
- 📍 **GPS Tracking System** — Locate cycles in real-time  
- 📡 **Real-Time Monitoring** — Monitor usage and performance  
- 🚨 **Emergency Signals** — Sends alerts when unsafe conditions are detected  
- 👩‍🦽 **Adaptive Cycles** — Inclusive design for differently-abled users
""")

# Contact Info
st.header("📞 Contact Us")
st.markdown("""
**Email:** support@ecocycleai.com  
**Phone:** +91 98765 43210  
**Instagram:** [@ecocycle_ai](https://instagram.com)
""")
