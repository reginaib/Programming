i = int(input())
prev = None

while True:
    line = input()
    if line == 'NYT':
        break

    current = int(line)

    if prev is not None and current - prev != i:
        print(f'{prev} -> {current} ({current - prev:+})')
    prev = current
