total = 0
count = 0
average = 0

while True:
    try:
        line = input("> ")
        if line == "done":
            break
        else:
            total = total + int(line)
            count = count + 1
        print(line)
    except:
        print("Please enter a number.")

print("Done!")
average = float(total) / float(count)
print(total, count, average)
