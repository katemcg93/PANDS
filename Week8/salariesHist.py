import numpy as np
import matplotlib.pyplot as plt
minSalary = 20000
maxSalary = 80000

numberOfEntries = 10
np.random.seed(1)

salaryRange = np.random.randint(minSalary,maxSalary,numberOfEntries)
plt.hist(salaryRange)
plt.show()