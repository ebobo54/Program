import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.log(1+x**0.5)

x = np.linspace(1, 4, 100)

y = [f(i) for i in x]

w = 2.3

plt.plot(x, y, label="ln(1+x**0.5)")

def df(x):
    return -math.log(1+x**0.5)

tangent_slope = df(w)

tangent = [f(w) + tangent_slope*(i - w) for i in x]

plt.plot(x, tangent, label="касательная x=2.3")
plt.plot(w, f(w), "ro")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()

# import math
# import matplotlib.pyplot as plt
# import numpy as np

# def f(x):
#     return math.log(1 + x**0.5)

# x = np.linspace(1, 4, 100)
# y = [f(i) for i in x]

# w = 2.3

# plt.plot(x, y, label="log(1+x**0.5)")

# def df(x):
#     return 1 / (2 * (1 + x**0.5))

# tangent_slope = df(w)

# tangent = [f(w) + tangent_slope * (i - w) for i in x]

# plt.plot(x, tangent, label="Касательная x=2.3")
# plt.plot(w, f(w), "ro")

# plt.title('График функции и касательной')
# plt.xlabel('x')
# plt.ylabel('y')

# plt.legend()

# plt.grid(True)

# plt.annotate(f'Точка касания (x={w}, y={f(w):.2f})', 
#              xy=(w, f(w)), xytext=(w, f(w)+0.5),
#              arrowprops=dict(facecolor='black', shrink=0.05))

# plt.show()
