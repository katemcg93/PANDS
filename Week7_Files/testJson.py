import json
filename = "testdict.json"

testDict = dict(name = "Fred", age = "31", grades = [34,56,85])


def writeDict(testDict):
    with open("testdict.json", "wt") as f:
        json.dump(testDict, f)

writeDict(testDict)

def readDict():
    with open("testdict.json", "rt") as f:
        data = json.load(f)
        print(data)

readDict()