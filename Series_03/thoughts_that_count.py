number_rw = int(input())
number_wb = int(input())
operator = input()


for red in range(2, number_rw - 1):
    white = number_rw - redpy
    if operator == '>':
        if red <= white:
            continue
    elif red >= white:
        break

    blue = number_wb - white
    if blue >= 2:
        print(blue, white, red, sep='\n')
        break
