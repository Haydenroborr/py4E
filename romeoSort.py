romeo = open('romeo.txt')
allWords = []
#print(romeo)

for line in romeo:
    words = line.split()
    for word in words:
        if word in allWords:
            continue
        else:
            allWords.append(word)
            continue

allWords.sort()
print(allWords)
