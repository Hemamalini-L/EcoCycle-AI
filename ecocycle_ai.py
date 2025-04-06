import streamlit as st

# Page configuration
st.set_page_config(page_title="EcoCycle-AI", layout="centered")

# Title & intro
st.title("🚲 EcoCycle-AI: Smart Cycle Sharing System")
st.markdown("""
Welcome to **EcoCycle-AI**, an intelligent and inclusive cycle-sharing platform designed with advanced AI features to promote eco-friendly, accessible, and safe mobility for everyone.
""")

# Booking button
st.markdown("### 📅 Book a Cycle Now")
if st.button("🚴 Book a Ride"):
    st.success("Booking feature coming soon! Stay tuned.")

# Video demo
st.markdown("### 📽️ Watch How It Works")
st.video("https://youtu.be/fu7VLfcLf6Y?si=srYur4nDvoev8JQe")

# Features section
st.markdown("### 🔍 Key Features")
st.markdown("""
- 📍 **GPS Tracking System**  
- ⏱️ **Real-Time Monitoring**  
- 🆘 **Emergency Signal Alerts**  
- 🧭 **AI-Powered Route Optimization**  
- 🧑‍🦽 **Adaptive Technology for Differently-Abled Users**  
- 🔋 **Battery & Health Tracking**
""")

# AI Cycle Image
st.markdown("### 🖼️ Sample AI-Powered Cycle")
st.image("revolution-white-x-1024x670.jpg", caption="Revolution HPC AI-Powered Cycle", use_column_width=True)

# Contact Information
st.markdown("### 📬 Contact Us")
st.markdown("""
- 📧 Email: [ecocycleai@gmail.com](mailto:ecocycleai@gmail.com)  
- 📱 Phone: +91 98765 43210  
- 🌐 Website: [https://ecocycle-ai.streamlit.app](https://ecocycle-ai.streamlit.app)
""")

# Footer
st.markdown("---")
st.markdown("© 2025 EcoCycle-AI. All rights reserved.")

