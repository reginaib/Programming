density = float(input())
fecundity = float(input())
num_steps = int(input())
print(density)

for _ in range(num_steps - 1):
    density = density * (1 - density) * fecundity

    print(density)

