import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-2, 0, 100)
x2 = np.linspace(0, 1, 100)
x3 = np.linspace(1, 9, 100)

y1 = x1**2 + 1
y2 = 2*x2 - 1
y3 = np.sqrt(x3)

plt.figure(figsize=(10,6))

plt.plot(x1, y1, 'b-', label='x²+1, x≤0')
plt.plot(x2[1:], y2[1:], 'r-', label='2x-1, 0<x≤1')  # без x=0
plt.plot(x3, y3, 'g-', label='√x, x>1')

# Точки
plt.plot(0, 1, 'bo', markersize=8)  # закрашена
plt.plot(0, -1, 'ro', markersize=8, markerfacecolor='none')  # выколота
plt.plot(1, 1, 'go', markersize=8)  # закрашена

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.legend()
plt.title("График функции")
plt.xlabel("x")
plt.ylabel("y")
plt.show()