import streamlit as st
import json
import os

st.set_page_config(page_title="Referral Generator", layout="centered")
st.title("💼 LinkedIn Referral Message Generator")

# -------- File to persist user info --------
USER_DATA_FILE = "user_data.json"

# -------- Load cached user data --------
if "user_profile" not in st.session_state:
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            st.session_state.user_profile = json.load(f)
    else:
        st.session_state.user_profile = {
            "user_name": "",
            "user_role": "",
            "user_intro": ""
        }

# -------- User Info Section --------
st.subheader("👤 Your Info")
user_name = st.text_input("Your Name", value=st.session_state.user_profile.get("user_name", ""))
user_role = st.text_input("Your Current Role", value=st.session_state.user_profile.get("user_role", ""))
user_intro = st.text_area("Brief Background", value=st.session_state.user_profile.get("user_intro", ""))

if st.button("💾 Save Info"):
    st.session_state.user_profile = {
        "user_name": user_name,
        "user_role": user_role,
        "user_intro": user_intro
    }
    with open(USER_DATA_FILE, "w") as f:
        json.dump(st.session_state.user_profile, f)
    st.success("✅ Info saved. It'll persist even if you refresh the page.")

# -------- Referral Request Form --------
st.subheader("📨 Referral Request")
recipient_name = st.text_input("Recipient's Name")
job_title = st.text_input("Job Title")
company_name = st.text_input("Company Name")
job_link = st.text_input("Job Link")
job_id = st.text_input("Job ID (Optional)")

# -------- Generate Message --------
if st.button("📋 Generate Message"):
    msg_lines = []

    msg_lines.append(f"Hi {recipient_name},")
    msg_lines.append(
        f"I hope you’re doing well! I came across an exciting opportunity for a {job_title} role at {company_name}, and I noticed that you’re connected with the company. "
        f"Given your experience and position, I was wondering if you’d feel comfortable referring me for the role."
    )
    if job_link:
        msg_lines.append(f"Job Link: {job_link}")
    if job_id:
        msg_lines.append(f"Job ID: {job_id}")
    if user_intro.strip():
        msg_lines.append(f"A quick background about me — {user_intro}")

    msg_lines.append("Please let me know if you need any more information or context from my side.")
    msg_lines.append("Thanks in advance for your support — I truly appreciate it!")
    msg_lines.append("Warm regards,")
    msg_lines.append(user_name)

    final_message = "\n\n".join(msg_lines)
    st.subheader("📎 Copy your message:")
    st.code(final_message, language='markdown')
