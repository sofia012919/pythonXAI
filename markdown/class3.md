---



### ✅ 列表 List（就像裝東西的盒子）

```python
my_list = ["apple", "banana", "cherry"]
```

* `[]` 表示一個**清單（List）**
* `len()` 可以看清單有幾個東西
* `type()` 可以看變數的種類是不是 list

```python
print(len([]))  # 0，表示裡面沒東西
print(type(["apple"]))  # <class 'list'>
```

---

### 🔁 用 `for` 一個一個看清單裡的東西

```python
l = [1, 2, 3]
for i in range(len(l)):
    print(l[i])  # 用數字當索引，一個一個看

for item in l:
    print(item)  # 用 item 表示每一項
```

---

### ✏️ 改清單裡的內容

```python
l[0] = "a"  # 把第 0 個改成 "a"
l[2] = "c"  # 把第 2 個改成 "c"
```

---

### 🧻 清單的複製與修改

```python
a = [10, 20, 30]
b = a[:]  # 複製一份
b[1] = 200
print(a)  # a 不會被改變
```

---

### 📦 常用的清單功能

```python
l1 = [1, 2, 3]
l1.append(4)  # 加一個東西

l2 = ["a", "b", "c", "b", "a"]
l2.remove("b")  # 把第一個 "b" 移除

l3 = [1, 2, 3]
l3.pop(1)  # 拿掉第 1 個東西

l5 = [3, 1, 5, 3.3, 4, 2]
l5.sort()  # 排序（從小到大）

l6 = ["banana", "cherry", "apple"]
l6.sort()
print(l6)  # ['apple', 'banana', 'cherry']
```

---

### 🧱 while 迴圈：重複做事情

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

- `break` 可以提早停止

```python
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
```

---

### 🎲 `random`：製造隨機的數字

```python
import random
print(random.randrange(0, 10, 2))  # 產生 0~10 間的偶數
print(random.randrange(10, 20))  # 產生 10~19 間的整數
```

---

### 🎰 模擬抽獎機（10 次抽 1\~3 號）

```python
count1 = 0
count2 = 0
count3 = 0

for i in range(10):
    n = random.randrange(1, 4)
    if n == 1:
        count1 += 1
    elif n == 2:
        count2 += 1
    elif n == 3:
        count3 += 1
    print(n)

print(f"1的次數: {count1} 2的次數: {count2} 3的次數: {count3}")
```

---

### 🎯 終極密碼（猜數字遊戲）

```python
target = random.randrange(1, 100)
while True:
    guess = int(input("請猜一個數字(1-100): "))
    if guess < target:
        print("再大一點")
    elif guess > target:
        print("再小一點")
    else:
        print("猜中了!")
        break
```

---

### 🎁 一番賞模擬（抽到就中獎）

```python
table = [0]*100
target = random.randint(1, 100)
table[target - 1] = 1
count = 0

while True:
    pick = random.randint(1, 100)
    count += 1
    if table[pick - 1] == 2:
        print("已經抽過了")
        count -= 1
    elif table[pick - 1] == 1:
        print("恭喜中了一番賞")
        break
    else:
        print("沒中，繼續抽")
        table[pick - 1] = 2

print(f"總共抽了{count}次，花費 {count*200}元")
```

---

### 📱 Streamlit（讓 Python 變成網頁）

#### 顯示按鈕和欄位

```python
import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

#### 顯示輸入框

```python
text = st.text_input("請輸入文字")
st.write("你輸入的文字是:", text)
```

#### session_state 記住資料

```python
if "var1" not in st.session_state:
    st.session_state.var1 = 1

if st.button("加1"):
    st.session_state.var1 += 1
    st.rerun()

st.write(f"現在是: {st.session_state.var1}")
```

---

### 🍔 點餐機（有加入與刪除）

```python
if "order" not in st.session_state:
    st.session_state.order = []

food = st.text_input("請輸入餐點")
if st.button("加入"):
    st.session_state.order.append(food)
    st.rerun()

st.write("購物籃：")
for i in range(len(st.session_state.order)):
    col1, col2 = st.columns([9, 1])
    col1.write(st.session_state.order[i])
    if col2.button("刪除", key=i):
        st.session_state.order.pop(i)
        st.rerun()
```

---
