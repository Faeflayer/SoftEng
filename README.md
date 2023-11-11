# Тема 6. Базовые коллекции: словари, кортежи. 
Отчет по Теме #6 выполнил:
- Факаев Тимур Ранисович
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |


Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### В школе, где вы учились, узнали, что вы крутой программист и попросили написать программу для учителей, которая будет при вводе кабинета писать для него ключ доступа и статус, занят кабинет или нет. При написании программы необходимо использовать словарь (dict), который на вход получает номер кабинета, а выводит необходимую информацию. Если кабинета, который вы ввели нет в словаре, то в консоль в виде значения ключа нужно вывести "None" и виде статуса вывести "False". По большому счету написав данную программу мы с вами научились заменять иногда громоздкую конструкцию if/elif/else. Поскольку здесь функционал словаря полностью повторяет функционал условия, но при этом у использования словарей в более сложных программах есть намного больше возможностей реализации
```python
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 2999, 'access': True},
    104: {'key': 7070, 'access': False},
    None: {'key': None, 'access': False}
    }
response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_6/pics/lab1.png )

## Лабораторная работа №2
### Алексей решил создать самый большой словарь в мире. Для этого он придумал функцию dict maker (**kwargs), которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my dict, состоящий всего из одного элемента «first» со значением «so easy». Помогите Алексею создать данную функцию. Ниже на скриншоте мы использовали встроенный модуль pprint, который выводит большие объемы информации более понятно для восприятия человеческим глазом. Иногда очень удобно использовать данную возможность Python.
```python
from pprint import pprint

my_dict = {'first': 'so easy'}


def dict_maker(**kwargs):
    my_dict.update(**kwargs)


dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name='Михаил', age=31, weight=70, eyes_color='blue')
pprint(my_dict)
```
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_6/pics/lab2.png)

## Лабораторная работа №3
### Для решения некоторых задач бывает необходимо разложить строку на отдельные символы. Мы знаем что это можно сделать при помощи split(), у которого более гибкая настройка для разделения для этого, но если нам нужно посимвольно разделить строку без всяких условий, то для этого мы можем использовать кортежи (tuple). Для этого напишем любую строку, которую будем делить и "обвернем" ее в tuple и дальше мы можем как нам угодно с ней работать, например, сделать ее списком (тогда получится полный аналог split()) или же работать с ним дальше, как с кортежем.
```python
input_string = 'HelloWorld'
result = tuple(input_string)
print(result)
print(list(result))
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_6/pics/lab3.png )

## Лабораторная работа №4
### Вовочка решил написать крутую функцию, которая будет писать имя, возраст и место работы, но при этом на вход этой функции будет поступать кортеж. Помогите Вовочке написать эту программу.
```python
def personal_info(name, age, company='unnamed'):
    print(f"Name: {name} Age: {age} Company: {company}")


tom = ('Григорий', 22)
personal_info(*tom)

bob = ('Георгий', 41, 'Yandex')
personal_info(*bob)
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_6/pics/lab4.png )

## Лабораторная работа №5
### Для сопровождения первых лиц государства Х нужен кортеж, но никто не может определиться с порядком машин, поэтому вам нужно написать функцию, которая будет сортировать кортеж, состоящий из целых чисел по возрастанию, и возвращает его. Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.
```python
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))


if __name__ == '__main__':
    print(tuple_sort((5, 5, 3, 1, 9)))
    print(tuple_sort((5, 5, 2.1, '1', 9)))
```
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_6/pics/lab5.png)


## Самостоятельная работа №1
### При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных.

```python
req = input("Введите последовательность чисел, разделенных пробелом: ")
list = req.split()
list = [int(num) for num in list]
numbers_tuple = tuple(list)

print("Список:", list)
print("Кортеж:", numbers_tuple)

```
### Результат.
![Меню]( )

## Выводы
1. ` req = input("Введите последовательность чисел, разделенных пробелом: ") `:  req Переменная, которой присвоиться значение от пользователя
2. ` list = req.split()`:  list - список, который создается путем разбития строки req с помощью .split()
3. ` list = [int(num) for num in list] `: Преобразования строковых значений в числовые
4. ` print("Список чисел:", list) `:  Функция вывода сообщения в консоль


## Самостоятельная работа №2
### Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде). Входные данные: (1, 2, 3), 1) (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3) (2, 4, 6, 6, 4, 2), 9) Ожидаемый результат: (2, 3) (1, 2, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2) (2, 4, 6, 6, 4, 2)

```python
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
```
### Результат.
![Меню]( )

## Выводы
Во втором задании код выводит три сообщения с результатами решения поставленной задачи. Каждая строчка кода получилась индивидуальной:
1. ` def Task(tupl, value):  Функция Task с параметрами tupl ( tuple - кортеж ) и value
2. ` if element in tup: `: Условие, если value в tupl..
3. ` index = tupl.index(value) `: Переменной index присваиваем значение. С помощью метода index() присваиваем value индекc
4. ` return tupl[:index] + tupl[index+1:] `. Возвращаем новый созданный кортеж
5. ` return tupl `: Возвращает tupl, если не выполняется условие if




## Общие выводы по теме
