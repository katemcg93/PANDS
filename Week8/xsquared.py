import matplotlib.pyplot as plt
import numpy as np

xaxis = np.array(range(1,100))
yaxis = xaxis * xaxis
plt.plot(xaxis, yaxis)
plt.show()