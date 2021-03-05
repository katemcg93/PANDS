def menu () :
    print (
        "What would you like to do?"
        "\t (a) Add new student"
        "\t (v) View Students"
        "\t (q) View Students"
        )
    selection = input("Type one letter (a/v/q):")

    return selection

studentList = []


def readmodules ():
    modules = []
    moduleInput = input("Please enter a module name:")
    while moduleInput.strip() != "":
        moduleDetail ={
           "Name" : moduleInput,
            "Grade" : input("Please Enter a grade:")
            }
        modules.append(moduleDetail)
        moduleInput = input("Please enter a new module:")
    if moduleInput == "":
            print("ok")
    return modules

def doadd(studentList) :
    studentInfo = {}
    studentInfo["name"] = input("Please enter Name: ")
    studentInfo["Modules"] = readmodules()  
    print(studentInfo)         
    studentList.append(studentInfo)
    print(studentList)
    return(studentList)
        

def getModules (modules):
    print("\t Name :\t Grade")
    for moduleDetail in modules:
        print("\t {} : {}".format(moduleDetail["Name"],moduleDetail["Grade"]))
      

def doview(studentList):
    for studentInfo in studentList:
        print("Student : {}".format(studentInfo["name"]))
        getModules(studentInfo["Modules"])
        #print(studentInfo["Modules"])   

selection = menu() 

while selection != "q":
    if selection == "a":
        studentList = doadd(studentList)
        selection = menu()
    elif selection == "v":
        doview(studentList)
        selection = menu()     
    else:
        print("Please enter a valid value")
        selection = menu()


