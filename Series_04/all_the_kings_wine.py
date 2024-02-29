num_deaths = int(input())
deceased_prisoners = [input() for _ in range(num_deaths)]

poisoned_bottle = 0
for prisoner in deceased_prisoners:
    position = ord(prisoner) - ord('A')
    poisoned_bottle += 2 ** position

print(f"Bottle #{poisoned_bottle} is poisoned.")
