text = "X-DSPAM-Confidence:    0.8475";

string = text.find('0')
num = text[string:]
number = float(num)
print(number)
#print(num)
