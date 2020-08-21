max = None
min = None


for number in [4, 5, 7, 16, 3]:
    if min is None or number < min:
        min = number
    if max is None or number > max:
        max = number
    print(min, max)

print("Final:", min, max)
