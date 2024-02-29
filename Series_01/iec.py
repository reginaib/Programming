# Read the input values
gigabytes = int(input())
megabytes = int(input())
kilobytes = int(input())
bytes = int(input())

# Calculate the total amount of bytes
total_bytes = bytes + kilobytes * 1000 + megabytes * 10 ** 6 + gigabytes * 10 ** 9

# Calculate the IEC units
gibibytes = total_bytes // 2 ** 30
rest = total_bytes % 2 ** 30
mebibytes = rest // 2 ** 20
rest %= (2 ** 20)
kibibytes = rest // 2 ** 10
bytes = rest % 1024

# Print the output
print(f"{total_bytes}b")
print(f"{gibibytes}Gib, {mebibytes}Mib, {kibibytes}Kib, {bytes}b")
