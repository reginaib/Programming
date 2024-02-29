sentence = input()
start = int(input())
step = int(input())

if start < 0:
    start += len(sentence)

decoded = ''
for _ in range(len(sentence)):
    decoded += sentence[start]
    start += step
    if step > 0:
        start %= len(sentence)
    elif start < 0:
        start += len(sentence)

print(decoded)
