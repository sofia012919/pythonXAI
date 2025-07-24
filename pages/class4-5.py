import random


def roll_dice(n):

    save = []
    for i in range(n):
        number = random.randint(1, 6)
        save.append(number)
    return save


n = int(input("輸入投骰子次數:"))
outcome = roll_dice(n)

print(f"隨機投出的數字是：", outcome)

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

for num in outcome:
    if num == 1:
        n1 += 1
    elif num == 2:
        n2 += 1
    elif num == 3:
        n3 += 1
    elif num == 4:
        n4 += 1
    elif num == 5:
        n5 += 1
    elif num == 6:
        n6 += 1

print(
    f"1的次數：{n1}  2的次數：{n2}  3的次數：{n3}  4的次數：{n4}  5的次數：{n5}  6的次數：{n6}"
)
