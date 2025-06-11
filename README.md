# 🏷️ Resume Role Classifier  

## 📌 Project Overview

**Resume Role Classifier** is a powerful and intuitive machine learning application designed to predict the most suitable job role for a candidate based on their resume content. Leveraging **Natural Language Processing (NLP)** techniques and a **Logistic Regression** classifier, this web app processes raw resume text and accurately classifies it into predefined job categories.

🧠 Built using:

- Scikit-learn for ML Modeling
- TF-IDF for feature extraction
- NLTK for text preprocessing
- Streamlit for interactive web UI
- Pickle for model deployment
- Heroku-ready for cloud deployment

## 🧰 Features

✅ Clean UI for resume input via Streamlit  
✅ Text preprocessing with NLTK (tokenization, stopword removal, stemming)  
✅ Role classification using a trained Logistic Regression model  
✅ Real-time prediction and result display  
✅ Deployable on cloud (Heroku/Streamlit-ready)  

## 🧠 How It Works

1. **Input Resume Text**: User pastes raw resume text into the app.
2. **Preprocessing**:
   - Lowercasing
   - Removing special characters
   - Removing stopwords
   - Stemming with PorterStemmer
3. **Vectorization**: TF-IDF vectorizer converts the cleaned text into numerical form.
4. **Prediction**: Logistic Regression model predicts the job category.
5. **Output**: Predicted role is shown to the user.

## 📁 Project Structure

## 📁 Project Structure

```
| File/Folder Name              | Description                                      |
|------------------------------|--------------------------------------------------|
| resume_lr_model.pkl          | Trained Logistic Regression model               |
| resume_tfidf.pkl             | TF-IDF Vectorizer used for feature extraction   |
| resume_label_encoder.pkl     | Label Encoder for mapping roles to integers     |
| UpdatedResumeDataSet.csv     | Dataset used for training and evaluation        |
| streamlit_app.py             | Main Streamlit app script                       |
