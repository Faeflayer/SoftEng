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