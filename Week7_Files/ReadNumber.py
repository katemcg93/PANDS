def readInt():
     with open("Week7_Files\IntegerCount.txt","r") as f:
        storedNumber = int(f.read())
        return storedNumber
        

def updateInt(storedNumber):
    with open("Week7_Files\IntegerCount.txt","w") as f:
        newNumber = storedNumber + 1
        f.write(str(newNumber))
        print("We have run this programme {} times ".format(str(newNumber)))


storedNumber = readInt()
updateInt(storedNumber)
    











