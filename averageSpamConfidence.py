fileName = input('Enter the file name: ')
numAdd = 0.0
total = 0
count = 0
try:
    fileName = open(fileName)
except:
    print('File cannot be opened:', fileName)
    exit()
for line in fileName:
    if line.startswith('X-DSPAM-Confidence: 0.'):
        number = float(line.find(":"))
        num = line[int(number)+1:]
        #print(line, num)
        numAdd = numAdd + float(num)
        count = count + 1
        #total = float(total) + numAdd
    else:
        continue
average = numAdd / count
#print(numAdd)
#print(total)
#print(count)
print('Average spam confidence:', average)
