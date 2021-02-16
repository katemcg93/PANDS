from statistics import mean

numbers = []

number = input("Please enter a number (0 to quit)")

list_lenth = len(numbers)

while number != "0" :
        print(number)
        numbers.append(float(number))
        number = input("Please enter a number")
        print(numbers)


average = sum(numbers)/len(numbers)
print("The average of this list is {}".format(average))



