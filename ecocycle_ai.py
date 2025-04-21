import streamlit as st
import datetime
import random

st.set_page_config(page_title="EcoCycle AI", page_icon="🚲", layout="wide")

# 1. Welcome Section
st.title("🚲 EcoCycle AI - Smart Cycle Sharing System")
st.markdown("""
A fully **solar-powered**, AI-integrated cycle system made for **everyone**, including **differently-abled users**.  
EcoCycle enhances **mobility, sustainability, safety**, and real-time **intelligent decision making**.
""")

st.image("https://images.unsplash.com/photo-1595902203456-96caaac5392b", use_column_width=True)

# 2. Video Demonstration
st.header("🎥 Live Demo")
st.video("https://youtu.be/fu7VLfcLf6Y")

# 3. Key AI-Powered Features
st.header("🧠 AI & Tech Features")
features = {
    "🧭 AI-Powered Route Optimization": "Suggests shortest & safest paths using real-time traffic data.",
    "♿ Adaptive Technology": "Voice guidance, adjustable pedals, and posture support for differently-abled users.",
    "👥 Dual Seating & Safety": "Ergonomic double seating with seatbelts, rear camera view, and bump sensors.",
    "⚠️ Emergency Alert System": "One-click SOS alerts nearest help stations.",
    "📍 Real-Time GPS Tracking": "Live cycle location, estimated time, and distance updates.",
    "🔋 Smart Battery Monitor": "Battery status, solar recharge level, and usage patterns.",
    "🎵 In-Ride Entertainment": "Play music or podcasts during rides via in-cycle speaker.",
    "📊 Analytics Dashboard": "Speed, distance, CO2 saved, ride feedback, and usage heatmaps."
}

for k, v in features.items():
    st.markdown(f"**{k}**: {v}")

# 4. Booking Form
st.header("📝 Book an EcoCycle")
with st.form("booking_form"):
    name = st.text_input("Your Name")
    phone = st.text_input("Phone Number")
    pickup = st.text_input("Pickup Location")
    drop = st.text_input("Drop Location")
    date = st.date_input("Select Date", min_value=datetime.date.today())
    time = st.time_input("Pickup Time", value=datetime.time(9, 0))
    needs_adaptive = st.checkbox("I require adaptive support (for differently-abled)")
    entertainment = st.selectbox("Choose Entertainment", ["None", "Music", "Podcast"])
    submitted = st.form_submit_button("🚴 Book Now")
    if submitted:
        st.success(f"✅ Booking confirmed for {name} on {date} at {time}!")
        st.info(f"Route from {pickup} to {drop} has been optimized using AI.")

# 5. AI Route Optimization (Mocked)
if pickup and drop:
    route_distance = round(random.uniform(2.0, 8.0), 2)
    eta = int(route_distance * random.uniform(4, 6))
    st.header("🧠 Suggested Smart Route")
    st.markdown(f"**Optimized Distance**: {route_distance} km")
    st.markdown(f"**Estimated Time**: {eta} minutes 🚴")
    st.success("✅ Your route avoids traffic and maximizes safety using AI analysis.")

# 6. Emergency Support
st.header("🚨 Emergency Signal")
if st.button("🔴 Send Emergency Signal"):
    st.error("🚨 Emergency Signal Sent! Nearby support teams alerted.")
    st.balloons()

# 7. Battery & GPS Info (Mocked)
st.header("🔋 Battery & GPS Monitoring")
battery = random.randint(50, 100)
solar_gain = random.randint(1, 10)
location = "Live GPS: EcoCycle currently active in Zone 5, Tiruchengode"

col1, col2 = st.columns(2)
with col1:
    st.metric("🔋 Battery Level", f"{battery}%", delta=f"+{solar_gain}% solar charge")
with col2:
    st.success(location)

# 8. Usage Analytics (Mock Data)
st.header("📊 EcoCycle Analytics")
ride_count = random.randint(1000, 5000)
co2_saved = round(ride_count * 0.3, 2)
avg_speed = round(random.uniform(15, 25), 1)

st.markdown(f"""
- 🚲 **Total Rides**: {ride_count}  
- 🌱 **CO₂ Saved**: {co2_saved} kg  
- ⚡ **Avg. Speed**: {avg_speed} km/h  
""")

# 9. Contact Section
st.header("📞 Contact Us")
st.markdown("""
- 📧 Email: **ecocycleai@domain.com**  
- 📱 Phone: **+91-9876543210**  
- 🌐 Website: [www.ecocycleai.in](https://www.ecocycleai.in)  
""")

st.markdown("---")
st.caption("© 2025 EcoCycle-AI | Developed by Hemamalini L | All rights reserved.")
