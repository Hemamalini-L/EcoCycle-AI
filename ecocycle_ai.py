import streamlit as st
from datetime import datetime
import random

# --- Page config ---
st.set_page_config(page_title="EcoCycle-AI", layout="wide")

# --- Welcome Section ---
st.title("🚴 EcoCycle-AI: Revolutionizing Urban Mobility")
st.markdown("""
Welcome to **EcoCycle-AI**, an AI-powered smart cycle sharing system designed to make urban transport **efficient**, **eco-friendly**, and **inclusive**.  
Experience seamless cycling with **live tracking**, **emergency alerts**, **route optimization**, and **smart booking**.
""")

# --- Image Section ---
st.image("revolution-white-x-1024x670.jpg", caption="AI-Powered Smart Cycle", use_column_width=True)

# --- Video Tutorial ---
st.header("📽️ How It Works")
st.video("https://youtu.be/fu7VLfcLf6Y?si=srYur4nDvoev8JQe")

# --- Booking Section ---
st.header("📅 Book Your Ride")
with st.form("booking_form"):
    name = st.text_input("Name")
    date = st.date_input("Booking Date", min_value=datetime.now().date())
    time = st.time_input("Pickup Time")
    pickup = st.text_input("Pickup Location")
    drop = st.text_input("Drop Location")
    cycles = st.number_input("Number of Cycles", min_value=1, max_value=5, step=1)
    submit = st.form_submit_button("🚲 Confirm Booking")

    if submit:
        st.success(f"✅ Booking confirmed for {name} on {date} at {time}.\nYour cycle(s) will be ready at {pickup}. Enjoy your ride to {drop}!")

# --- GPS Live Location Simulation ---
st.header("📍 Live GPS Tracker")
st.map({
    "lat": [11.3410 + random.uniform(-0.01, 0.01)],
    "lon": [77.7172 + random.uniform(-0.01, 0.01)]
})

# --- Emergency Assistance ---
st.header("🆘 Emergency Assistance")
if st.button("🚨 Send Emergency Signal"):
    st.error("Emergency alert sent to nearest support center. Help is on the way!")

# --- Estimated Time & Traffic ---
st.header("⏱️ Estimated Travel Time (Based on Traffic)")
traffic_factor = random.randint(10, 25)
st.info(f"Estimated time to reach your destination: **{traffic_factor} minutes**.")

# --- Battery Monitoring ---
st.header("🔋 Smart Battery & Charging Status")
battery_level = random.randint(40, 100)
charging = battery_level < 50
st.progress(battery_level / 100)
st.text(f"Battery Level: {battery_level}% {'(Charging Recommended)' if charging else '(Good to Go!)'}")

# --- Key Features Section ---
st.header("🚴‍♂️ Key Features")
st.markdown("""
- 📡 **Real-Time GPS Tracking**  
- 👁️ **Live Monitoring System**  
- 🆘 **Emergency Signal Support**  
- ♿ **Route Optimization for Differently-Abled**  
- 🔋 **Battery Level & Charging Station Info**  
- 🚌 **Local Transport Integration**  
- 💬 **User-Friendly Booking Interface**
""")

# --- Contact Section ---
st.header("📞 Contact Us")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    - 📧 Email: ecocyclesupport@gmail.com  
    - 📱 Contact: +91-9876543210
    """)
with col2:
    st.markdown("""
    - 🌐 Website: [ecocycle-ai.web.app](https://ecocycle-ai.web.app)  
    - 🧠 Powered by: Hemamalini L  
    """)

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 EcoCycle-AI | Built with ❤️ using Streamlit by Hemamalini L")




