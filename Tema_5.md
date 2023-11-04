# Тема 5 Базовые коллекции: строки и списки . 
Отчет по Теме #5 выполнил:
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
### Друзья предложили вам поиграть в игру “найди отличия и убери повторения (версия для программистов)”. Суть игры состоит в том, что на вход программы поступает два множества, а ваша задача вывести все элементы первого, которых нет во втором. А вы как раз недавно прошли множества и знаете их возможности, поэтому это не составит для вас труда
```python
set_1 = {'1','3','5','7','9'}
set_2 = {'1','2','3','4','5','6','7','8','9'}
print (set_2-set_1)
```
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/1.png)

## Лабораторная работа №2
### 
```python
a = set('123456789')
print (a)
for i in range(1,5):
   a.add(i)
print(a)
```
```python
a = frozenset('123456789')
print (a)
for i in range(1,5):
   a.add(i)
print(a)
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/2.1.png )
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/2.2.png )

## Лабораторная работа №3
### 
```python
list = ['a', 'b', 'c', 'd', 'e']
list[0], list[-1] = list[-1], list[0]
print(list)
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/3.png )

## Лабораторная работа №4
### 
```python
a = [1,2,3,4,5,6,7,8,9]
print(a[3:6])
```
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/4.png)

## Лабораторная работа №5
### 
```python
def useless(lst):
    return max(lst) / len(lst)
print(useless([2,3,6,2,11]))
print(useless([-12.53,-11,-1,0,-33,83,329,11.22,47]))
print(useless([-23.33,12,1,23,87,82.11,2.22,9,11.22,-1,-2]))
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/5.png )

## Лабораторная работа №6
### 
```python
sheroes = ['batman','spiderman','superman']
ivan,vasya,petya = sheroes
print('Иван -', ivan)
print('Вася -', vasya)
print('Петя -', petya)
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/6.png )

## Лабораторная работа №7
### 
```python
a =[-11.22,-1,2,0,3,55,4,21,2.33]
a.sort()
print('Отсортированный список:\n',a)
a.pop(0)
print('Отсортированный список без наименьшего элемента:\n',a)
```
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/7.png)

## Лабораторная работа №8
### 
```python
from random import randint

def list_maker():
    a = [randint(1,100) for _ in range(randint(3,10))]
    return a

if __name__ == '__main__':
    result = []
    for _ in range(randint(1,5)):
        result.append(list_maker())

    print(result)
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/8.png )

## Лабораторная работа №9
### 
```python
def superset(set_1,set_2):
    if set_1 > set_2:
        print(f'Объект {set_1} является чистым супермножетсвом')
    elif set_1 == set_2:
        print(f'Множества равны:')
    elif set_1 < set_2:
        print(f'Объект {set_2} является чистым супермножетсвом')
    else:
        print ('Супермножетсво не обнаружено')

if __name__ == '__main__':
    superset({1,8,3,5},{3,5})
    superset({1,8,3,5}, {5,3,8,1})
    superset({3,5}, {5,3,8,1})
    superset({90,100}, {3,5})
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/9.png )

## Лабораторная работа №10
### 
```python
my_list = [2,5,8,3]
print(my_list[::-1])
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_5/pics/10.png )




## Самостоятельная работа №1
###

```python

```
### Результат.
![Меню]( )

## Выводы



## Общие выводы по теме
