import streamlit as st
st.set_page_config(page_title="survey", page_icon= ":memo")

st.header ("This is a survey to find which sports is liked  by people of your country")

st.markdown("<h2 style='color: green;'>Please answer the following questions</h2>", unsafe_allow_html=True)

a = st.text_input ("What is your name ? ")

st.write("")

f = st.text_input ("wich is your favorite sport? ")

st.write("")

l = st.text_input ("In which country do you live? ")

st.write("")

if a:
    pass
    st.write("Your name is",a )

st.write("")

if f:
    pass
    st.write ("<>Your favorite sport is",f)

st.write("")

if l:
    pass
    st.write ("You live in",l)

st.write("")

if  l:
    pass
    st.markdown("<h2 style='color: red;'>Thank you for your valueable time!!</h2>", unsafe_allow_html=True)
