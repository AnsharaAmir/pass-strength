''' import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase and lowercase
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Check for digits
    if any(c.isdigit() for c in password)::
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    # Check for special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Assign strength level
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score in [3, 4]:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, score, feedback, color

# Streamlit UI
st.title("🔒 Password Strength Meter")

# User Input
password = st.text_input("Enter your password", type="password")

if password:
    strength, score, feedback, color = check_password_strength(password)

    # Display result
    st.markdown(f"### Password Strength: <span style='color:{color}; font-size:24px'>{strength} (Score: {score}/5)</span>", unsafe_allow_html=True)

    # Display feedback
    if feedback:
        st.warning("Suggestions to improve:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")  '''



import streamlit as st
import re
import pandas as pd
import os
from io import BytesIO


def check_password_strength(password):
    score = 0
    feedback = []
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase and lowercase
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    # Check for special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 2
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    

    # Assign strength level
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score in [3, 4]:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, score, feedback, color

st.set_page_config(page_title="🔐Password Strength Meter", layout='wide')
st.title("🔐Password Strength Meter")
st.write("Learn how to create strong passwords, and get evaluated by reviews!")
password = st.text_input("Enter a strong password" , type="password")
st.subheader("📜Instructions:")
"* Password must contain eight letters."
"* Contains both, uppercase and lowercase letters."
"* Indlude atleast one digit (0-9)."
"* Have one special character (!@#$#%^&*)"

if password:
    strength, score, feedback, color = check_password_strength(password)

    # Display result
    st.markdown(f"### Password Strength: <span style='color:{color}; font-size:24px'>{strength} (Score: {score}/5)</span>", unsafe_allow_html=True)

    # Display feedback
    if feedback:
        st.warning("Suggestions to improve:")
        for suggestion in feedback:
            st.write(f"- {suggestion}") 