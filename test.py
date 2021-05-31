
print('hello, this is Celcius to Fahrenheit conversion program.')

c = input("enter value: ")

def getFahrenheitFromCelcius(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

f = getFahrenheitFromCelcius(c)




print("The Fahrenheit is {0}".format(f))


if ( f > 100):
    print("it is very hot")
else:
    print("it is okay temp")

print(f)

