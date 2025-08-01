import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import nltk

nltk.download('punkt')

ps = PorterStemmer()

tfidf = pickle.load(open('Vectorizer.pkl','rb'))
model = pickle.load(open('Model.pkl','rb'))

st.title('Email Spam Classifier')



# 1 preprocess
# 2 vectorize
# 3 predict
# 4 Display


input_sms = st.text_area("Enter the message")

if st.button('Predict'):


    def transform_text(text):
        text = text.lower()
        text = nltk.word_tokenize(text)
        y = []
        for i in text:
            if i.isalnum():
                y.append(i)

        text = y[:]  # to store a list into variable we need to clone it first
        y.clear()

        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)

        text = y[:]
        y.clear()

        for i in text:
            y.append(ps.stem(i))

        return " ".join(y)

    transformed_sms = transform_text(input_sms)

    # 2 vectorize
    vectorize = tfidf.transform([transformed_sms])

    # 3 predict
    result = model.predict(vectorize)[0]

    # dispaly

    if result == 1:
        st.header("Spam")
    else:
        st.header("not Spam")
