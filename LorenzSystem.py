import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.integrate import solve_ivp
from multiprocessing import Pool, freeze_support


# Perform calculations
def lorenz_system(t, xyz, sigma, rho, beta):
    x, y, z = xyz
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


# Set parameters for the Lorenz system
sigma = float(sys.argv[1])
rho = float(sys.argv[2])
beta = 8 / 3

# Set the time span for integration
t_span = (0, int(sys.argv[3]))

# Set the number of iterations
iterations = int(sys.argv[4])

# Initialize lists to store the chaotic values
x_values = []
y_values = []
z_values = []

# Initialize variables for starting positions
global x0
global y0
global z0

# Set initial position
x0 = float(sys.argv[5])
y0 = float(sys.argv[6])
z0 = float(sys.argv[7])


# Get the next random starting position based on the previous starting position
def custom_random(seed):
    random.seed(seed)
    return random.uniform(0.001, 0.999)


# Generate each starting positions path
def compute_chaotic_values(_):
    global x0
    global y0
    global z0

    initial_values = [x0, y0, z0]
    sol = solve_ivp(lorenz_system, t_span, initial_values, args=(sigma, rho, beta),
                    t_eval=np.linspace(0, t_span[1], 1000))

    # Change starting position for next calculation
    x0 = custom_random(x0)
    y0 = custom_random(y0)
    z0 = custom_random(z0)
    return sol.y[0], sol.y[1], sol.y[2]


if __name__ == '__main__':
    freeze_support()
    # Use multiprocessing for faster computing and higher quality systems
    with Pool() as pool:
        results = pool.map(compute_chaotic_values, range(iterations))

    # Extract the results
    for x, y, z in results:
        x_values.extend(x)
        y_values.extend(y)
        z_values.extend(z)

    # Save the variables to a text file
    file_path = os.path.join("chaos_coordinates", 'lorenz_values.txt')
    with open(file_path, 'w') as file:
        for x, y, z in zip(x_values, y_values, z_values):
            file.write(f"{x} {y} {z}\n")

    # Create a 3D plot of the Lorenz attractor (if needed)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_values, y_values, z_values, lw=0.5)
    ax.set_title("Lorenz Attractor")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Save the generated plot as an image
    image_path = os.path.join("chaos_graphs", 'lorenz_system.png')
    plt.savefig(image_path)
    # plt.show()
