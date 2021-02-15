grade = input ("Enter your percentage grade:")
gradeint = int(grade)
if gradeint <40 :
    print("fail")
elif gradeint >=40 and gradeint <= 49:
    print("Pass")
elif gradeint >=50 and gradeint <= 59:
    print("2:2")
elif gradeint >=60 and gradeint <= 69:
    print("2:1")
elif gradeint >=70 and gradeint <=100:
    print("1:1")
else:
    print("Invalid entry")

