# Тема 7 Работа с файлами (ввод, вывод). 
Отчет по Теме #7 выполнил:
- Факаев Тимур Ранисович
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | 
| Задание 7 | + | 
| Задание 8 | + | 
| Задание 9 | + |
| Задание 10 | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк
### Результат.
![Меню]( )

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку извашего файла, при этом используйте конструкцию open()/close().
```python
file = open('text.txt', 'r',)
print(file.readline())
file.close()
```
### Результат.
![Меню]( )

## Лабораторная работа №3
### 
```python
file = open('text.txt', 'r',)
print(file.readlines())
file.close()
```
### Результат.
![Меню]( )

## Лабораторная работа №4
### 
```python
with open('text.txt', 'r') as file:
  print(file.readlines())
```
### Результат.
![Меню]( )

## Лабораторная работа №5
### 
```python
with open('text.txt', ) as file:
  for line in file:
      print(line)
```
### Результат.
![Меню]( )

## Лабораторная работа №6
### 
```python
with open('text.txt', 'a+') as file:
  file.write('\nSomething new')

with open('text.txt', 'r') as file:
    result = file.readlines()
    print(result)
```
### Результат.
![Меню]( )

## Лабораторная работа №7
### 
```python
lines = ['one', 'two', 'three']
with open('text.txt', 'w') as file:
    for line in lines:
        file.write('\nCycle run ' + line)
    print('Done!')
```
### Результат.
![Меню]( )


## Лабораторная работа №9
### 
```python
def longest_words(file):
    with open(file, encoding='utf=8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

            if len(sought_words) == 1:
                return sought_words[0]
            return sought_words


print(longest_words('text.txt'))
```
### Результат.
![Меню]( )

## Лабораторная работа №10
### 
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат.
![Меню]( )
![Меню]( )

## Самостоятельная работа №1
###

```python

```
### Результат.
![Меню]( )

## Выводы



## Общие выводы по теме
