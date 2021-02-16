import random
randNoList = []
for i in range (0, 10):
    randomNo = random.randint(0,100)
    randNoList.append(randomNo)

print("The random numbers \t", randNoList)

randNoList.sort(reverse=True)
print(randNoList)
print("The sorted numbers are \t ", randNoList [:3])