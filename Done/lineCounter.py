fileName = input('Enter the file name: ')
fileName = open(fileName)
count = 0
for line in fileName:
    count = count + 1
print('There were', count, 'lines in the file.')
