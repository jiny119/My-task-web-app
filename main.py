import streamlit as st
import webbrowser

st.title("💰 Earn & Win App")

# Complete Survey
st.subheader("📊 Complete Survey & Subscribe to Continue")
st.write("Click the button below to visit and subscribe to continue.")
if st.button("Complete Survey"):
    webbrowser.open_new_tab("https://www.youtube.com/@ToonCraftStudio-f7o")  # Replace with your channel link

# Play Game & Earn
st.subheader("🎮 Play & Earn")
st.write("Play a game and earn rewards!")
if st.button("Play Game"):
    webbrowser.open_new_tab("https://poki.com/")  # Replace with a real earning game link

# Install App & Earn
st.subheader("📱 Install App & Earn")
st.write("Install the app and earn rewards!")
if st.button("Install App"):
    webbrowser.open_new_tab("https://play.google.com/store/apps/details?id=com.tiktok")  # Replace with a real app link

# Watch Ads & Earn
st.subheader("🎥 Watch Ads & Earn")
st.write("Watch ads to earn coins.")
if st.button("Watch Ad"):
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=trr3AC1jiEk")  # Replace with an ad link

st.write("🔗 Share this app with friends & earn more!")
