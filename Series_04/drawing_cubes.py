# Read input
width = int(input())
height = int(input())
depth = int(input())

# Draw the cuboid
for i in range(depth, 0, -1):
    print(' ' * i + ':' * (width - 1) + '/' + '+' * min(depth - i, height - 1))

for i in range(depth, height):
    print('#' * width + '+' * depth)

for i in range(min(depth - 1, height - 1), -1, -1):
    print('#' * width + '+' * i)


