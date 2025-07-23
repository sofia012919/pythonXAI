第一堂課的筆記內容 Ƹ̵Ӝ̵Ʒ

---

# ₊⊹ 我的 Python 程式入門筆記 .ᐟ.ᐟ

## 💡 什麼是變數？

變數就像是一個「裝東西的盒子」，我們可以把數字或文字放進去，也可以換內容！

---

## 🌟 if elif else 判斷閏年

我們可以用 if、elif、else 來判斷某一年是不是閏年：

閏年規則：

1. 如果年份能被 4 整除，可能是閏年。
2. 但如果能被 100 整除又不能被 400 整除，就不是閏年。
3. 如果能被 400 整除，一定是閏年。

範例：

```python
year = 2024
if year % 400 == 0:
    print("閏年！")
elif year % 100 == 0:
    print("不是閏年！")
elif year % 4 == 0:
    print("閏年！")
else:
    print("不是閏年！")
```

你可以把 year 換成你想查的年份，看看結果！

```python
a = 20       # 把數字20放進a盒子
print(a)     # 打開a盒子看看裡面是什麼
a = "apple"  # 把a的內容換成 "apple" 字
print(a)
```

---

## ➕➖✖️➗ 基本數學運算

Python 可以幫我們做加減乘除！

```python
print(7 + 3)   # 加法 → 10
print(7 - 3)   # 減法 → 4
print(7 * 3)   # 乘法 → 21
print(7 / 3)   # 除法 → 2.333...
print(7 % 3)   # 餘數 → 1
print(7 ** 3)  # 7的三次方 → 343
print(7 // 3)  # 只留下整數 → 2
```

---

## 🧮 變數加加減減

我們可以讓變數自己加、自己乘！

```python
x = 4
x = x + 3   # 4 + 3 = 7
x = x * 2   # 7 * 2 = 14
print(x)    # 印出結果 → 14
```

---

## 🧵 文字也能加在一起！

```python
s1 = "hello"
s2 = "world"
print(s1 + s2 * 3)  # hello + worldworldworld
```

還可以用 **f 字串** 拼接文字跟變數：

```python
name = "pythonXAI"
age = 31
msg = f"我是{name}，今年{age}歲"
print(msg)
```

---

## 🔍 看長度、看型態

- `len()`：看文字有幾個字
- `type()`：看這個東西是什麼類型

```python
print(len("hello"))  # → 5

print(type(True))     # 布林值（真假）
print(type(1))        # 整數
print(type(1.0))      # 小數
print(type("hello"))  # 字串
```

---

## 🔁 不同型態轉換

```python
# 布林 → 整數
print(int(True))   # → 1
print(int(False))  # → 0

# 整數 → 小數
print(float(123))  # → 123.0

# 數字/真假/文字 → 字串
print(str(True))     # → "True"
print(str(1000))     # → "1000"
print(str("yes"))    # → "yes"

# 真假判斷（bool）
print(bool(0))       # False（零是假的）
print(bool(1))       # True
print(bool(""))      # False（空字串是假的）
print(bool("hi"))    # True（有字就是真的）
```

---

## 🎤 讓使用者輸入東西

```python
get = input("請輸入內容: ")
print(get)
print(type(get))  # 輸入的東西都是「文字型」喔！
```

---

## 🖥️ Streamlit 畫面顯示（網頁工具）

`streamlit` 是讓我們能把 Python 做成簡單網頁的工具！

```python
import streamlit as st

st.title("這是標題")      # 做出大標題
st.write("這是文字")      # 顯示文字內容
```

---

## 📝 Markdown 美化文字

可以讓內容變漂亮：

```markdown
這是用 markdown 寫的內容

- **粗體字**
- _斜體字_
- [這是連結](https://www.example.com)
- `這是程式碼片段`
```

print("Hello, World!")

```

# 標題一
## 標題二
### 標題三
#### 標題四

- 清單項目1
- 清單項目2
```
