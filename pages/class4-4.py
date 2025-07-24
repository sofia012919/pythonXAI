def hello():
    print("hello")


def hello2(name):
    print(f"hello" + name)


hello()
hello()


def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def calculate_circle_area(r, pi=3.14, scale=1):
    return r**2 * pi


hello()
hello2("Tom")
print(my_max(10, 20))
print(calculate_circle_area(10))
print(calculate_circle_area(10, scale=2))
print(calculate_circle_area(10, 3.1415926, 2))


print("-" * 10)

length = 5
area = 123


def calculate_square_area1():
    area = length**2
    print("面積是", area)


def calculate_square_area2():
    area = length**2
    return area


def calculate_square_area3():
    global area
    area = length**2


length = 10
calculate_square_area1()
print(calculate_square_area2())
calculate_square_area3()
print(area)

print("-" * 10)


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x1 = int(input("請輸入x1:"))
y1 = int(input("請輸入y1:"))
x2 = int(input("請輸入x2:"))
y2 = int(input("請輸入y2:"))


print(distance(x1, y1, x2, y2))
