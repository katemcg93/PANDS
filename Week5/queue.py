import random
queueList = []
count = 1

for i in range (10):
    randNo=random.randint(1,100)
    queueList.append(randNo)

print("Queue is ", queueList)

while len(queueList)>1:
    print("Current number is ", queueList.pop(0), "queue is ", queueList)

print("Queue is now empty")
