import converter
celsius=float(input("Enter the temperature in Celsius:"))
fahrenheit=converter.celsius_to_fahrenheit(celsius)
print(f"{celsius}C is equals to the{fahrenheit}F")
#OUTPUT=
# Enter the temperature in Celsius:-5
# -5.0C is equals to the23.0F
#OUTPUT=
#Enter the temperature in Celsius:10
#10.0C is equals to the50.0F
'''
here if i give input in negative then it runs because it is identified by 
the float '''
