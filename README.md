# Тема . 
Отчет по Теме # выполнил:
- Факаев Тимур Ранисович
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | 
| Задание 3 | + | 
| Задание 4 | + | 
| Задание 5 | + |


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
### Задание садовник и помидоры

```python
class Tomato:
    states = ['отсутствует', 'цветение', 'зеленый', 'красный']

    def __init__(self, index, state):
        self._index = index
        self._state = state

    def grow(self):
        if self._state < len(self.states) - 1:
            self._state += 1

    def is_ripe(self):
        return self._state == len(self.states) - 1


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index, 0) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        ripe_tomatoes = [tomato for tomato in self.tomatoes if tomato.is_ripe()]
        self.tomatoes = [tomato for tomato in self.tomatoes if not tomato.is_ripe()]
        return ripe_tomatoes

    def __str__(self):
        return f"Куст с {len(self.tomatoes)} помидорами"

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            ripe_tomatoes = self._plant.give_away_all()
            print(f"{self.name} собрал урожай: {len(ripe_tomatoes)} помидоров.")
        else:
            print(f"{self.name}, не все плоды созрели. Подождите еще немного.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: ...")

    def __str__(self):
        return f"Садовод по имени {self.name}"



# Вызов справки по садоводству
Gardener.knowledge_base()


# Создание объектов TomatoBush и Gardener
tomato_bush = TomatoBush(5)
gardener = Gardener("Иван", tomato_bush)
print(tomato_bush)
print(gardener)
# Уход за кустом с помидорами
gardener.work()

# Проверка зрелости томатов
for tomato in tomato_bush.tomatoes:
  print(f"Томат {tomato._index}: {Tomato.states[tomato._state]}")
#
# Попытка сбора урожая, когда томаты еще не дозрели
gardener.harvest()

# Продолжение ухода за кустом
gardener.work()

# Проверка зрелости томатов
for tomato in tomato_bush.tomatoes:
 print(f"Томат {tomato._index}: {Tomato.states[tomato._state]}")

# Продолжение ухода за кустом
gardener.harvest()

# Проверка, что все томаты собраны
if not tomato_bush.tomatoes:
 print("Урожай собран полностью")
 # Т.к томаты не собраны, то ухаживаем за ними еще один круг, проверяем и собираем
gardener.work()
for tomato in tomato_bush.tomatoes:
 print(f"Томат {tomato._index}: {Tomato.states[tomato._state]}")
gardener.harvest()
```
### Результат.
![Меню]( )
![Меню]( )
![Меню]( )
![Меню]( )
![Меню]( )



## Общие выводы по теме
