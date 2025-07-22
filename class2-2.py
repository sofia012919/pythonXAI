import streamlit as st

# number = st.number_input(
#     "請輸入數字",
#     min_value=0,
#     max_value=100,
#     value=60,
#     step=1,
# )  # 最少跟最多

# st.write(f"你輸入的數字是 {number}")

# '##練習'
# import streamlit as st

# number = st.number_input(
#     "#請輸入成績#",
#     min_value=0,
#     max_value=100,
#     value=60,
#     step=1,
# )

# # 判斷分數等第
# if number >= 90:
#     grade = "***A***"
# elif number >= 80 and number < 90:
#     grade = "***B***"
# elif number >= 70 and   number < 80:
#     grade = "***C***"
# elif number >= 60 and number < 70:
#     grade = "***D***"
# else:
#     grade = "E"

# st.write(f"你的成績等第是：{grade}")

# st.button(f"你的成績等第是：{grade}")
st.button("點我！")  # 按鈕
if st.button("點我"):
    st.balloons()

if st.button("點我!!"):
    st.snow()
