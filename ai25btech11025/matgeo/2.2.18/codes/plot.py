import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# === Load the C shared library ===
lib = ctypes.CDLL("./libunitvector.so")

# Define C function signature
lib.unitVector.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int,
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double))
lib.unitVector.restype = None

# Plane equation: ax + by + cz + d = 0
a, b, c, d = 1, 2, 3, -6   # Example: x + 2y + 3z - 6 = 0

# Output variables for unit vector
ux = ctypes.c_double()
uy = ctypes.c_double()
uz = ctypes.c_double()

# Call C function to get unit normal vector
lib.unitVector(a, b, c, ctypes.byref(ux), ctypes.byref(uy), ctypes.byref(uz))
u = np.array([ux.value, uy.value, uz.value])

# === Plotting ===
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create mesh grid for the plane
xx, yy = np.meshgrid(range(-2, 5), range(-2, 5))
zz = (-(a*xx + b*yy + d)) / c   # Solve for z from ax+by+cz+d=0

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Pick a point on the plane (x=0,y=0 ⇒ z=-d/c)
point = np.array([0, 0, -d/c])

# Plot the normal vector
ax.quiver(point[0], point[1], point[2],
          u[0], u[1], u[2],
          length=2, color='red', linewidth=2)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Plane and its Unit Normal Vector")
plt.savefig("/home/r-nikhil/ee1030-2025/ai25btech11025/matgeo/2.2.18/figs/plotc.png")
plt.show()

