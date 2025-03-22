import streamlit as st

# Fake database (For storing users, coins, referrals, and clicks)
users_db = {}
user_coins = {"test_user": 20000}  # Example user with 20,000 coins
user_referrals = {"test_user": 10}
user_clicks = {"test_user": 5}

# Session Management
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# 📌 Sign Up Page
def signup():
    st.subheader("🔹 Create a New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if new_user in users_db:
            st.warning("⚠️ Username already exists! Try another.")
        else:
            users_db[new_user] = new_password
            user_coins[new_user] = 0  # New user starts with 0 coins
            user_referrals[new_user] = 0
            user_clicks[new_user] = 0
            st.success("✅ Account created successfully! Now log in.")

# 📌 Login Page
def login():
    st.subheader("🔹 Log In to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if username in users_db and users_db[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"✅ Welcome, {username}!")
        else:
            st.error("❌ Invalid username or password.")

# 📌 Settings Page
def settings():
    st.subheader("⚙ Settings")

    # 🎨 Theme Change
    theme = st.selectbox("🔹 Choose Theme", ["Light", "Dark", "Blue"])
    st.session_state.theme = theme
    st.success(f"✅ Theme changed to {theme}!")

    # 💰 Withdrawal System
    st.subheader("💸 Withdraw Earnings")
    username = st.session_state.username
    coins = user_coins.get(username, 0)
    referrals = user_referrals.get(username, 0)
    clicks = user_clicks.get(username, 0)

    st.write(f"💰 Your Balance: {coins} Coins")
    st.write(f"👥 Referrals: {referrals}/10")
    st.write(f"🖱 Clicks: {clicks}/5")

    if coins >= 15000 and referrals >= 10 and clicks >= 5:
        amount = st.number_input("Enter amount to withdraw", min_value=15000, step=500)
        payment_method = st.selectbox("Select Payment Method", ["JazzCash", "EasyPaisa", "Payoneer", "PayPal"])
        if st.button("Request Withdrawal"):
            st.success(f"✅ Withdrawal request of {amount} coins via {payment_method} submitted!")
    else:
        st.warning("⚠️ Minimum 15,000 coins, 10 referrals, and 5 clicks required for withdrawal.")

    # 🔴 Logout Button
    if st.button("🔴 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("✅ Logged out successfully!")

# 📌 Task Page
def task_page():
    st.title("🎯 Earn & Win Tasks")
    
    # 📌 Settings Icon (Top Right Corner)
    st.markdown(
        """
        <div style="position: fixed; top: 10px; right: 10px;">
            <a href="?page=settings">
                <img src="https://cdn-icons-png.flaticon.com/512/2099/2099058.png" width="40">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("Complete tasks and earn rewards!")

    username = st.session_state.username

    if st.button("🎮 Play & Earn"):
        user_coins[username] += 5
        st.success("✅ You earned 5 coins!")

    if st.button("📥 Install App & Earn"):
        user_coins[username] += 5
        st.success("✅ You earned 5 coins!")

    if st.button("▶️ Watch Ad & Earn"):
        user_coins[username] += 5
        st.success("✅ You earned 5 coins!")

    if st.button("📊 Complete Survey & Earn"):
        user_coins[username] += 20
        st.success("✅ You earned 20 coins!")

    if st.button("🔗 Refer a Friend & Earn 5 Coins"):
        user_referrals[username] += 1
        user_coins[username] += 5
        st.success("✅ You earned 5 coins for a referral!")

    if st.button("🖱 Click Ads & Earn 5 Coins"):
        user_clicks[username] += 1
        user_coins[username] += 5
        st.success("✅ You earned 5 coins for clicking an ad!")

# 📌 Page Navigation
if not st.session_state.logged_in:
    login()
elif "page" in st.session_state and st.session_state.page == "settings":
    settings()
else:
    task_page()
