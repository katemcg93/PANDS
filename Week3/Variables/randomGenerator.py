import random
randomNo = random.randint(0,10)
print ("Here's a random number {}".format(randomNo))

minValue = input("Enter the min value:")
maxValue = input("Enter the max value:")
minInt = int(minValue)
maxInt = int(maxValue)

randomChoice = random.randint(minInt, maxInt)
print("Here's the random number from your range: {}.".format(randomChoice))