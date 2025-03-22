import streamlit as st
import json
import os

# JSON فائل کا نام جہاں یوزر ڈیٹا محفوظ ہوگا
DB_FILE = "users.json"

# یوزر ڈیٹا لوڈ کرنے کا فنکشن
def load_users():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

# یوزر ڈیٹا محفوظ کرنے کا فنکشن
def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)

# ڈیٹا بیس کو لوڈ کریں
users_db = load_users()

# --- Session Management ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

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
            # نیا یوزر بنائیں اور JSON فائل میں محفوظ کریں
            users_db[new_user] = new_pass
            save_users(users_db)
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
# Task Page (Example)
# ---------------------------
def task_page():
    st.title("🎯 Earn & Win Tasks")
    st.write("Welcome, " + st.session_state.username + "!")
    # یہاں مزید ٹاسکس شامل کریں
    if st.button("Test Task: Earn 5 Coins"):
        st.success("✅ Task completed!")

# ---------------------------
# Navigation Logic
# ---------------------------
def main():
    # اگر یوزر لاگ ان نہیں ہے تو Sign Up / Login پیجز دکھائیں
    if not st.session_state.logged_in:
        choice = st.sidebar.radio("Menu", ["Log In", "Sign Up"])
        if choice == "Log In":
            login_page()
        else:
            signup_page()
    else:
        task_page()

if __name__ == "__main__":
    main()
