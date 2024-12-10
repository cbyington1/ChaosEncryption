import os
import sys
import numpy as np
import matplotlib.pyplot as plt


# Perform calculations
def logistic_map(r, x):
    x = r * x * (1 - x)
    x = min(max(x, 0.001), 0.999)
    return x


# Set initial conditions
initial_position = float(sys.argv[1])
iterations = int(sys.argv[2])
transient = int(sys.argv[3])

# Generate r values
r_values = np.linspace(initial_position, 4.0, 10000)

# Initialize a list to store the chaotic values
x_values = []

# Generate the bifurcation diagram
for r in r_values:
    x = initial_position
    for _ in range(transient):
        x = logistic_map(r, x)
    for _ in range(iterations):
        x = logistic_map(r, x)
        x_values.append((r, x))

# Save the chaotic values to a text file
file_path = os.path.join("chaos_coordinates", 'logistic_map_values.txt')
with open(file_path, 'w') as file:
    for r, x in x_values:
        file.write(f"{r} {x} 0\n")

# Create a scatter plot of the bifurcation diagram
r, x = zip(*x_values)
plt.scatter(r, x, s=1, marker='.', c='black')
plt.title("Logistic Map Bifurcation Diagram")
plt.xlabel("r (Parameter)")
plt.ylabel("X")
plt.xlim(min(r_values), max(r_values))
plt.ylim(0, 1)

# Save the generated plot as an image
image_path = os.path.join("chaos_graphs", 'logistic_map.png')
plt.savefig(image_path)
# plt.show()
