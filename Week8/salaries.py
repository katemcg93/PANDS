import numpy as np
minSalary = 20000
maxSalary = 80000

numberOfEntries = 10
#np.random.seed(1)

salaryRange = np.random.randint(minSalary,maxSalary,numberOfEntries)
print(salaryRange)

salaryAndRaise = salaryRange + 15000
print(salaryAndRaise)

salariesMult = salaryRange * 1.05
print(salariesMult)

salariesInt = salariesMult.astype(int)
print(salariesInt)