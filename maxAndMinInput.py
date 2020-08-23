max = None
min = None

# Enter 7, 2, bob, 10, 4
while True:
    number = input("Enter a number: ")
    try:
        if number == "done":
            break
        number = float(number)
        if min is None:
            min = float(number)
        if max is None:
            max = float(number)
        if float(number) < min:
            min = number
        if float(number) > max:
            max = number
    except:
        print("Invalid input")

print("Maximum is", int(max))
print("Minimum is", int(min))
