class TempConversion:
    def __init__(self, temp):
        self._tempConversion__temp = temp

class Celsius_to_Kelvin(TempConversion):
    def conversion(self):
        return self._tempConversion__temp + 273.15

class Celsius_to_Fahrenheit(TempConversion):
    def conversion(self):
        return (self._tempConversion__temp * 9/5) + 32

class Fahrenheit_to_Celsius(TempConversion):
    def conversion(self):
        return (self._tempConversion__temp - 32) * 5/9

class Fahrenheit_to_Kelvin(TempConversion):
    def conversion(self):
        return (self._tempConversion__temp + 459.67) * 5/9

class Kelvin_to_Celsius(TempConversion):
    def conversion(self):
        return self._tempConversion__temp - 273.15

class Kelvin_to_Farenheitt(TempConversion):
    def conversion(self):
        return (self._tempConversion__temp - 273.15) * 1.8 + 32

CelsiusTemp = float(input("Enter the temperature in Celsius: "))
convert = Celsius_to_Kelvin(CelsiusTemp)
print(str(convert.conversion()) + " Kelvin")
convert = Celsius_to_Fahrenheit(CelsiusTemp)
print(str(convert.conversion()) + " Fahrenheit")

FahrenheitTemp = float(input("Enter the temperature in Fahrenheit: "))
convert = Fahrenheit_to_Celsius(FahrenheitTemp)
print(str(convert.conversion()) + " Celsius")
convert = Fahrenheit_to_Kelvin(FahrenheitTemp)
print(str(convert.conversion()) + " Kelvin")

KelvinTemp = float(input("Enter the temperature in Kelvin: "))
convert = Kelvin_to_Celsius(KelvinTemp)
print(str(convert.conversion()) + " Celsius")
convert = Kelvin_to_Farenheitt(KelvinTemp)
print(str(convert.conversion()) + " Fahrenheit")
