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











# import streamlit as st
# import pickle

# # Load model and vectorizer
# with open(r'C:\Users\abhinandan\Desktop\my_ml_model\model\email_spam_detection.pkl', 'rb') as file:
#     model = pickle.load(file)

# with open(r'C:\Users\abhinandan\Desktop\my_ml_model\model\vectorizer.pkl', 'rb') as file:
#     vectorizer = pickle.load(file)

# # Streamlit UI
# st.title("Email Spam Detection")

# email_text = st.text_area("Enter the email text here:")

# if st.button("Predict"):
#     if email_text:
#         email_vec = vectorizer.transform([email_text])
#         prediction = model.predict(email_vec)
#         result = 'Spam' if prediction[0] == 1 else 'Not Spam'
#         st.success(f"This email is: {result}")
#     else:
#         st.warning("Please enter an email to analyze.")






# import streamlit as st
# import pickle

# # Load model and vectorizer
# model = pickle.load(open('C:/Users/abhinandan/Desktop/Deploy_model/email_spam_detection.pkl', 'rb'))
# vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# # Streamlit UI
# st.title("📧 Email Spam Detector")
# st.write("Enter your email message below:")

# input_text = st.text_area("Message")

# if st.button("Predict"):
#     if input_text.strip() == "":
#         st.warning("Please enter a message.")
#     else:
#         transformed_text = vectorizer.transform([input_text])
#         prediction = model.predict(transformed_text)[0]
        
#         if prediction == 1:
#             st.error("🚫 This is a Spam Email!")
#         else:
#             st.success("✅ This is a Legitimate Email.")







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
