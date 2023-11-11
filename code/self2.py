def Task(tupl, value):
    if value in tupl
        index = tupl.index(value)
        return tupl[:index] + tupl[index + 1:]
    else:
        return tupl

input1 = (1, 2, 3)
input2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
input3 = (2, 4, 6, 6, 4, 2)
value1 = 1
value2 = 3
value3 = 9

result1 = Task(input1, value1)
result2 = Task(input2, value2)
result3 = Task(input3, value3)

print(result1)
print(result2)
print(result3)
