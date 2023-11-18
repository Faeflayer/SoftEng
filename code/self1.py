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