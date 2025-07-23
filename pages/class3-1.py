print(len([]))
print(type(["apple"]))  # <class 'list'>
print(type(["a", "b"]))  # <class 'list'>
print(len([1, 2, 3]))

l = [1, 2, 3]
for i in range(len(l)):
    print(l[i])
print("--" * 20)
l[0] = "a"
l[2] = "c"

print("--" * 20)

for element in l:
    print(element)
print("--" * 20)
a = [10, 20, 30]
b = a[:]
b[1] = 200
print(a)  # [10, 200, 30]

print("--" * 20)
c = [10, 20, 30]
d = c[:]
d[1] = 500
print(c)  # [10, 20, 30]

print("--" * 20)
l1 = [1, 2, 3]
l1.append(4)
print(11)

print("--" * 20)
l2 = ["a", "b", "c", "b", "a"]
l2.remove("b")
print(12)

print("--" * 20)

l3 = [1, 2, 3]
l3.pop(1)
print(14)

print("--" * 20)
l5 = [3, 1, 5, 3.3, 4, 2]
l5.sort

l6 = ["banana", "cherry", "apple"]
l6.sort()
print(l6)  # [1, 2, 3, 3.3
