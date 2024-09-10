user_input = int(input("Enter a temperature in Celsius: "))


# Celsius to Fahrenheit

def f_conversion(celcius):
    return (celcius * 9/5) + 32

farhrenheit = f_conversion(user_input)
print(farhrenheit)

# Fahrenheit to Celsius

user_input_2 = int(input("Enter a temperature in Fahrenheit: "))

def c_conversion(fahrenheit):
    return (fahrenheit - 32 ) * 5/9

celcius = c_conversion(user_input_2)
print(celcius)
