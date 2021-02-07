import math

userNumber = input("Enter a float number")
floatingNumber = float(userNumber)
wholeNumber = round(abs(floatingNumber))
print(str(floatingNumber) + " rounded is "+ str(wholeNumber) + " ")
