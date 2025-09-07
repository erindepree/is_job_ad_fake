import streamlit as st
import pickle

st.title("Is this Job ad a fake?")
#st.write(
#    "text"
#)
job_ad = st.text_input("Copy and paste the job ad here:", key='job_ad_text')

st.write('WARNING: NOT ACCURATE.  Please return after Sep 9 for a fully functioning version.  Thanks!')


with open('model_log_cv.pkl', 'rb') as f:
    model = pickle.load(f)

if st.button('check if fraud'):
    pred = model.predict(job_ad)[0,1]
    if pred == 1:
        st.write("The model predicts this job ad is fraudulent!")
    else:
        st.write("The model predicts this job ad is legit!")

st.link_button('To read about this model, please visit my GitHub', "https://github.com/erindepree/fake_job_ads")