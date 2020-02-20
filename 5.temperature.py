print("Enter your choice: 1 or 2")
print("1. Convert celcius to Fahrenheit")
print("2. Convert Fahrenheit to Celcius")
choice = int(input("Enter your choice:"))
temp = float(input("Enter temperature:"))

if choice == 1:
    f=(temp*9/5)+32
    print('{0} degree celcius = {1} degree fahrenheit'.format(temp,f))
if choice == 2:
    c = (temp-32)*5/9
    print('{0} degree fahrenheit = {1} degree celcius'.format(temp,c))
    



