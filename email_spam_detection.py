# from flask import Flask, render_template, request
# import pickle

# app = Flask(__name__)

# with open(r'C:\Users\abhinandan\Desktop\my_ml_model\model\email_spam_detection.pkl', 'rb') as file:
#     model = pickle.load(file)

# with open(r'C:\Users\abhinandan\Desktop\my_ml_model\model\vectorizer.pkl', 'rb') as file:
#     vectorizer = pickle.load(file)

# @app.route('/')
# def home():
#     return render_template('index7.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         email_text = request.form['email_text']
#         if email_text:
#             email_vec = vectorizer.transform([email_text])
            
#             prediction = model.predict(email_vec)
            
#             result = 'Spam' if prediction[0] == 1 else 'Not Spam'
#             return render_template('index7.html', prediction_text=f'This email is: {result}')
#         else:
#             return render_template('index7.html', prediction_text='Please enter an email to analyze.')

# if __name__ == '__main__':
#     app.run(debug=True)











import streamlit as st
import pickle

# Load model and vectorizer
with open(r'C:\Users\abhinandan\Desktop\my_ml_model\model\email_spam_detection.pkl', 'rb') as file:
    model = pickle.load(file)

with open(r'C:\Users\abhinandan\Desktop\my_ml_model\model\vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Streamlit UI
st.title("Email Spam Detection")

email_text = st.text_area("Enter the email text here:")

if st.button("Predict"):
    if email_text:
        email_vec = vectorizer.transform([email_text])
        prediction = model.predict(email_vec)
        result = 'Spam' if prediction[0] == 1 else 'Not Spam'
        st.success(f"This email is: {result}")
    else:
        st.warning("Please enter an email to analyze.")






