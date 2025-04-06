import streamlit as st
import pydeck as pdk
from datetime import datetime

st.set_page_config(page_title="EcoCycle-AI", layout="wide")
st.title("🚴‍♀️ EcoCycle-AI: Smart Cycle Sharing System")
st.markdown("Making transportation smarter, greener, and safer using AI 🌱")

# --- Video Section ---
st.subheader("🎥 How It Works")
st.video("https://www.youtube.com/watch?v=O2gBWyG6v3U")  # Replace with your actual video link

# --- AI-Powered Cycles Images ---
st.subheader("🚲 AI-Powered Smart Cycles")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://i.imgur.com/WrkE0xy.jpg", caption="Cycle with GPS & AI")  # Replace with your own images
with col2:
    st.image("https://i.imgur.com/lBOC6dl.jpg", caption="Real-time Monitoring")
with col3:
    st.image("https://i.imgur.com/SNp5ldN.jpg", caption="Emergency Support Features")

# --- Feature Highlights ---
st.subheader("🌟 Smart Features")
st.markdown("""
- 📍 **GPS Tracking System**  
- 🛰️ **Real-Time Monitoring**  
- 🚨 **Emergency Signal Detection**  
- 🔋 **Battery Status Alerts**  
- 🧠 **AI-Powered Route Optimization (coming soon)**  
""")

# --- Booking System ---
st.subheader("📅 Book Your EcoCycle")
with st.form("booking_form"):
    name = st.text_input("Enter your name")
    pickup_location = st.selectbox("Pickup Location", ["Main Station", "Bus Stop", "Park Entrance"])
    booking_date = st.date_input("Booking Date", datetime.today())
    booking_time = st.time_input("Booking Time", datetime.now().time())
    submit = st.form_submit_button("Confirm Booking")
    if submit:
        st.success(f"Thank you {name}! Your EcoCycle is booked at {pickup_location} on {booking_date} at {booking_time}.")

# --- Emergency Section ---
st.subheader("🚨 Emergency Assistance")
if st.button("Send Emergency Alert"):
    st.error("🚨 Emergency Alert Sent! Help is on the way.")

# --- Live Location Map (Mock GPS) ---
st.subheader("📍 Current Cycle Locations (Demo)")
mock_data = [{"lat": 11.342, "lon": 77.728}]
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/streets-v12',
    initial_view_state=pdk.ViewState(
        latitude=11.342, longitude=77.728, zoom=13,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=mock_data,
            get_position='[lon, lat]',
            get_radius=100,
            get_color='[255, 0, 0, 160]',
            pickable=True,
        )
    ],
))

# --- Contact Info ---
st.sidebar.title("📬 Contact Us")
st.sidebar.markdown("📧 **Email:** hemamalini291204@gmail.com")
st.sidebar.markdown("📞 **Phone:** +91 9876543210")
st.sidebar.markdown("🌐 **Website:** [ecocycle-ai.streamlit.app](https://ecocycle-ai.streamlit.app)")

st.sidebar.markdown("---")
st.sidebar.info("🚀 Powered by AI & Streamlit")
