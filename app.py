import streamlit as st

st.set_page_config(page_title="LinkedIn Referral Message Generator", layout="centered")

st.title("💼 LinkedIn Referral Message Generator")

# ----- Initialize user profile in session state -----
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_role' not in st.session_state:
    st.session_state.user_role = ""
if 'user_intro' not in st.session_state:
    st.session_state.user_intro = ""

# ----- User Profile Section -----
with st.expander("👤 Your Profile (optional, auto-fills future forms)", expanded=True):
    st.session_state.user_name = st.text_input("Your Full Name", value=st.session_state.user_name)
    st.session_state.user_role = st.text_input("Current Role", value=st.session_state.user_role, placeholder="e.g., Cloud Engineer at Sprinklr")
    st.session_state.user_intro = st.text_area("Brief Description", value=st.session_state.user_intro, placeholder="Write a quick intro you want in every referral")

# ----- Referral Form Section -----
st.subheader("🔗 Referral Request Details")

recipient_name = st.text_input("Recipient's Name*", placeholder="e.g., John")
job_title = st.text_input("Job Title*", placeholder="e.g., Backend Engineer")
company_name = st.text_input("Company Name*", placeholder="e.g., Google")
job_link = st.text_input("Job Link*", placeholder="Paste the job URL")
job_id = st.text_input("Job ID (optional)", placeholder="Optional")
resume_link = st.text_input("Resume Link (optional)", placeholder="Google Drive or other URL")

# Pre-fill intro from profile
brief_intro = st.text_area("Brief Intro*", value=st.session_state.user_intro)

# ----- Generate Referral Message -----
if st.button("Generate Referral Message"):
    if not (recipient_name and job_title and company_name and job_link and brief_intro):
        st.warning("⚠️ Please fill all required fields marked with *")
    else:
        job_id_line = f"\nJob ID: {job_id}" if job_id.strip() else ""
        resume_line = f"\nHere is my resume for reference: {resume_link}" if resume_link.strip() else ""

        sender_name = st.session_state.user_name or "Akshay Gupta"  # fallback if not filled

        message = f"""
Hi {recipient_name},

I hope you’re doing well! I came across an exciting opportunity for a {job_title} role at {company_name}, and I noticed that you’re connected with the company. Given your experience and position, I was wondering if you’d feel comfortable referring me for the role.

Job Link: {job_link}{job_id_line}

A quick background about me — {brief_intro.strip()}

{resume_line}

Please let me know if you need any more information or context from my side.

Thanks in advance for your support — I truly appreciate it!

Warm regards,  
{sender_name}
"""

        st.success("Referral Message Generated! ✨")
        st.text_area("📋 Copy your message below:", value=message, height=300)
        st.code(message, language="markdown")
