first_letter_position = int(input()) - 1
step = int(input())
length_of_hidden_word = int(input())
text = ''

while True:
    line = input()
    if not line:
        break
    for char in line:
        if char.isalpha():
            text += char

decoded = ''
for _ in range(length_of_hidden_word):
    if 0 <= first_letter_position < len(text):
        decoded += text[first_letter_position]
        first_letter_position += step
    else:
        decoded += '?'

print(decoded)
