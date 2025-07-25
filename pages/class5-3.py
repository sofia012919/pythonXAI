import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("user").write("這是ＡＩ回應")


history = [
    {"role": "user", "content": "請用繁體中文進行後續對話"},
    {"role": "assistant", "content": "你好，我是 Python 小助手！"},
    {"role": "user", "content": "請問st.chat_message()是什麼？"},
    {
        "role": "assistant",
        "content": "st.chat_message()是一個函式，它可以在 Streamlit 中建立聊天對話窗口。",
    },
]


for message in history:

    if message["role"] == "user":
        st.chat_message("user", avatar="🐶").write(message["content"])

    elif message["role"] == "assistant":
        st.chat_message("assistant", avatar="💫").write(message["content"])
