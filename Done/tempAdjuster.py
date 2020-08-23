whichTemp = "If you have Celsius temperature: enter C. If you have Fahrenheit temperature: enter F\n"
tempConvertor = "Enter your temperature:\n"

celsiusOrFahrenheit = input(whichTemp)

if celsiusOrFahrenheit == str("C") or str("c"):
    celsiusTemp = input(tempConvertor)
    fahrenheitTemp = (float(celsiusTemp) * 1.8) + 32
    print("Your temperature in Fahrenheit are " + str(fahrenheitTemp) + ".")
elif celsiusOrFahrenheit == str("F") or str("f"):
    print("F")
    fahrenheitTemp = input(tempConvertor)
    celsiusTemp = (float(fahrenheitTemp) - 32)
    print("Your temperature in Celsuis are: " + str(celsiusTemp) + ".")
