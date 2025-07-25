import streamlit as st
import openai  # pip install openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "system_message" not in st.session_state:
    st.session_state.system_message = "請用繁體中文進行後續對話"

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"


if "message" not in st.session_state:
    st.session_state.message = []

col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    st.session_state.system_message = st.text_input(
        "系統訊息", st.session_state.system_message
    )
with col2:

    st.selectbox("AI模型", ["gpt-4o-mini", "gpt-4o"])
with col3:
    if st.button("✖️"):
        st.session_state.message = []
        st.rerun()

for message in st.session_state.message:
    # st.chat_message(message["role"], avatar=message["avatar"]).write(message["content"])

    if message["role"] == "user":
        st.chat_message("user", avatar="🐶").write(message["content"])

    elif message["role"] == "assistant":
        st.chat_message("assistant", avatar="💫").write(message["content"])

prompt = st.chat_input("今天想問什麼💫")

if prompt:
    st.session_state.message.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.message,
    )

    assistant_message = response.choices[0].message.content
    st.session_state.message.append({"role": "assistant", "content": assistant_message})
    st.rerun()
