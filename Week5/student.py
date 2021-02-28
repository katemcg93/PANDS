student = {
    "name": "Mary",
    "courses" : {
            "Course1" :{ "Course": "Programming","Grade": "35"},
            "Course2" : {"Course" : "History","Grade" : "99"}
        }
    }

print(student)
print(student ["name"])


print(student["courses"])

print(student["name"])
for i in student["courses"].values():
    print(i)