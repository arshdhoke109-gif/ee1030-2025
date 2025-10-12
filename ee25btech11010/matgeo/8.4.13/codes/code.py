import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./code.so')

# Define the function signature
lib.solve_conic.restype = None

# Call the function 
lib.solve_conic()

# Ellipse parameters
a_e, b_e = 5, 4
theta = np.linspace(0, 2*np.pi, 400)
x_ellipse = a_e * np.cos(theta)
y_ellipse = b_e * np.sin(theta)

# Hyperbola parameters
a_h, b_h = 3, 4
x_vals = np.linspace(-10, 10, 400)
y_hyperbola_pos = b_h * np.sqrt((x_vals**2 / a_h**2) - 1)
y_hyperbola_neg = -y_hyperbola_pos

# Plot
plt.figure(figsize=(6,6))
plt.plot(x_ellipse, y_ellipse, 'b', label=r'$\frac{x^2}{25} + \frac{y^2}{16} = 1$')
plt.plot(x_vals, y_hyperbola_pos, 'r', label=r'$\frac{x^2}{9} - \frac{y^2}{16} = 1$')
plt.plot(x_vals, y_hyperbola_neg, 'r')

# Annotate
plt.text(6, 0.5, r'$\frac{x^2}{9} - \frac{y^2}{16} = 1$', color='r')
plt.text(2, 3.5, r'$\frac{x^2}{25} + \frac{y^2}{16} = 1$', color='b')

# Styling
plt.axhline(0, color='k', lw=0.8)
plt.axvline(0, color='k', lw=0.8)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ellipse and Hyperbola')
plt.grid(True)
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/8.4.13/figs/ell.png")
plt.show()
