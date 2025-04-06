import streamlit as st

# Set page config
st.set_page_config(page_title="EcoCycle-AI", layout="wide")

# Title and intro
st.title("🚴 EcoCycle-AI: Smart Cycle Sharing System")
st.markdown("""
Welcome to **EcoCycle-AI**, an innovative AI-powered cycle sharing platform designed for smart cities and inclusive mobility.  
Our goal is to make transportation **eco-friendly**, **intelligent**, and **accessible to everyone**, including the differently-abled.
""")

# Image of AI-powered cycle
st.image("revolution-white-x-1024x670.jpg", caption="AI-Powered Cycle", use_column_width=True)

# Section: Video Demo
st.header("📽️ How It Works")
st.video("https://youtu.be/fu7VLfcLf6Y?si=srYur4nDvoev8JQe")

# Booking Button
st.header("📅 Book Your Ride")
if st.button("🚲 Book Now"):
    st.success("Redirecting to booking portal... (You can integrate a form or booking backend here.)")

# Features Section
st.header("🚴‍♀️ Key Features of EcoCycle-AI")
features = [
    "📍 **GPS Tracking System** - Track your cycle in real time.",
    "📡 **Real-Time Monitoring** - Monitor cycle status and location live.",
    "🆘 **Emergency Assistance** - Built-in system to send signals in emergencies.",
    "♿ **AI-Powered Route Optimization** - Smart routes based on user needs, including differently-abled support.",
    "🔋 **Smart Battery Monitoring** - Get notified when the battery is low.",
    "🌐 **Integrated with Local Transport** - Smooth transitions with metro and bus networks."
]
for feat in features:
    st.markdown(f"- {feat}")

# Contact Info
st.header("📞 Contact Us")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    - 📧 **Email**: hemamalini291204@gmail.com  
    - 📱 **Phone**: +91-9876543210  
    """)
with col2:
    st.markdown("""
    - 🌐 **Website**: [ecocycle-ai.web.app](https://ecocycle-ai.web.app)  
    - 🏢 **Address**: Vivekananda College of Technology for Women, Tamil Nadu  
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 EcoCycle-AI | Developed by Hemamalini L 💚")

