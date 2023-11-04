a = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
a1 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
a2 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

for i in reversed(range(len(a))):
    if a[i] == 2:
        del a[i]
    elif a[i] == 3:
        a[i] = 4
print(a)

for i in reversed(range(len(a1))):
    if a1[i] == 2:
        del a1[i]
    elif a1[i] == 3:
        a1[i] = 4
print(a1)

for i in reversed(range(len(a2))):
    if a2[i] == 2:
        del a2[i]
    elif a2[i] == 3:
        a2[i] = 4
print(a2)
