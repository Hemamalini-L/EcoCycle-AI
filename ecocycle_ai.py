import streamlit as st
import datetime

# Set page configuration
st.set_page_config(page_title="EcoCycle-AI", layout="wide")

# 1. Welcome & Topic
st.title("🚴 EcoCycle-AI: Revolutionizing Urban Mobility with AI")
st.markdown("""
Welcome to **EcoCycle-AI**, your smart AI-powered cycle sharing platform. Designed with the latest in AI, IoT, and smart mobility, it ensures **efficiency**, **safety**, and **accessibility for all**, including differently-abled users.
""")

# 2. Picture
st.image("revolution-white-x-1024x670.jpg", caption="AI-Powered EcoCycle", use_column_width=False, width=500)

# 3. Video Tutorial
st.header("📽️ How It Works")
st.video("https://youtu.be/fu7VLfcLf6Y?si=srYur4nDvoev8JQe")

# 4. Booking Details
st.header("📅 Book Your EcoCycle")
with st.form("booking_form"):
    name = st.text_input("Full Name")
    date = st.date_input("Booking Date", datetime.date.today())
    pickup = st.text_input("Pickup Location")
    drop = st.text_input("Drop Location")
    duration = st.selectbox("Rental Duration", ["30 mins", "1 hour", "2 hours", "Whole Day"])
    submitted = st.form_submit_button("Confirm Booking")
    if submitted:
        st.success(f"Booking confirmed for {name} on {date} from {pickup} to {drop} for {duration}.")

# 5. Show Booking Status
if submitted:
    st.info("Your booking is confirmed. You will receive a notification and cycle unlock code via email.")

# 6. Live GPS Location (Demo)
st.header("📍 Live Location & GPS")
st.map({"lat": [11.3410], "lon": [77.7172]})  # Sample location

# 7. Emergency Button
st.header("🆘 Emergency Assistance")
if st.button("Raise Emergency Alert"):
    st.warning("Emergency alert sent to nearest support team and your emergency contact.")

# 8. Estimated Time Based on Traffic (Mock)
st.header("⏱️ ETA Based on Real-Time Traffic")
st.info("Estimated Time from Pickup to Drop: 18 mins (Based on current traffic)")

# 9. Battery & Charging
st.header("🔋 Battery Status")
st.progress(0.7, text="Battery Level: 70% - Sufficient for 20km ride")

# 10. Contact
st.header("📞 Contact Us")
st.markdown("""
- 📧 Email: ecocyclesupport@gmail.com  
- 📱 Phone: +91-9876543210
""")

# 11. Details from Presentation
st.header("💡 What Makes EcoCycle-AI Unique")
st.markdown("""
- AI-powered route optimization for safer & smarter travel.
- Inclusive design for differently-abled riders.
- Seamless local transport integration (buses, metro).
- Real-time tracking & emergency support.
- Sustainable & scalable for smart cities.
""")

# 12. Feedback System
st.header("🗣️ Give Feedback")
feedback = st.text_area("Share your experience or suggestions")
if st.button("Submit Feedback"):
    st.success("Thank you! Your feedback is valuable to us.")

# 13. Local Transport Integration
st.header("🚎 Connected with City Transport")
st.markdown("""
Plan your journey with EcoCycle-AI and switch to metro or bus without hassle. We provide location-aware station info & multi-modal route planning.
""")

# 14. Payment Options
st.header("💳 Payment Options")
st.markdown("""
- UPI / Google Pay / PhonePe
- Credit/Debit Cards
- Wallets
- Subscription models for regular users
""")

# 15. Weather Detection
st.header("☁️ Weather Conditions")
st.info("Weather: Cloudy | Temperature: 29°C | Ride Status: Safe to Ride")  # Mock data

# 16. Parking Availability
st.header("🅿️ Nearby Parking Spots")
st.markdown("""
- Station 1 (300m) - 6 cycles available
- Station 2 (500m) - 2 cycles available
""")

# 17. Traffic Management
st.header("🚦 Smart Traffic Alerts")
st.warning("Heavy traffic near Main Street. Recommended alternate route: via Park Avenue.")

# 18. Issue Identification
st.header("⚙️ Report an Issue")
issue = st.text_input("Report any issue with the cycle or app")
if st.button("Submit Issue"):
    st.success("Thanks! We’ll address it immediately.")

# Footer
st.markdown("---")
st.markdown("© 2025 EcoCycle-AI | Developed by Hemamalini L")

