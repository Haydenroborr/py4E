counter = 0
fruit = "banana"
index = -1

while counter < len(fruit):
    letter = fruit[index]
    print(letter)
    counter = counter + 1
    index = index - 1
print(fruit)

# def count(word, letter):
#     counter = 0
#     for letters in word:
#         if letters == str(letter):
#             counter = counter + 1
#
#     print('There is', counter, letter, 'in', word + ".")

def countv2(word, letter):
    num = 0
    num = word.count(letter)
    print('There is', num, letter, 'in', word + ".")

countv2(fruit, "b")
countv2(fruit, "a")
countv2(fruit, "n")
