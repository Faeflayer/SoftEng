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
| Задание 8 | - | 
| Задание 9 | + |
| Задание 10 | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/1.png)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку извашего файла, при этом используйте конструкцию open()/close().
```python
file = open('text.txt', 'r',)
print(file.readline())
file.close()
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/2.png )

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла массиве, при этом используйте конструкцию open()/close().
```python
file = open('text.txt', 'r',)
print(file.readlines())
file.close()
```
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/3.png)

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open('text.txt', 'r') as file:
  print(file.readlines())
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/4.png )

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
```python
with open('text.txt', ) as file:
  for line in file:
      print(line)
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/5.png )

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
```python
with open('text.txt', 'a+') as file:
  file.write('\nSomething new')

with open('text.txt', 'r') as file:
    result = file.readlines()
    print(result)
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/6.png )

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.
```python
lines = ['one', 'two', 'three']
with open('text.txt', 'w') as file:
    for line in lines:
        file.write('\nCycle run ' + line)
    print('Done!')
```
### Результат.
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/7.png )


## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст:
### Приветствие Спасибо Извините Пожалуйста До свидания Ты готов? Как дела? С днем рождения! Удача! Я тебя люблю.
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных
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
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/9.png)

## Лабораторная работа №10
### Требуется создать csv-файл «rows 300.csv» со следующими столбцами:
### • № - номер по порядку (от 1 до 300); • Секунда - текущая секунда на вашем ПК; • Микросекунда - текущая миллисекунда на часах.
### Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
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
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/10.png )
![Меню](https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/11.png )




## Самостоятельная работа №1
###

```python
with open('text.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()
    words = text1.split()
print(f'Количество слов: {len(words)}')

word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_word = max(word_count, key=word_count.get)
print(f'Самое частое слово: {max_word}, упоминается {word_count[max_word]} раз')
```
### Результат.
![Меню]( )

## Выводы

## Самостоятельная работа №1
###

```python

```
### Результат.
![Меню]( )

## Выводы

## Самостоятельная работа №1
###

```python

```
### Результат.
![Меню]( )

## Выводы

## Самостоятельная работа №1
###

```python

```
### Результат.
![Меню]( )

## Выводы


## Общие выводы по теме
