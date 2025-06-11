import nltk
import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Load artifacts
model = pickle.load(open("resume_lr_model.pkl", "rb"))
tfidf = pickle.load(open("resume_tfidf.pkl", "rb"))
le = pickle.load(open("resume_label_encoder.pkl", "rb"))

def preprocess(text):
    text = re.sub(r'[^a-zA-Z ]', ' ', text).lower().split()
    return " ".join([stemmer.stem(w) for w in text if w not in stop_words])

st.title("🏷️ Resume Role Classifier")
resume_input = st.text_area("Paste your resume here:")
if st.button("Predict Role"):
    clean = preprocess(resume_input)
    vec = tfidf.transform([clean])
    pred = model.predict(vec)[0]
    st.success(f"Predicted Role: **{le.inverse_transform([pred])[0]}**")




