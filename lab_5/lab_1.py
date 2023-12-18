import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.exp(-x - 1/2)

x = np.linspace(1, 2, 100)

y = [f(i) for i in x]

plt.plot(x, y, label="e^(-x-1/2)")

def df(x):
    return -math.exp(-x - 1/2)

tangent_slope = df(1.5)

tangent = [f(1.5) + tangent_slope*(i - 1.5) for i in x]

plt.plot(x, tangent, label="касательная x=1.5")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
