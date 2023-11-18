with open("text.txt", "r") as file:
    text = file.read()

words = text.split()

if len(words) < 30:
    with open('text.txt', 'w') as file:
        file.write ('Nothing')

with open('text.txt', 'r') as file:
    text_to_read = file.read()

print(text_to_read)