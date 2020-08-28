fileName = input('Enter the file name: ')
try:
    fileName = open(fileName)
except:
    print('File cannot be opened:', fileName)
    exit()
for line in fileName:
    line = line.upper()
    print(line)
