word = input()
n = int(input())
word_use = word.upper()
row, column = None, None
search = True
line_number = 0
while search and n > 0:
    line = str(input()).upper()
    line_number += 1
    index = line.find(word_use)
    if index !=-1:
        column = index
        row = line_number-1
        search = False
        print(f"{word} is on row {row} and column {column}")
    else:
        line_reverse = line[::-1]
        index2= line_reverse.find(word_use)
        if index2 !=-1:
            column = len(line_reverse) - (len(line_reverse[:index2]) + len(word_use))
            row = line_number-1
            search= False
            print(f"{word} is on row {row} and column {column}")


    n -=1

if not row :
    print(f"{word} is not found")