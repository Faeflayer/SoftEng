# Тема . 
Отчет по Теме # выполнил:
- Факаев Тимур Ранисович
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | + |
| Задание 7 | + | + |
| Задание 8 | + | + |
| Задание 9 | + | + |
| Задание 10 | + | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### 
```python
class vanya:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Иван':
            self.name = f'Да, я {name}'
        else:
            self.name = f'Я не {name}, а Иван'

person1= vanya('Алексей')
person2= vanya('Иван')
print(person1.name)
print(person2.name)

person2.surname = 'Петров'

```
### Результат.
![Меню]( )

## Лабораторная работа №2
### 
```python
class Icecream:
    def __init__(self, ing=None):
        if isinstance(ing, str):
            self.ing = ing
        else:
            self.ing = None

    def comp(self):
        if self.ing:
            print(f'Мороженое с {self.ing}')
        else:
            print('Обычное мороженое')

icecream = Icecream()
icecream.comp()
icecream = Icecream('шоколадом')
icecream.comp()
icecream = Icecream(5)
icecream.comp()
```
### Результат.
![Меню]( )

## Лабораторная работа №3
### 
```python
class Myclass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, 'Свойство value')

obj = Myclass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value()) # ошибка т.к аргумент удален

```
### Результат.
![Меню]( )

## Лабораторная работа №4
### 
```python
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")

cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
```
### Результат.
![Меню]( )

## Лабораторная работа №5
### 
```python
class rus:

    @staticmethod
    def greeting():
        print('Привет')

class eng:

    @staticmethod
    def greeting():
        print('Hello')

def greet(language):
    language.greeting()

ivan = rus()
greet(ivan)
john = eng()
greet(john)

```
### Результат.
![Меню]( )

## Самостоятельная работа №1
###

```python

```
### Результат.
![Меню]( )

## Выводы



## Общие выводы по теме
