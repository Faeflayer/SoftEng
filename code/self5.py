list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

set_1 = set()
set_2 = set()
set_3 = set()

for num in list_1:
    str_num = str(num)
    set_1.add(num)
    for i in range(2, num + 1):
        set_1.add(str_num * i)

for num in list_2:
    str_num = str(num)
    set_2.add(num)
    for i in range(2, num + 1):
        set_2.add(str_num * i)

for num in list_3:
    str_num = str(num)
    set_3.add(num)
    for i in range(2, num + 1):
        set_3.add(str_num * i)


print(set_1)
print(set_2)
print(set_3)