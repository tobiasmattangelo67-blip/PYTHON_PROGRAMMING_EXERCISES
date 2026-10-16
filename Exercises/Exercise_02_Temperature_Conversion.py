
# * This function returns the number of this temperature in degrees Fahrenheit
def convertToFahrenheit(degreesCelsius):
    fahrenheit = degreesCelsius * (9 / 5) + 32
    return fahrenheit

# * This function returns the number of this temperature in degrees Celsius
def convertToCelsius(degreesFahrenheit):
    celsius = (degreesFahrenheit - 32) * (5 / 9)
    return celsius

assert convertToCelsius(0) == -17.77777777777778, "this is false"
print(convertToCelsius(0))

assert convertToCelsius(180) == 82.22222222222223, "this is false"
print(convertToCelsius(180))

assert convertToFahrenheit(0) == 32, "this is false"
print(convertToFahrenheit(0))

assert convertToFahrenheit(100) == 212, "this is false"
print(convertToFahrenheit(100))

assert convertToCelsius(convertToFahrenheit(15)) == 15, "this is false"
print(convertToCelsius(15))