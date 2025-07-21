# a = 20  # 建立變數
# print(a)  # 輸出變數
# a = 30  # 變更變數值
# print(a)  # 輸出變數
# a = "apple"  # 變更變數為字串
# print(a)
# x = 4
# x = x + 3
# print(x)
# x = x * 2
# print(x)  # 輸出變數
# print(7 + 3)  # 加法
# print(7 - 3)  # 減法
# print(7 * 3)  # 乘法
# print(7 / 3)  # 除法
# print(7 % 3)  # 輸出餘數
# print(7**3)  # 冪運算
# print(7 // 3)  # 整數除法
# v1 = 0.1
# v2 = 0.2
# print(v1 + v2)  # 浮點數加法
# s1 = "hello"
# s2 = "world"
# print(s1 + s2 * 3)  # 字串連接
name = "pythonXAI"  # 建立字串變數
age = 31  # 建立整數變數
ne_str = f"我是{name}今年{age}歲"
print(ne_str)  # 輸出字串變數

print(len(""))
print(len("hello"))

print(type(True))  # 呼叫函數並傳遞參數
print(type(1))  # 輸出整數類型
print(type(1.0))  # 輸出浮點數類型
print(type("hello"))  # 輸出字串類型

print(int(True))
print(int(123))  # 將布林值轉換為整數

print(float(True))
print(float(123))  # 將整數轉換為浮點數

print(bool(0))  # fales
print(bool(1))  # True
print(bool(-2))  # True
print(bool(""))  # True
print(bool("hello"))  # false

print(str(True))
print(str(1000))  # 將布林值轉換為字串
print(str("yes"))  # 將浮點數轉換為字串

# get = input()
get = input("請輸入內容: ")  # 等待使用者輸入
print(get)
print(type(get))


r = input("請輸入圓的半徑")  # 等待使用者輸入
r = int(r)
area = 3.14 * r**2
print(f"圓的面積為: {area}")  # 輸出圓的面積
print(f"圓的面積為: {area}")
print("圓的面積為:", area)
