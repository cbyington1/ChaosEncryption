import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Perform calculations
def henon_heiles(t, u):
    x, y, px, py = u
    dxdt = px
    dydt = py
    dpxdt = -x - 2 * x * y
    dpydt = -y - (x ** 2 - y ** 2)
    return [dxdt, dydt, dpxdt, dpydt]


# Set the initial conditions
u0 = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]

# Set the time span for integration
t_span = (0, int(sys.argv[5]))
t_eval = np.linspace(*t_span, 10000)

# Solve the Hénon-Heiles system
sol = solve_ivp(henon_heiles, t_span, u0, t_eval=t_eval)

# Extract the trajectories
x = sol.y[0]
y = sol.y[1]

# Save the chaotic values to a text file
file_path = os.path.join("chaos_coordinates", 'henon_heiles_values.txt')
with open(file_path, 'w') as file:
    for x_val, y_val in zip(x, y):
        file.write(f"{x_val} {y_val} 0\n")

# Create a 2D plot of the Hénon-Heiles trajectories
plt.figure(figsize=(8, 6))
plt.plot(x, y, lw=0.5)
plt.title("Hénon-Heiles System Trajectories")
plt.xlabel("X")
plt.ylabel("Y")

# Save the generated plot as an image
image_path = os.path.join("chaos_graphs", 'hénonheiles_system.png')
plt.savefig(image_path)
#plt.show()
