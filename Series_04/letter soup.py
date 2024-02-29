# read number of lines in the grid
n = int(input())

# initialize hidden word
word = ''

# traverse lines of the grid
for _ in range(n):
    
    # read next line of the grid
    line = input()
    
    # filter letters from line and append
    # them to the hidden word
    for character in line:
        if character.isalpha():
            word += character
            
# write out hidden word
print(word)
