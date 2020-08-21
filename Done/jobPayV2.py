hourInfo = "Enter Hours you worked last two weeks:\n"
payInfo = "Enter your pay rate:\n"

def computePay(x, y):
    totalhour = input(x)
    totalrate = input(y)

    hour = float(totalhour)
    rate = float(totalrate)

    overtime = float(hour) - 40
    if float(hour) > 40:
        overtimeRate = float(rate) * 1.5
        extraPay = overtime * overtimeRate
        return extraPay
        hour = float(hour) - overtime

    pay = float(hour) * float(rate) + extraPay
    print("Pay", pay)

computePay(hourInfo, payInfo)
