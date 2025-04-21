import streamlit as st
import datetime
import random
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="EcoCycle AI", layout="wide")

# --- Title and Hero Image ---
st.title("🚲 EcoCycle AI - Smart Cycle Sharing System")
st.image("https://images.unsplash.com/photo-1595902203456-96caaac5392b", use_column_width=True)
st.markdown("""
EcoCycle is a **solar-powered**, AI-driven smart cycle service that promotes sustainability, accessibility, and tech-enabled convenience.
""")

# --- Video ---
st.header("🎥 Watch How It Works")
st.video("https://youtu.be/fu7VLfcLf6Y")

# --- Features List ---
st.header("🧠 Smart Features")
features = {
    "🧭 AI Route Optimization": "Shortest & safest paths using live traffic data.",
    "♿ Adaptive Tech": "Voice-guidance, pedal/posture support for differently-abled users.",
    "👥 Dual Seating & Safety": "Double seating, seatbelts, rear cam, and bump sensors.",
    "⚠️ SOS Alert System": "One-click emergency alerts nearby help centers.",
    "📍 GPS Live Tracking": "Cycle's real-time location on the map.",
    "🔋 Smart Battery": "Track charge, solar gain, usage pattern.",
    "🎵 Entertainment": "Play music/podcasts during your ride.",
    "📊 Analytics Dashboard": "Speed, distance, CO2 saved, usage heatmaps.",
    "📝 Feedback System": "Collect & analyze user satisfaction.",
    "🏆 Reward System": "Earn green points and convert them into rewards!"
}

for title, desc in features.items():
    st.markdown(f"**{title}** — {desc}")

# --- Booking Form ---
st.header("📅 Book Your EcoCycle")
with st.form("booking"):
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    pickup = st.text_input("Pickup Location")
    drop = st.text_input("Drop Location")
    date = st.date_input("Date", datetime.date.today())
    time = st.time_input("Time", datetime.time(9, 0))
    entertainment = st.selectbox("Entertainment Option", ["None", "Music", "Podcast"])
    needs_voice = st.checkbox("Voice Assistance Needed?")
    submit = st.form_submit_button("🚴 Confirm Booking")

if submit:
    st.success(f"✅ Booking confirmed for {name} on {date} at {time}")
    st.info("Route AI optimized. Voice guidance & entertainment will be active!")

# --- Mock AI Route ---
if pickup and drop:
    route_km = round(random.uniform(2.0, 7.5), 2)
    time_min = int(route_km * random.uniform(4, 6))
    st.metric("🚴 Optimized Route Distance", f"{route_km} km")
    st.metric("⏱️ ETA", f"{time_min} mins")

# --- GPS Live Map ---
st.header("📍 Live GPS Tracking")
location_data = pd.DataFrame({
    'lat': [11.3775 + random.uniform(-0.005, 0.005)],
    'lon': [77.7998 + random.uniform(-0.005, 0.005)]
})

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=11.3775,
        longitude=77.7998,
        zoom=13,
        pitch=50,
    ),
    layers=[pdk.Layer(
        'ScatterplotLayer',
        data=location_data,
        get_position='[lon, lat]',
        get_color='[255, 30, 0, 160]',
        get_radius=100,
    )],
))

# --- Battery Info ---
st.header("🔋 Battery & Solar Recharge")
battery = random.randint(60, 100)
solar = random.randint(5, 15)
st.metric("Battery Level", f"{battery}%", delta=f"+{solar}% Solar")

# --- Emergency Alert ---
st.header("🚨 Emergency SOS")
if st.button("Send Emergency Signal"):
    st.error("🚨 Alert sent to nearest help center!")
    st.balloons()

# --- Voice Assistant Simulation ---
if needs_voice:
    st.header("🗣️ Voice Assistant")
    st.success("Voice Guidance Activated: 'Please start pedaling. Your route is ready!'")

# --- Feedback System ---
st.header("📝 Ride Feedback")
with st.form("feedback"):
    rating = st.slider("Rate your ride", 1, 5, 4)
    comments = st.text_area("Your Feedback")
    fed = st.form_submit_button("Submit Feedback")
    if fed:
        st.success("Thank you for your feedback!")
        if rating <= 2:
            st.warning("We'll improve your experience next time!")

# --- Reward System ---
st.header("🏆 Your Green Rewards")
rides = random.randint(5, 50)
points = rides * 10
st.metric("Total Eco Rides", f"{rides}")
st.metric("Reward Points Earned", f"{points} Points")
if points >= 100:
    st.success("🎁 Redeem now for special offers!")

# --- Real-Time Dashboard ---
st.header("📊 Live Usage Dashboard")
data = pd.DataFrame({
    'Metric': ['Total Rides', 'CO₂ Saved (kg)', 'Avg Speed (km/h)', 'Total Distance (km)'],
    'Value': [
        random.randint(1000, 5000),
        round(random.uniform(200, 1000), 2),
        round(random.uniform(15, 25), 1),
        random.randint(8000, 20000)
    ]
})
st.dataframe(data, use_container_width=True)

# --- Contact Info ---
st.markdown("---")
st.header("📞 Contact Us")
st.markdown("""
**EcoCycle AI Support**  
📧 Email: ecocycleai@domain.com  
📱 Phone: +91-9876543210  
🌐 Website: [www.ecocycleai.in](https://www.ecocycleai.in)
""")

st.caption("Made with 💚 by Hemamalini | Powered by AI & Solar Energy 🚲🌞")
