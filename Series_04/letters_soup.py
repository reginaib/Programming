# read the number of lines
lines = int(input())

# process the remaining lines one by one
word = ''

for _ in range(lines):

    # read the next line of the input
    line = input()

    # extract all letters from the line and append to the word
    for character in line:
        if character.isalpha():
            word += character

#generate the word
print(word)