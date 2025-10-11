import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared C library
lib = ctypes.CDLL("./code.so")

# Define the return type of the C function
lib.find_k.restype = ctypes.c_double

# Call the C function
k = lib.find_k()
print("Value of k for equal roots:", k)

# Define the quadratic function
def f(x, k):
    return k * x * (x - 2) + 6

# Create x values
x = np.linspace(-1, 3, 200)
y = f(x, k)

# Plot the quadratic
plt.plot(x, y, label=f"k = {k:.2f}")
plt.axhline(0, color="black", linewidth=0.8)  # x-axis
plt.axvline(0, color="black", linewidth=0.8)  # y-axis
plt.title("Quadratic: kx(x - 2) + 6 = 0 (Equal Roots Condition)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/9.4.22/figs/parabola.png")
plt.show()



