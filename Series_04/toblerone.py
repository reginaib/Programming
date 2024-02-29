brand_name = input()
city_name = input().lower()

city_index = 0
result = ""

for char in brand_name:
    if city_index < len(city_name) and char.lower() == city_name[city_index]:
        result += "[" + char + "]"
        city_index += 1
    else:
        result += char

result = result.replace("][", "")

print(result)
