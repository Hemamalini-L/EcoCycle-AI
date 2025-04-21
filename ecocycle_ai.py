import streamlit as st
import datetime
import random

st.set_page_config(page_title="EcoCycle AI", page_icon="\ud83d\udeb2", layout="wide")

# --- Welcome Section ---
st.title("\ud83d\udeb2 EcoCycle AI - Smart Cycle Sharing System")
st.markdown("""
A fully **solar-powered**, AI-integrated cycle system made for **everyone**, including **differently-abled users**.  
EcoCycle enhances **mobility, sustainability, safety**, and real-time **intelligent decision making**.
""")

st.image("https://images.unsplash.com/photo-1595902203456-96caaac5392b", use_column_width=True)

# --- Video Demonstration ---
st.header("\ud83c\udfa5 Live Demo")
st.video("https://youtu.be/fu7VLfcLf6Y")

# --- AI & Tech Features ---
st.header("\ud83e\udde0 AI & Tech Features")
features = {
    "\ud83e\udded AI-Powered Route Optimization": "Suggests shortest & safest paths using real-time traffic data.",
    "\u267f Adaptive Technology": "Voice guidance, adjustable pedals, and posture support for differently-abled users.",
    "\ud83d\udc65 Dual Seating & Safety": "Ergonomic double seating with seatbelts, rear camera view, and bump sensors.",
    "\u26a0\ufe0f Emergency Alert System": "One-click SOS alerts nearest help stations.",
    "\ud83d\udccd Real-Time GPS Tracking": "Live cycle location, estimated time, and distance updates.",
    "\ud83d\udd0b Smart Battery Monitor": "Battery status, solar recharge level, and usage patterns.",
    "\ud83c\udfb5 In-Ride Entertainment": "Play music or podcasts during rides via in-cycle speaker.",
    "\ud83d\udcca Analytics Dashboard": "Speed, distance, CO2 saved, ride feedback, and usage heatmaps."
}

for k, v in features.items():
    st.markdown(f"**{k}**: {v}")

# --- Booking Form ---
st.header("\ud83d\udcdd Book an EcoCycle")
with st.form("booking_form"):
    name = st.text_input("Your Name")
    phone = st.text_input("Phone Number")
    pickup = st.text_input("Pickup Location")
    drop = st.text_input("Drop Location")
    date = st.date_input("Select Date", min_value=datetime.date.today())
    time = st.time_input("Pickup Time", value=datetime.time(9, 0))
    needs_adaptive = st.checkbox("I require adaptive support (for differently-abled)")
    entertainment = st.selectbox("Choose Entertainment", ["None", "Music", "Podcast"])
    submitted = st.form_submit_button("\ud83d\udeb4 Book Now")
    if submitted:
        st.success(f"\u2705 Booking confirmed for {name} on {date} at {time}!")
        st.info(f"Route from {pickup} to {drop} has been optimized using AI.")

# --- AI Route Optimization (Mocked) ---
if pickup and drop:
    route_distance = round(random.uniform(2.0, 8.0), 2)
    eta = int(route_distance * random.uniform(4, 6))
    st.header("\ud83e\udde0 Suggested Smart Route")
    st.markdown(f"**Optimized Distance**: {route_distance} km")
    st.markdown(f"**Estimated Time**: {eta} minutes \ud83d\udeb4")
    st.success("\u2705 Your route avoids traffic and maximizes safety using AI analysis.")

# --- Emergency Support ---
st.header("\ud83d\udea8 Emergency Signal")
if st.button("\ud83d\udd34 Send Emergency Signal"):
    st.error("\ud83d\udea8 Emergency Signal Sent! Nearby support teams alerted.")
    st.balloons()

# --- Battery & GPS Info (Mocked) ---
st.header("\ud83d\udd0b Battery & GPS Monitoring")
battery = random.randint(50, 100)
solar_gain = random.randint(1, 10)
location = "Live GPS: EcoCycle currently active in Zone 5, Tiruchengode"

col1, col2 = st.columns(2)
with col1:
    st.metric("\ud83d\udd0b Battery Level", f"{battery}%", delta=f"+{solar_gain}% solar charge")
with col2:
    st.success(location)

# --- Usage Analytics (Mocked Data) ---
st.header("\ud83d\udcca EcoCycle Analytics")
ride_count = random.randint(1000, 5000)
co2_saved = round(ride_count * 0.3, 2)
avg_speed = round(random.uniform(15, 25), 1)

st.markdown(f"""
- \ud83d\udeb2 **Total Rides**: {ride_count}  
- \ud83c\udf31 **CO\u2082 Saved**: {co2_saved} kg  
- \u26a1 **Avg. Speed**: {avg_speed} km/h  
""")

# --- Contact Section ---
st.header("\ud83d\udcde Contact Us")
st.markdown("""
- \ud83d\udce7 Email: **ecocycleai@domain.com**  
- \ud83d\udcf1 Phone: **+91-9876543210**  
- \ud83c\udf10 Website: [www.ecocycleai.in](https://www.ecocycleai.in)  
""")

# --- Footer ---
st.markdown("---")
st.caption("\u00a9 2025 EcoCycle-AI | Developed by Hemamalini L | All rights reserved.")
