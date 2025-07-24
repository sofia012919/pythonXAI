---
## 🐍 Python 筆記第二彈（進階也看得懂！）
---

### 📚 字典 Dictionary（像一個查字典的東西）

```python
d1 = {}  # 空字典
d2 = {"apple": "蘋果"}
d3 = {1: "one", 2: "two", 3: "three"}
```

#### 🔎 查找資料

```python
print(d2["apple"])  # 輸出：蘋果
print(d3[2])        # 輸出：two
```

#### 🔁 看所有資料

```python
for key in d3.keys():
    print(key)  # 印出所有「鍵」

for value in d3.values():
    print(value)  # 印出所有「值」

for key, value in d3.items():
    print(f"{key}:{value}")  # 一起看
```

#### ✏️ 增加、修改、刪除

```python
d3[2] = "二"  # 修改
d3[4] = "four"  # 增加新鍵值
v = d3.pop(1)  # 刪除鍵為1的
print(f"刪除的值：{v}")
v = d3.pop(5, "不存在的鍵")  # 沒有就顯示預設文字
```

#### ✅ 判斷有沒有這個鍵

```python
print(2 in d3)  # True
print("three" in d3)  # False（這是值不是鍵）
```

---

### 📁 清單判斷

```python
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)  # True
```

---

## 🖼️ Streamlit 圖片平台（用 Python 做圖文網頁）

### ✅ 顯示圖片列表

```python
import os
import streamlit as st

# 檢查資料夾存在
file_path = "image"
if not os.path.exists(file_path):
    st.error("找不到資料夾")
else:
    valid_exts = [".jpg", ".jpeg", ".png", ".gif"]
    files = [f for f in os.listdir(file_path) if f.endswith(tuple(valid_exts))]
    st.write("找到圖片：", files)

    img_size = st.number_input("請輸入圖片大小", min_value=50, max_value=500, value=300)
    for img in files:
        st.image(os.path.join(file_path, img), width=img_size)
```

---

### 🛒 Streamlit 購物網站

顯示商品、購買商品、補充庫存！

```python
st.title("購物平台")
if "products" not in st.session_state:
    st.session_state.products = {}

# 把圖片變成商品
files = os.listdir("image")
for img in files:
    if img.endswith(".png") and img[:-4] not in st.session_state.products:
        st.session_state.products[img[:-4]] = {
            "image": f"image/{img}",
            "price": 10,
            "stock": 10,
        }

# 顯示商品
cols = st.columns(3)
for i, (name, detail) in enumerate(st.session_state.products.items()):
    with cols[i % 3]:
        st.image(detail["image"], use_container_width=True)
        st.write("商品名稱：" + name)
        st.write("價格：" + str(detail["price"]))
        st.write("庫存：" + str(detail["stock"]))
        if st.button("購買", key=name):
            if detail["stock"] > 0:
                detail["stock"] -= 1
                st.success(f"已購買{name}")
                st.rerun()
            else:
                st.error(f"{name}已售罄")
```

---

## 🔧 函式 Function（可以重複用的小機器）

```python
def hello():
    print("hello")

def hello2(name):
    print("hello " + name)

hello()
hello2("Tom")
```

### ✅ 回傳值的函式

```python
def my_max(a, b):
    if a > b:
        return a
    else:
        return b

print(my_max(10, 20))
```

### ✅ 預設值與參數

```python
def calculate_circle_area(r, pi=3.14, scale=1):
    return r**2 * pi * scale

print(calculate_circle_area(10))
```

---

## 🧠 變數作用範圍（local / global）

```python
length = 10
area = 123

def calculate_square_area1():
    area = length**2
    print("面積是", area)

def calculate_square_area2():
    return length**2

def calculate_square_area3():
    global area
    area = length**2

calculate_square_area1()
print(calculate_square_area2())
calculate_square_area3()
print(area)  # 這裡會被 global 改到
```

---

## 📏 計算距離（座標之間的距離公式）

```python
def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
```

---

## 🎲 投骰子統計

```python
import random

def roll_dice(n):
    result = []
    for i in range(n):
        result.append(random.randint(1, 6))
    return result

outcome = roll_dice(10)

# 數幾次
count = [0, 0, 0, 0, 0, 0]  # 對應1~6
for num in outcome:
    count[num - 1] += 1

for i in range(6):
    print(f"{i+1} 的次數：{count[i]}")
```

---
