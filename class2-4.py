# 練習
# 這個程式會用 for 迴圈，讓 i 從 1 變到 5
# 每次都把數字 i 變成字串，然後重複 i 次
# 例如 i=3 時，str(3) * 3 就是 "333"
import streamlit as st

st.write("數字金字塔")
input = st.number_input("請輸入一個數字（1-9)", step=1, min_value=1, max_value=9)
st.write("數字金字塔:")
for i in range(1, input + 1):
    st.write(str(i) * i)

st.write("箭頭金字塔")
num2 = st.number_input("請輸入箭頭層數", step=1, min_value=1)
arrow = ""
for i in range(1, num2 + 1):
    if i == 1:
        arrow = arrow + (" " * (num2 - i - 1) + "*" + "\n")
    else:
        arrow = arrow + (" " * (num2 - i) + "*" * (i * 2 - 1) + "\n")
for i in range(num2):
    arrow = arrow + (" " * (num2 - 1) + "*" "\n")
st.write(
    f"""
```
箭頭金字塔：
 {arrow}
``` 
"""
)
