import streamlit as st
from streamlit_javascript import st_javascript
import json

st.set_page_config(page_title="Referral Generator", layout="centered")
st.title("💼 LinkedIn Referral Message Generator")

# Step 1: Try reading from browser cookie
cookie = st_javascript("document.cookie") or ""
user_profile = {"user_name": "", "user_role": "", "user_intro": ""}

try:
    cookie_pairs = [c.strip().split("=") for c in cookie.split(";")]
    cookie_dict = {k: v for k, v in cookie_pairs if len(k) > 1}
    if "referral_data" in cookie_dict:
        user_profile = json.loads(cookie_dict["referral_data"])
except Exception as e:
    st.error("Failed to load cookies")

# Step 2: User Profile Section
st.subheader("👤 Your Info")
user_name = st.text_input("Your Name", value=user_profile.get("user_name", ""))
user_role = st.text_input("Your Current Role", value=user_profile.get("user_role", ""))
user_intro = st.text_area("Brief Background", value=user_profile.get("user_intro", ""))

if st.button("💾 Save Info"):
    save_data = json.dumps({
        "user_name": user_name,
        "user_role": user_role,
        "user_intro": user_intro
    }).replace("'", "\\'")
    st_javascript(f"document.cookie = 'referral_data={save_data}; path=/'")
    st.success("✅ Saved to your browser. Will persist across refreshes.")

# Step 3: Referral Form Inputs
st.subheader("📨 Referral Request")
recipient_name = st.text_input("Recipient's Name")
job_title = st.text_input("Job Title")
company_name = st.text_input("Company Name")
job_link = st.text_input("Job Link")
job_id = st.text_input("Job ID (Optional)")

# Step 4: Generate Message
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
