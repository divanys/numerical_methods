import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - 4 * x**2 + 2

x = np.linspace(-2, 5, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x) = x^3 - 4x^2 + 2')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()

