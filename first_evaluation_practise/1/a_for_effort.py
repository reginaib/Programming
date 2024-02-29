letters = input()
num = int(input())

# Read and process the words
total = 0

for _ in range(num):
    word = input().upper()
    integer = ''
    for letter in word:
        index = letters.index(letter)
        integer += str(index)
    integer = int(integer)
    total += integer
    print(f"{word} ({integer})")

print('=' * 10)

total_word = ''
for digit in str(total):
    index = int(digit)
    total_word += letters[index]

print(f"{total_word} ({total})")
