def computepay(h,r):
    h = float(h)
    r = float(r)
    if h > 40:
        otHour = h - 40
        otRate = r * 1.5
        ot = otRate * otHour
        totalPay = (h - otHour) * r + ot
        print(ot)
    return totalPay

hours = input("Enter Hours:")
rate = input("Enter rate:")
p = computepay(hours,rate)
print("Pay",p)
