import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import streamlit as st

@st.cache_resource
def load_model():
    df = pd.read_csv("comments.csv")
    model = Pipeline([
        ('tfidf' , TfidfVectorizer()) ,
        ('classification' , LogisticRegression())
    ])

    model.fit(df['comment'] , df['label'])
    return model

model = load_model()

st.title("this is a youtube comment classifier!")
input = st.text_area("enter a youtube comment: ")

if input:
    prediction = model.predict([input])[0]

    if prediction == "toxic":
        st.error("this comment is toxic!")
    else:
        st.success("this comment is supportive/positive")