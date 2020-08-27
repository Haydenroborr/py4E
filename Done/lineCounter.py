fileName = input('Enter the file name: ')
try:
    fileName = open(fileName)
except:
    print('File cannot be opened:', fileName)
    exit()
count = 0
for line in fileName:
    count = count + 1
print('There were', count, 'lines in the file.')
