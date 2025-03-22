import streamlit as st
import webbrowser

# --- Fake Databases ---
users_db = {}            # {username: password}
user_coins = {}          # {username: coin_balance}
user_referrals = {}      # {username: referrals_count}
user_clicks = {}         # {username: clicks_count}

# --- Session Management ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# ---------------------------
# Sign Up Page
# ---------------------------
def signup_page():
    st.title("Create a New Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        if new_user in users_db:
            st.warning("⚠️ Username already exists! Try another.")
        else:
            # Create new user
            users_db[new_user] = new_pass
            user_coins[new_user] = 0
            user_referrals[new_user] = 0
            user_clicks[new_user] = 0
            st.success("✅ Account created successfully! Please log in now.")

# ---------------------------
# Login Page
# ---------------------------
def login_page():
    st.title("Log In")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        if user in users_db and users_db[user] == password:
            st.session_state.logged_in = True
            st.session_state.username = user
            st.success(f"✅ Welcome, {user}!")
        else:
            st.error("❌ Invalid username or password.")

# ---------------------------
# Settings Page
# ---------------------------
def settings_page():
    st.title("Settings")

    # Theme Change
    theme_choice = st.selectbox("Select Theme", ["Light", "Dark", "Blue"])
    st.session_state.theme = theme_choice
    st.success(f"Theme changed to {theme_choice}!")

    # Withdrawal System
    st.subheader("💸 Withdraw Earnings")
    username = st.session_state.username
    coins = user_coins.get(username, 0)
    refs = user_referrals.get(username, 0)
    clicks = user_clicks.get(username, 0)

    st.write(f"**Your Balance:** {coins} coins")
    st.write(f"**Referrals:** {refs}/10")
    st.write(f"**Clicks:** {clicks}/5")
    st.write("**Minimum:** 15000 coins + 10 referrals + 5 clicks required for withdrawal.")

    if coins >= 15000 and refs >= 10 and clicks >= 5:
        withdraw_amount = st.number_input("Enter amount to withdraw", min_value=15000, max_value=coins, step=500)
        method = st.selectbox("Select Payment Method", ["JazzCash", "EasyPaisa", "Payoneer", "PayPal"])
        if st.button("Request Withdrawal"):
            st.success(f"✅ Withdrawal request of {withdraw_amount} coins via {method} submitted!")
    else:
        st.warning("⚠️ You do not meet the withdrawal requirements yet.")

    # Logout Button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("✅ Logged out successfully!")

# ---------------------------
# Task Page
# ---------------------------
def task_page():
    st.title("🎯 Earn & Win App")

    # Settings Icon (Top Right Corner)
    st.markdown(
        """
        <div style="position: fixed; top: 10px; right: 10px;">
            <a href="?page=settings">
                <img src="https://cdn-icons-png.flaticon.com/512/2099/2099058.png" width="40" />
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("Complete tasks below to earn coins:")

    username = st.session_state.username

    # --- Tasks ---

    # 1) Complete Survey (YouTube Channel + Video)
    if st.button("Complete Survey & Earn"):
        # Open Channel
        webbrowser.open_new_tab("https://www.youtube.com/@ToonCraftStudio-f7o?sub_confirmation=1")
        st.success("Please Subscribe, then watch the video!")
        # After subscription
        if st.button("Watch Video"):
            webbrowser.open_new_tab("https://youtu.be/trr3AC1jiEk?si=CKMZeDaMnLhFRUJ6")
            user_coins[username] += 20
            st.success("✅ You earned 20 coins for completing the survey!")

    # 2) Play Game & Earn
    if st.button("Play Game & Earn"):
        # Free test game link
        webbrowser.open_new_tab("https://poki.com/en/g/gumball-darwin-s-yearbook")
        user_coins[username] += 5
        st.success("✅ You earned 5 coins!")

    # 3) Install App & Earn
    if st.button("Install App & Earn"):
        # Free test app link
        webbrowser.open_new_tab("https://play.google.com/store/apps/details?id=com.spotify.music")
        user_coins[username] += 5
        st.success("✅ You earned 5 coins!")

    # 4) Watch Ads & Earn (Placeholder)
    if st.button("Watch Ads & Earn"):
        st.warning("⚠️ AdSense Approval needed. For now, pretend you watched an ad.")
        user_coins[username] += 5
        st.success("✅ You earned 5 coins for watching ads!")

    # 5) Referral
    if st.button("Refer a Friend & Earn"):
        user_referrals[username] += 1
        user_coins[username] += 5
        st.success("✅ You earned 5 coins for referral!")

    # 6) Click Ads & Earn
    if st.button("Click Ads & Earn"):
        user_clicks[username] += 1
        user_coins[username] += 5
        st.success("✅ You earned 5 coins for clicking ads!")

# ---------------------------
# Navigation Logic
# ---------------------------
def main():
    # Check if user is logged in
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", [""])[0]

    if not st.session_state.logged_in:
        # Show Sign Up / Login options
        choice = st.sidebar.radio("Menu", ["Login", "Sign Up"])
        if choice == "Login":
            login_page()
        else:
            signup_page()
    else:
        if page == "settings":
            settings_page()
        else:
            task_page()

# Run the app
if __name__ == "__main__":
    main()
