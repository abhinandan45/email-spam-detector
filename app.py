import streamlit as st
import pickle

model = pickle.load(open('model/email_spam_detection.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.set_page_config(page_title="Email Spam Detector", page_icon="📧", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f4f6f8;
        padding: 20px;
        border-radius: 12px;
    }
    .stTextArea textarea {
        background-color: #ffffff;
        border-radius: 10px;
        font-size: 16px;
        padding: 15px;
    }
    .stButton>button {
        background-color: #6366f1;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #4f46e5;
    }
    footer {
        visibility: hidden;
    }
    .custom-footer {
        margin-top: 50px;
        text-align: center;
        font-size: 16px;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4f46e5;'>📧 Email Spam Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Check if your email is Spam or Legitimate</p>", unsafe_allow_html=True)

input_text = st.text_area("✉️ Paste your email message here:")

if st.button("🔍 Detect"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        transformed_text = vectorizer.transform([input_text])
        prediction = model.predict(transformed_text)[0]

        if prediction == 1:
            st.error("🚫 This is a **Spam** Email!")
        else:
            st.success("✅ This is a **Legitimate** Email.")

st.markdown(
    "<div class='custom-footer'>Made with ❤️ by <b>Abhinandan Rajput</b></div>",
    unsafe_allow_html=True
)

