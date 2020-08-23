max = None
min = None


for number in [7, 2, "bob", 10, 4]:
    try:
        if min is None or number < min:
            min = number
        if max is None or number > max:
            max = number
    except:
        print("Invalid input")

print("Maximum is", max)
print("Minimum is", min)
