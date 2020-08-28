fileName = input('Enter the file name: ')
if fileName == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fileName = open(fileName)
except:
    print('File cannot be opened:', fileName)
    exit()

count = 0
for line in fileName:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'lines in the file.')
