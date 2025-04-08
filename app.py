import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('model/email_spam_detection.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Streamlit UI
st.title("📧 Email Spam Detector")
st.write("Enter your email message below:")

input_text = st.text_area("Message")

if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("Please enter a message.")
    else:
        transformed_text = vectorizer.transform([input_text])
        prediction = model.predict(transformed_text)[0]

        if prediction == 1:
            st.error("🚫 This is a Spam Email!")
        else:
            st.success("✅ This is a Legitimate Email.")
