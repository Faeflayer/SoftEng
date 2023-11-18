# Тема 7 Работа с файлами (ввод, вывод). 
Отчет по Теме #7 выполнил:
- Факаев Тимур Ранисович
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | - |
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
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

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
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/selftext.png)
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/self1.png)

## Выводы
1. ` file.read() читает данные в файле `
2. ` text.split() разделяет данные(слова), чтобы их можно было подсчитать `
3. ` with open - функция открывающая файл и закрывающая его после окончания работы `
4. ` print(f..) - f-строка сочитающая в себе и текст и значение переменной полученной с помощью len(words) `


## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
### Текст в файле:
### Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.
### Ожидаемый результат:
### Input file contains: 108 letters 20 words 4 lines

```python
line_count = 0
word_count = 0
letter_count = 0

with open('text.txt', 'r') as file:
    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)
        for word in words:
            letter_count += len(word)

print("Input file contains:", letter_count, "letters", word_count, "words", line_count, "lines")
```
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/self3.png)

## Выводы
1. ` line_count = 0 - Как и следующие две строки создает переменную равную нулю т.к в дальнейшем мы будем использовать их как счетчик поэтому нужно начальное значение `
2. ` with open('text.txt' , 'r') as file: открывает файл text.txt исключительно для чтения без возможности редактирования `
3. ` for line in file: line_count += 1 - каждая строка в файле прибавляет 1 к счетчику строк `
4. ` words = line.split() - создание переменной, которая будет хранить в себе данные как единицу(слово) `
5. ` word_count +- len(words) счетчик слов равен длине массива состоящего из слов `

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
### Запрещенные слова:
### hello email python the exam wor is
### Предложение для проверки:
### Hello, world! Python IS the programming language of thE future. My EMAIL is… PYTHON is awesome!!!!
### Ожидаемый результат:
### *****, ***ld! ****** ** *** programming language of *** future. My ****** **…. ****** ** awesome!!!!

```python
import re

forbidden_words: list[str] = []
with open("text.txt", "r") as f:

    forbidden_words.extend(f.read().split())

    msg = "Hello, world! Python IS the programming language of thE future. My EMAIL is… PYTHON is awesome!!!!"

for w in forbidden_words:
    msg = re.sub(w, "*" * len(w), msg, flags=re.IGNORECASE)
print(msg)
```
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/self4.png)

## Выводы
1. ` import re : Импорт модуля re для работы с регулярными выражениями.`
2.  ` forbidden_words: list[str] = [] - создание списка запрещенных слов  `
3.  ` with open("text.txt", "r") as f: - открытие файла для чтения `
4.  ` msg = re.sub(w, "*" * len(w), msg, flags=re.IGNORECASE) : Замена каждого вхождения запрещенного слова в предложении на символ "*" с сохранением регистра. `

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

```python
with open("text.txt", "r") as file:
    text = file.read()

words = text.split()

if len(words) < 30:
    with open('text.txt', 'w') as file:
        file.write ('Nothing')

with open('text.txt', 'r') as file:
    text_to_read = file.read()

print(text_to_read)
```
### Результат.
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/self5.png)
![Меню]( https://github.com/Faeflayer/SoftEng/blob/Tema_7/pics/self6.png)

## Выводы
1. ` with open("text.txt", "r") as file: - открытие файла дял чтения `
2. ` text = file.read() - присвоение переменной text данных из файла `
3.  ` words - text.split() - сплит данных в словарь из слов `
4.  ` if len(words) < 30: - проверка на количество слов `
5.  `  with open('text.txt', 'w') as file:  file.write ('Nothing') - если не соответсвует условию if, то текст изменяется на Nothing `
6.  ` with open('text.txt', 'r') as file:   text_to_read = file.read() - повторное чтение файла после возможных изменений `
7.  ` print(text_to_read) - вывод данных на экран `


## Общие выводы по теме
Работа с файлами в Python включает в себя операции чтения и записи данных в файлы. 
Для чтения файла можно использовать функцию open, например with open ('text.txt', 'r') as file:
Для записи в файл можно использовать практически схожую строку за исключением 'r', которая означает read, нужно заменить на 'w' - write.
Использование with помогает защитить информацию и закрывает файл автоматически, когда программа заканчивает работу с ним.
