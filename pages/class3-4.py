i = 0
while i < 5:
    print(i)
    i += 1

print("--" * 20)
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1

print("-" * 20)
for i in range(5):
    if i == 3:
        break
    print(i)

import random

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
print(f"1的次數: {count1}   2的次數: {count2} 3的次數: {count3}")
print("--" * 20)
print(random.randrange(0, 10, 2))
print(random.randrange(10, 20))
