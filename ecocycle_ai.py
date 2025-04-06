import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="EcoCycle-AI", layout="wide")

# Title and Intro
st.title("🚴 EcoCycle-AI: Smart Cycle Sharing System")
st.markdown("""
Welcome to **EcoCycle-AI**, an innovative AI-powered cycle sharing platform designed for smart cities and inclusive mobility.  
Our goal is to make transportation **eco-friendly**, **intelligent**, and **accessible to everyone**, including the differently-abled.
""")

# AI Cycle Image
image = Image.open("revolution-white-x-1024x670.jpg")
st.image(image, caption="AI-Powered Cycle", use_column_width=True)

# Video Demo
st.header("📽️ How It Works")
st.video("https://youtu.be/fu7VLfcLf6Y?si=srYur4nDvoev8JQe")

# Booking Section
st.header("📅 Book Your Ride")
if st.button("🚲 Book Now"):
    st.success("✅ Redirecting to booking portal... (Integrate Google Form or API here)")

# GPS Tracking (Simulation)
st.header("📍 GPS Tracking & Monitoring")
st.map(data=None)  # You can replace this with real GPS API data in future
st.markdown("""
**Live Location Tracking** enabled with smart AI monitoring system.
""")

# Emergency Assistance
st.header("🆘 Emergency Assistance")
if st.button("🚨 Send Emergency Signal"):
    st.warning("🚨 Emergency signal sent to nearest station! Help is on the way.")

# AI-Powered Routing
st.header("🧠 AI-Powered Route Optimization")
st.markdown("""
Our smart algorithm provides:
- Optimized routes based on traffic
- Support for differently-abled users
- Environmental-friendly suggestions 🚦🌳
""")

# Smart Battery & Transport Integration
st.subheader("🔋 Smart Battery & Transit Connectivity")
st.markdown("""
- Battery status notifications to avoid mid-way halts  
- Integrated with metro, bus, and local transport for hassle-free rides  
""")

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



