steps = int(input())
num_lines = int(input())

one_line = ''
for _ in range(num_lines):
    inp_line = input()
    one_line += inp_line

rev_line = one_line[::-1]

message = ''
for i in range(steps):
    message += rev_line[i::steps]

print(message)

