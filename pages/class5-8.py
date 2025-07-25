import streamlit as st
import openai  # pip install openai
import json
import random

openai.api_key = st.secrets["OPENAI_API_KEY"]

with open("question/quizzes.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    if "pick" not in st.session_state:
        st.session_state.pick = random.randrange(0, len(data))
    quiz = data[st.session_state.pick]


if "system_message" not in st.session_state:
    st.session_state.system_message = "你是一名海龜湯遊戲主持人，只能回答（yes/no/沒什麼關西），如果玩家的描述很接近正解，則輸出遊戲講完正解請用繁體中文進行後續對話\n題目：{quiz['title']}\n正解：{quiz['answer']}"

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o"


if "message" not in st.session_state:
    st.session_state.message = []

st.title("海龜湯")


col1, col2 = st.columns([4, 1])

with col1:

    st.selectbox("AI模型", ["gpt-4o", "gpt-4o-mini"])
with col2:
    if st.button("✖️"):
        st.session_state.message = []
        st.rerun()
st.chat_message("assistant", avatar="💫").write("題目:" + quiz["title"])
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
