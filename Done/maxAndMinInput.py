# max = None
# min = None
numbers = []
# Enter 7, 2, bob, 10, 4
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        number = float(number)
    except:
        print("Invalid input")
        continue
    if number not in numbers:
        numbers.append(number)
    # if min is None:
    #     min = float(number)
    # if max is None:
    #     max = float(number)
    # if float(number) < min:
    #     min = number
    # if float(number) > max:
    #     max = number

print("Maximum is", int(max(numbers)))
print("Minimum is", int(min(numbers)))
