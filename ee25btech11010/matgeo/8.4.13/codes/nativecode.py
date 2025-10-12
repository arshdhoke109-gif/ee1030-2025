import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a_ellipse = 5
b_ellipse = 4

# Hyperbola parameters
a_hyperbola = 3
b_hyperbola = 4

# Ellipse: x ∈ [-a, a]
x_ellipse = np.linspace(-a_ellipse, a_ellipse, 400)
y_ellipse = b_ellipse * np.sqrt(1 - (x_ellipse / a_ellipse)**2)

# Hyperbola: valid only for |x| ≥ a
x_right = np.linspace(a_hyperbola, 10, 400)
x_left = np.linspace(-10, -a_hyperbola, 400)

y_right = b_hyperbola * np.sqrt((x_right / a_hyperbola)**2 - 1)
y_left  = b_hyperbola * np.sqrt((x_left  / a_hyperbola)**2 - 1)

# Plot ellipse
plt.plot(x_ellipse,  y_ellipse, 'b', label='Ellipse')
plt.plot(x_ellipse, -y_ellipse, 'b')

# Plot hyperbola (both branches)
plt.plot(x_right,  y_right, 'r', label='Hyperbola')
plt.plot(x_right, -y_right, 'r')
plt.plot(x_left,   y_left,  'r')
plt.plot(x_left,  -y_left,  'r')

# Axes
plt.axhline(0, color='k', linewidth=0.8)
plt.axvline(0, color='k', linewidth=0.8)

# Labels and formatting
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ellipse and Hyperbola')
plt.axis('equal')
plt.grid(True)
plt.tight_layout()

# Annotate equations beside curves
plt.text(6.2, 2.5, r'$\frac{x^2}{9} - \frac{y^2}{16} = 1$', color='r', fontsize=11, rotation=10)
plt.text(0.5, 4.5, r'$\frac{x^2}{25} + \frac{y^2}{16} = 1$', color='b', fontsize=11)
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/8.4.13/figs/ell.png")
plt.show()
