#This is a programme to take any dollar amount and convert it to cents
#Considerations for this include:
#Changing to an absolute number
#multiplying it by 100 to get the cents value
#need to be able to enter floats
#also need to change the cents value back to an integer once calculations are done

#author: Kate McGrath

userAmount = input("Please enter an amount: ")
absoluteAmount = abs(float(userAmount))
centsValue = int(absoluteAmount * 100)
print("That amount in cents is: {} ".format(centsValue))