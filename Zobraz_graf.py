import matplotlib.pyplot as plt
import math
import numpy as np

x = [n for n in range(90,100)]
y1 = [math.factorial(n) for n in x]
y2 = [n**(1/np.log(n)) for n in x]
y3 = [(math.e)**n for n in x]
"""
y4 = 
y5 = 
y6 =
y7 =
"""
plt.plot(x, y1, "red")
plt.plot(x, y2, "green")
plt.plot(x, y3, "blue")

plt.show()