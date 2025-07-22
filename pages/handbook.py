import streamlit as st

with st.expander("class1 課堂筆記"):
    st.write(
        """

    第一堂課的筆記內容 Ƹ̵Ӝ̵Ʒ      

    ---

    # ₊⊹我的 Python 程式入門筆記  .ᐟ.ᐟ   

    ## 💡什麼是變數？

    變數就像是一個「裝東西的盒子」，我們可以把數字或文字放進去，也可以換內容！

    ---

    ## 🌟 if elif else 判斷閏年

    我們可以用 if、elif、else 來判斷某一年是不是閏年：

    閏年規則：
    1. 如果年份能被4整除，可能是閏年。
    2. 但如果能被100整除又不能被400整除，就不是閏年。
    3. 如果能被400整除，一定是閏年。

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

    還可以用 **f字串** 拼接文字跟變數：

    ```python
    name = "pythonXAI"
    age = 31
    msg = f"我是{name}，今年{age}歲"
    print(msg)
    ```

    ---

    ## 🔍 看長度、看型態

    * `len()`：看文字有幾個字
    * `type()`：看這個東西是什麼類型

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
    * **粗體字**  
    * *斜體字*  
    * [這是連結](https://www.example.com)  
    * `這是程式碼片段`  

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

    ---


    
            """
    )

with st.expander("class2 課堂筆記"):
    st.write(
        """
    

---

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




    """
    )
