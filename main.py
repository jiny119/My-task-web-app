import streamlit as st
import webbrowser

# ایپ کا نام
st.title("💰 Earn & Win App")

# 🎯 Survey Button (YouTube Channel & Video)
st.subheader("📊 Complete Survey & Subscribe to Continue")
st.write("Click the button below to visit and subscribe to continue.")
if st.button("Complete Survey"):
    webbrowser.open_new_tab("https://www.youtube.com/@ToonCraftStudio-f7o?sub_confirmation=1")  
    # "?sub_confirmation=1" سے چینل کھلتے ہی سبسکرائب بٹن شو ہوگا

st.success("✅ Survey Completed Successfully!")  # سبسکرائب کنفرمیشن

# 🎮 Game Play Button
st.subheader("🎮 Play Game & Earn")
st.write("Play a game and earn rewards!")
if st.button("Play Game"):
    webbrowser.open_new_tab("https://poki.com/")  # اصل گیم کا لنک

# 📲 App Install Button
st.subheader("📱 Install App & Earn")
st.write("Install the app and earn rewards!")
if st.button("Install App"):
    webbrowser.open_new_tab("https://play.google.com/store/apps/details?id=com.tiktok")  # اصل ریفرل ایپ لنک

# 🎥 Watch Ads Button (بعد میں AdSense کے لنکس لگیں گے)
st.subheader("🎥 Watch Ads & Earn")
st.write("Watch ads to earn coins.")
if st.button("Watch Ad"):
    st.warning("⚠️ AdSense Approval کے بعد Ads چلیں گے!")

st.write("🔗 [Share this app with friends & earn more!](#)")
