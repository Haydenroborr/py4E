list = []
tries = 0
average = 0

while True:
    #print(tries)
    tries = tries + 1
    line = input("> ")

    if line == "done":
        break
    else:
        line = int(line)
        list.append(line)
    #print(line)
    continue

print("Done!")
#print(list)
average = sum(list) / len(list)
print(average)
