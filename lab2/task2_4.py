import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, lambdify, symbols

x_sym = symbols('x')

func = sympify(input('Введите математическую функцию: '))
range_bottom = int(input('Введите начало диапохона: '))
range_top = int(input('Введите конец диапозона: '))

f = lambdify(x_sym, func, 'numpy')

x = np.arange(range_bottom, range_top, 0.1)
y = f(x)

plt.plot(x, y)
plt.show()