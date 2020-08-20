hourInfo = "Enter Hours you worked last two weeks:\n"
payInfo = "Enter your pay rate:\n"

totalhour = input(hourInfo)
totalrate = input(payInfo)

hour = float(totalhour)
rate = float(totalrate)

def computePay(hour, rate):
    overtimeRate = float(rate) * 1.5
    extraPay = overtime * overtimeRate
    return extraPay


try:
    if float(hour) > 40:
        overtime = float(hour) - 40
        extraPay = computePay(hour, rate)
        hour = float(hour) - overtime

    pay = float(hour) * float(rate) + extraPay
    print(pay)

except:
    print("Error, please enter numberic input")
