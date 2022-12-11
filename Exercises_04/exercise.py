#I have an American air conditioner system returning temperatures, but I need the temperatures in
#standard units. Create a list of 10 values in degrees Kelvin. Write a code block to print these values in
#Celsius and Fahrenheit.

# Formula used for Kelvin to fahrenheit 1.8*(Klevin-273.15)+32
# Formula used for Kelvin to celsius Klevin-273.15
# Rounded all the output to 2 digits
kelvin_temps=[300,290,320,224,110,400,260,200,380,80]
for i in kelvin_temps:
	print(f"Kelvin Temp {i} in fahrenheit is ", str(round(1.8*(i-273.15)+32, 2)), "and in celsius is ", str(round(i-273.15, 2)) )







