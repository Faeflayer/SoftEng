import math
#функция
def Math1(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

# максимумы и минимумы
one_min = min(one)
one_max = max(one)
two_min = min(two)
two_max = max(two)
three_min = min(three)
three_max = max(three)

#расчет
triangle1 = Math1(one_min, two_min, three_min)
triangle2 = Math1(one_max, two_max, three_max)


print("Площадь первого треугольника:", triangle1)
print("Площадь второго треугольника:", triangle2)