import streamlit as st
import pickle

st.title("Is this Job ad a fake?")
#st.write(
#    "text"
#)
job_ad = st.text_input("Copy and paste the job ad here:", key='job_ad_text')

#with open('model_tfidf.pickle', 'rb') as f:
#    model = pickle.load(f)

if st.button('check if fraud'):
    pred = 1 #model.predict(job_ad)
    if pred == 1:
        st.write("The model predicts this job ad is fraudulent!")
    else:
        st.write("The model predicts this job ad is legit!")

st.link_button('To read about this model, please visit my GitHub', "https://github.com/erindepree/fake_job_ads")