userNumber = input("Please enter a number:")

while float(userNumber) != -1:
    
    numberFormat = round(float(userNumber))
    if(round(float(userNumber)) % 2  != 0):
        print("{} is an odd number".format(str(numberFormat)))

    else:
        print("{} is an even number".format(str(numberFormat)))

    userNumber = input("Please enter a number, enter -1 to quit")