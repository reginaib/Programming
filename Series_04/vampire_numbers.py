num_str = input()
number = int(num_str)
n = len(num_str)
found_fangs = False

if n % 2 != 0:
    print(f"{number} is not a vampire number.")
else:
    for i in range(10**(n//2-1), int(number ** 0.5) + 1):  # min int is 10; +1 is to include sqrt
        if number % i == 0:
            j = number // i
            if i % 10 == 0 and j % 10 == 0:
                continue
            fang1 = str(i)
            fang2 = str(j)
            if sorted(fang1 + fang2) == sorted(num_str):
                found_fangs = True
                print(f"{number} is a vampire number.")
                break

    if not found_fangs:
        print(f"{number} is not a vampire number.")
