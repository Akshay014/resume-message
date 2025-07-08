import streamlit as st

st.set_page_config(page_title="Referral Generator", layout="centered")
st.title("💼 LinkedIn Referral Message Generator")

# ------------------ Persistent User Info ------------------

@st.cache_data(show_spinner=False)
def load_empty_user():
    return {
        "user_name": "",
        "user_role": "",
        "user_intro": "",
    }

if "user_profile" not in st.session_state:
    st.session_state.user_profile = load_empty_user()

def save_user_profile():
    st.session_state.user_profile = {
        "user_name": st.session_state.user_name,
        "user_role": st.session_state.user_role,
        "user_intro": st.session_state.user_intro
    }
    st.success("✅ Profile saved!")

# ------------------ UI: User Info ------------------

st.subheader("👤 Your Profile")
st.text_input("Your Name", value=st.session_state.user_profile["user_name"], key="user_name")
st.text_input("Your Current Role", value=st.session_state.user_profile["user_role"], key="user_role")
st.text_area("Brief Description", value=st.session_state.user_profile["user_intro"], key="user_intro")

st.button("💾 Save My Info", on_click=save_user_profile)

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
