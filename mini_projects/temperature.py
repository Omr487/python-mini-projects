temperature = float(input("enter the temperature: "))
unit = input("enter the unit (c/k/f)")
if unit == "c":
    kelvin = temperature +273.15
    print(f"the temperature in kelvin is {round(kelvin,2)}K")
    fahrenheit = (temperature *9/5) +32
    print(f"the temperature in fahrenheit is {round(fahrenheit,2)}F")
elif unit =="k":
   celcius = temperature - 273.15
   print(f"the temperature in celcius is {round(celcius,2)}C")
   fahrenheit = 9/5 *(temperature-273.15) + 32
   print(f"the temperature in fahrenheit is {round(fahrenheit,2)}F") 
elif unit == "f":
    celcius = 1.8 *(temperature-32)
    print(f"the temperature in celcius is {round(celcius,2)}")
    kelvin = 5/9*(temperature-32)+273.15
    print(f"the temperature in kelvin is {round(kelvin,2)}")
else :
    print("invalid unit")
