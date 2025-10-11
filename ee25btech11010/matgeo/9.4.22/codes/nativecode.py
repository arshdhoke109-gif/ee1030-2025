import numpy as np
import matplotlib.pyplot as plt

k = 6
x = np.linspace(-1, 3, 400)
y = k*x*(x-2) + 6   # kx^2 - 2kx + 6

plt.figure(figsize=(6,4))
plt.axhline(0, color='gray', linewidth=0.8)
plt.plot(x, y, label=f'k={k} : y=kx(x-2)+6')
plt.scatter([1], [0], color='red', zorder=5)   # double root at x=1
plt.title('x^2-2x+1=0')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/9.4.22/figs/parabola.png")
plt.show()
