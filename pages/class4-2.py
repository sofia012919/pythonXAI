import streamlit as st
import os

# 圖片資料夾路徑
file_path = "image"

# 檢查資料夾是否存在
if not os.path.exists(file_path):
    st.error(f"資料夾不存在：{file_path}")
else:
    # 過濾只保留圖片檔案（副檔名檢查）
    valid_exts = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]
    files = [
        f
        for f in os.listdir(file_path)
        if os.path.isfile(os.path.join(file_path, f))
        and os.path.splitext(f)[1].lower() in valid_exts
    ]

    # 顯示圖片清單
    st.write("找到的圖片檔案：", files)

    # 讓使用者輸入顯示大小
    img_size = st.number_input(
        "請輸入圖片大小", step=10, min_value=50, max_value=500, value=300
    )

    # 顯示所有圖片
    for img in files:
        try:
            st.image(os.path.join(file_path, img), width=img_size, caption=img)
        except Exception as e:
            st.warning(f"無法顯示圖片 {img}：{e}")
