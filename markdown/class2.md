## 🐍 Python 是什麼？



---

## 🟢 比大小 & 判斷對不對

我們可以用一些符號來比數字大小或判斷東西是不是一樣的：

```python
print(1 == 1)   # 是不是一樣？→ True
print(1 != 2)   # 是不是不一樣？→ True
print(1 < 2)    # 小於 → True
print(2 > 1)    # 大於 → True
print(1 <= 1)   # 小於或等於 → True
print(2 >= 1)   # 大於或等於 → True
```

---

## 🧠 邏輯判斷（想一想：對 or 錯？）

```python
print(not True)      # 不是對的 → False
print(True and False) # 而且兩個都要對 → False
print(True or False)  # 或，只要一個對就好 → True
```

---

## 🔐 密碼小遊戲

```python
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎ＲＡＹ")
elif password == "5678":
    print("歡迎小艾")
elif password == "91011":
    print("歡迎小明")
else:
    print("密碼錯誤！請再試一次。")
```

---

## 🗓️ 判斷是不是閏年

```python
year = int(input("請輸入年份："))

if year % 400 == 0:
    print("閏年！")
elif year % 100 == 0:
    print("不是閏年！")
elif year % 4 == 0:
    print("閏年！")
else:
    print("不是閏年！")
```

---

## 🖼️ Streamlit：做互動畫面的小工具！

你可以用 `streamlit` 做出漂亮又好玩的按鈕和畫面！

### 🎮 成績分級小程式：

```python
number = st.number_input("請輸入成績", 0, 100, 60)

if number >= 90:
    grade = "A"
elif number >= 80:
    grade = "B"
elif number >= 70:
    grade = "C"
elif number >= 60:
    grade = "D"
else:
    grade = "E"

st.write(f"你的成績是：{grade}")
```

### 🎈 按鈕特效

```python
if st.button("點我！"):
    st.balloons()

if st.button("點我!!"):
    st.snow()
```

---

## 🔁 迴圈（重複做事情）

```python
for i in range(10):
    print(i)  # 印出 0 到 9

for i in range(2, 6):
    print(i)  # 印出 2 到 5

for i in range(2, 10, 2):
    print(i)  # 每次跳2 → 2, 4, 6, 8
```

---

## 🧱 數字金字塔

```python
for i in range(1, input + 1):
    st.write(str(i) * i)
```

輸入 3 會變成：

```
1
22
333
```

---

## 🔺 箭頭金字塔

```python
*
***
*****
*******
   *
   *
   *
```

用程式碼做出漂亮的圖形也可以喔！

---

## 📦 串列（list）就是「東西大集合」

串列就像是一個大箱子，裡面可以放很多東西：

```python
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # 印出第一個：10
print(my_list[2])  # 印出第三個：30

my_list.append(60)  # 加一個新的東西
print(my_list)  # 現在變成 [10, 20, 30, 40, 50, 60]
```

### 🍎 串列裡可以放什麼？

```python
L1 = []  # 空的
L2 = ['蘋果']
L3 = ['蘋果', '香蕉', '橘子']
L4 = [1, 2, 3, 4, 5]
L5 = [1, 2, 3, '蘋果', True, 3.14]
L6 = [1, 2, 3, ['蘋果', '香蕉']]

print(L6[3][0])  # 印出「蘋果」：因為它藏在裡面的小串列裡！
```

### ✂️ 切割串列

```python
L = [1, 2, 3, 'a', 'b', 'c']

print(L[1:4])     # 從第2個到第4個（不含第5個）
print(L[::2])     # 每隔一個拿一個
print(L[1:4:2])   # 從第2個到第4個，每隔一個取 → [2, 'a']
```

---



今天我們學會了：

* 怎麼比大小（==、<、>）
* 怎麼做選擇（if、elif、else）
* 怎麼重複做事（for）
* 怎麼存很多資料（list）
* 怎麼用 streamlit 做出互動介面！