i = int(input())

for _ in range(i):
    word = input()
    word_l = word.lower()
    letter_count = [0] * 26  # Initialize a list to count letter occurrences (a-z)

    for char in word_l:
        if char.isalpha():
            index = ord(char) - ord('a')
            letter_count[index] += 1

    is_double_word = all(count % 2 == 0 for count in letter_count)

    if is_double_word:
        print(word)


