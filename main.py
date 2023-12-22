import streamlit as st
from mongo import connect, show, delete_word_from_mongo

show_all_data = show()
word = st.text_input("Enter a word")
b1, b2 = st.columns(2)
if b1.button("Save"):
    connect(word)
if b2.button("delete"):
    delete_word_from_mongo(word)


for word in show_all_data:
    st.json(word)
