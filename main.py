import streamlit as st
import webbrowser

st.title("💰 Earn & Win App")

# Survey Button
st.subheader("📊 Complete Survey & Subscribe to Continue")
if st.button("Complete Survey"):
    webbrowser.open_new_tab("https://www.youtube.com/@ToonCraftStudio-f7o")
    st.warning("🔔 Please Subscribe First! Then Click Done.")
    if st.button("Done ✅"):
        st.success("✅ Survey Completed Successfully!")

# Game Play Button
st.subheader("🎮 Play & Earn")
if st.button("Play Game"):
    webbrowser.open_new_tab("https://poki.com/")  # Replace with your earning game link

# App Install Button
st.subheader("📱 Install App & Earn")
if st.button("Install App"):
    webbrowser.open_new_tab("https://play.google.com/store/apps/details?id=com.example")  # Replace with a referral app link

# Ads Watch Button
st.subheader("🎥 Watch Ads & Earn")
if st.button("Watch Ad"):
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=trr3AC1jiEk")  # Replace with Ad link

st.info("✨ Keep using the app and earn more rewards!")
