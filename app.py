import streamlit as st
import json

st.set_page_config(page_title="LinkedIn Referral Generator", layout="centered")
st.title("💼 LinkedIn Referral Message Generator")

st.markdown("Easily create a professional referral message for LinkedIn.")

# ------------------ Persistent Profile (JSON) ------------------
st.subheader("👤 Your Profile")

# Try to load saved profile
profile = {
    "user_name": "",
    "user_role": "",
    "user_intro": ""
}

uploaded_profile = st.file_uploader("Upload saved profile (optional)", type=["json"])
if uploaded_profile:
    profile.update(json.load(uploaded_profile))

profile["user_name"] = st.text_input("Your Full Name", value=profile["user_name"])
profile["user_role"] = st.text_input("Current Role", value=profile["user_role"])
profile["user_intro"] = st.text_area("Brief Description", value=profile["user_intro"])

# Option to download profile
st.download_button("💾 Save Profile", data=json.dumps(profile), file_name="profile.json", mime="application/json")

# ------------------ Referral Form ------------------
st.subheader("📨 Referral Details")

recipient_name = st.text_input("Recipient's Name*", placeholder="e.g., John")
job_title = st.text_input("Job Title*", placeholder="e.g., Backend Engineer")
company_name = st.text_input("Company Name*", placeholder="e.g., Google")
job_link = st.text_input("Job Link*", placeholder="Paste the job URL")
job_id = st.text_input("Job ID (optional)", placeholder="Optional")
resume_link = st.text_input("Resume Link (optional)", placeholder="Google Drive or other URL")

brief_intro = st.text_area("Brief Intro*", value=profile["user_intro"])

# ------------------ Message Generator ------------------
if st.button("Generate Referral Message"):
    if not (recipient_name and job_title and company_name and job_link and brief_intro):
        st.warning("⚠️ Please fill all required fields marked with *")
    else:
        # Cleanly format optional fields
        job_id_line = f"\nJob ID: {job_id}" if job_id.strip() else ""
        resume_line = f"\nHere is my resume for reference: {resume_link}" if resume_link.strip() else ""

        sender_name = profile["user_name"] or "Akshay Gupta"

        message_parts = [
            f"Hi {recipient_name},\n",
            f"I hope you’re doing well! I came across an exciting opportunity for a {job_title} role at {company_name}, and I noticed that you’re connected with the company. Given your experience and position, I was wondering if you’d feel comfortable referring me for the role.",
            f"\nJob Link: {job_link}",
            job_id_line,
            f"\n\nA quick background about me — {brief_intro.strip()}",
            resume_line,
            "\n\nPlease let me know if you need any more information or context from my side.",
            "Thanks in advance for your support — I truly appreciate it!",
            f"\nWarm regards,\n{sender_name}"
        ]

        # Filter out empty lines
        message = "\n".join([part.strip() for part in message_parts if part.strip()])

        st.success("Referral Message Generated! ✨")
        st.text_area("📋 Copy your message:", value=message, height=350)
        st.code(message, language="markdown")
