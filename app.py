import streamlit as st
import json
import os

st.set_page_config(page_title="Referral Generator", layout="centered")
st.title("💼 LinkedIn Referral Message Generator")

USER_DATA_FILE = "user_data.json"

# Load saved user data from file if available
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {"user_name": "", "user_role": "", "user_intro": ""}

# Save user data to file
def save_user_data(data):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f)

# Initialize session_state with saved data
if "user_profile" not in st.session_state:
    st.session_state.user_profile = load_user_data()

# ------------------ UI: User Info ------------------
st.subheader("👤 Your Profile")

st.text_input("Your Name", key="user_name", value=st.session_state.user_profile.get("user_name", ""))
st.text_input("Your Current Role", key="user_role", value=st.session_state.user_profile.get("user_role", ""))
st.text_area("Brief Description", key="user_intro", value=st.session_state.user_profile.get("user_intro", ""))

def handle_save():
    st.session_state.user_profile = {
        "user_name": st.session_state.user_name,
        "user_role": st.session_state.user_role,
        "user_intro": st.session_state.user_intro
    }
    save_user_data(st.session_state.user_profile)
    st.success("✅ Profile saved!")

st.button("💾 Save My Info", on_click=handle_save)

# ------------------ Referral Input ------------------
st.subheader("📨 Referral Info")

recipient_name = st.text_input("Recipient's Name*", placeholder="e.g., John")
job_title = st.text_input("Job Title*", placeholder="e.g., Backend Engineer")
company_name = st.text_input("Company Name*", placeholder="e.g., Google")
job_link = st.text_input("Job Link*", placeholder="https://...")
job_id = st.text_input("Job ID (optional)")
resume_link = st.text_input("Resume Link (optional)")

# ------------------ Generate ------------------

if st.button("✨ Generate Message"):
    if not all([recipient_name, job_title, company_name, job_link]):
        st.warning("Please fill all required fields marked with *")
    else:
        job_id_line = f"Job ID: {job_id}" if job_id.strip() else ""
        resume_line = f"Here is my resume for reference: {resume_link}" if resume_link.strip() else ""

        intro = st.session_state.user_intro.strip()
        name = st.session_state.user_name.strip()

        message_parts = [
            f"Hi {recipient_name},",
            f"I hope you’re doing well! I came across an exciting opportunity for a {job_title} role at {company_name}, and I noticed that you’re connected with the company. Given your experience and position, I was wondering if you’d feel comfortable referring me for the role.",
            f"Job Link: {job_link}",
            job_id_line,
            f"A quick background about me — {intro}" if intro else "",
            resume_line,
            "Please let me know if you need any more information or context from my side.",
            "Thanks in advance for your support — I truly appreciate it!",
            f"Warm regards,\n{name}"
        ]

        final_message = "\n\n".join([line for line in message_parts if line.strip()])
        st.success("Referral message generated! ✅")
        st.text_area("📋 Copy your message:", final_message, height=350)
