emails = open('mbox-short.txt')
address = []
#senter = []

for email in emails:
    if email.startswith('From '):
        address.append(email)
        emailInfo = email.split()
        print(emailInfo[1])
        #senter.append(emailInfo[1])
    else:
        continue

#print(senter)
print('There were', len(address), 'lines in the file with From as the first word')
