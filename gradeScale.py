gradeScore = input("Enter a score(between 0.0 and 1.0):\n")

try:
    if float(gradeScore) > 1.0:
        print("You've entered a number that's too high.")
    elif float(gradeScore) >= 0.9:
        print("Your grade is A.")
    elif float(gradeScore) >= 0.8:
        print("Your grade is B.")
    elif float(gradeScore) >= 0.7:
        print("Your grade is C.")
    elif float(gradeScore) >= 0.6:
        print("Your grade is D.")
    elif float(gradeScore) < 0.6:
        print("Your grade is F.")
except:
    print("Please enter a numberic value.")
