import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    st.chat_message(message["role"], avatar=message["avatar"]).write(message["content"])

prompt = st.chat_input("今天想問什麼💫")
if prompt:
    st.session_state.history.append({"role": "user", "avatar": "🐶", "content": prompt})
    st.rerun()
