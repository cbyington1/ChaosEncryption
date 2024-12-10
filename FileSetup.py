import os
import subprocess
import sys
import random


# Check if systems are valid and contain the valid amount of parameters. If valid add parameters to their respective array
def validate_system(key_parameter):
    henonHeilesParameters = []
    logisticsParameters = []
    lorenzParameters = []
    rosslerParameters = []

    system_names = set()  # To store encountered system names

    # Extract systems and parameters from systems
    for system_info in key_parameter:
        system_name = system_info[:2]

        # Check if the system name has been used before
        if system_name in system_names:
            print(f"Error: System name '{system_name}' was used more than once. Each system can only be used once.")
            exit(1)
        else:
            system_names.add(system_name)

        params = system_info[2:]

    if system_name == 'HS':
        params = params.strip('[]').split('][')

        try:
            params = [float(param) for param in params]
        except ValueError:
            print("Parameter key was not properly formatted")
            exit(1)

        if len(params) != 5:
            print("Invalid amount of parameters. Hénon Heiles system requires 5 parameters")
            exit(1)
        henonHeilesParameters.extend(params)
    elif system_name == 'LS':
        params = params.strip('[]').split('][')

        try:
            params = [float(param) for param in params]
        except ValueError:
            print("Parameter key was not properly formatted")
            exit(1)

        if len(params) != 7:
            print("Invalid amount of parameters. Lorenz system requires 7 parameters")
            exit(1)
        lorenzParameters.extend(params)
    elif system_name == 'RS':
        params = params.strip('[]').split('][')

        try:
            params = [float(param) for param in params]
        except ValueError:
            print("Parameter key was not properly formatted")
            exit(1)

        if len(params) != 7:
            print("Invalid amount of parameters. Rössler system requires 7 parameters")
            exit(1)
        rosslerParameters.extend(params)
    elif system_name == 'LM':
        params = params.strip('[]').split('][')

        try:
            params = [float(param) for param in params]
        except ValueError:
            print("Parameter key was not properly formatted")
            exit(1)

        if len(params) != 3:
            print("Invalid amount of parameters. Logistic map requires 3 parameters")
            exit(1)
        logisticsParameters.extend(params)
    else:
        print(f"Invalid system: {system_name}")
        exit(1)  # Terminate the program with an error code

    return henonHeilesParameters, logisticsParameters, lorenzParameters, rosslerParameters


# Get random line for next system
def random_target(var, maxLine):
    # Use previous combined coordinates for seed to generate int value in the proper range for the next file
    random.seed(var)
    return random.randint(1, maxLine)


# Directory name for saving chaotic coordinate files
chaos_directory = "chaos_coordinates"
os.makedirs(chaos_directory, exist_ok=True)

# Directory name for saving chaotic photos
chaos_directory = "chaos_graphs"
os.makedirs(chaos_directory, exist_ok=True)

key_parameter = sys.argv[1].split(", ")

# Set arrays
henonHeilesParams, logisticsParams, lorenzParams, rosslerParams = validate_system(key_parameter)

# Check if array is filled
if len(lorenzParams) == 7:
    # Set variables to parameters in proper datatype
    sigma = float(lorenzParams[0])
    rho = float(lorenzParams[1])
    t_span = int(lorenzParams[2])
    iterations = int(lorenzParams[3])
    x = float(lorenzParams[4])
    y = float(lorenzParams[5])
    z = float(lorenzParams[6])

    # Set variables to boolean value based on if they fall in the correct range
    valid_sigma = 5.0 <= sigma <= 10.0
    valid_rho = 20.0 <= rho <= 40.0
    valid_t_span = 20 <= t_span <= 100
    valid_iterations = 20 <= iterations <= 100
    valid_x = 0.001 <= x <= 0.999
    valid_y = 0.001 <= y <= 0.999
    valid_z = 0.001 <= z <= 0.999

    # If all variables are valid calculate system
    if valid_sigma and valid_rho and valid_t_span and valid_iterations and valid_x and valid_y and valid_z:
        subprocess.run(["python", "LorenzSystem.py", str(sigma), str(rho), str(t_span),
                        str(iterations), str(x), str(y), str(z)])
        print("Lorenz system processed")
    # If all variables are not valid tell user which are not and exit
    else:
        if not valid_sigma:
            print("Parameter 'sigma' is out of range. The value should be between 5.0 and 10.0.")
        if not valid_rho:
            print("Parameter 'rho' is out of range. The value should be between 20.0 and 40.0.")
        if not valid_t_span:
            print("Time span is out of range. The value should be between 20 and 100.")
        if not valid_iterations:
            print("Iterations are out of range. The value should be between 20 and 100.")
        if not valid_x:
            print("Initial condition 'x' is out of range. The value should be between 0.001 and 0.999.")
        if not valid_y:
            print("Initial condition 'y' is out of range. The value should be between 0.001 and 0.999.")
        if not valid_z:
            print("Initial condition 'z' is out of range. The value should be between 0.001 and 0.999.")
        exit(1)

# Check if array is filled
if len(rosslerParams) == 7:
    # Set variables to parameters in proper datatype
    a = float(rosslerParams[0])
    c = float(rosslerParams[1])
    t_span = int(rosslerParams[2])
    iterations = int(rosslerParams[3])
    x = float(rosslerParams[4])
    y = float(rosslerParams[5])
    z = float(rosslerParams[6])

    # Set variables to boolean value based on if they fall in the correct range
    valid_a = 0.1 <= a <= 0.3
    valid_c = 5.0 <= c <= 6.0
    valid_t_span = 50 <= t_span <= 200
    valid_iterations = 50 <= iterations <= 200
    valid_x = 0.001 <= x <= 0.999
    valid_y = 0.001 <= y <= 0.999
    valid_z = 0.001 <= z <= 0.999

    # If all variables are valid calculate system
    if valid_a and valid_c and valid_t_span and valid_iterations and valid_x and valid_y and valid_z:
        subprocess.run(["python", "RosslerSystem.py", str(a), str(c), str(t_span),
                        str(iterations), str(x), str(y), str(z)])
        print("Rössler system processed")
    # If all variables are not valid tell user which are not and exit
    else:
        if not valid_a:
            print("Parameter 'a' is out of range. The value should be between 0.1 and 0.3.")
        if not valid_c:
            print("Parameter 'c' is out of range. The value should be between 5.0 and 6.0.")
        if not valid_t_span:
            print("Time span is out of range. The value should be between 50 and 200.")
        if not valid_iterations:
            print("Iterations are out of range. The value should be between 50 and 200.")
        if not valid_x:
            print("Initial condition 'x' is out of range. The value should be between 0.001 and 0.999.")
        if not valid_y:
            print("Initial condition 'y' is out of range. The value should be between 0.001 and 0.999.")
        if not valid_z:
            print("Initial condition 'z' is out of range. The value should be between 0.001 and 0.999.")
        exit(1)

# Check if array is filled
if len(logisticsParams) == 3:
    # set variables to parameters in proper datatype
    initial_value = float(logisticsParams[0])
    iterations = int(logisticsParams[1])
    transient = int(logisticsParams[2])

    # Set variables to boolean value based on if they fall in the correct range
    valid_initial_value = 3.57 <= initial_value <= 4.0
    valid_iterations = 20 <= iterations <= 100
    valid_transient = 100 <= transient <= 500

    # If all variables are valid calculate system
    if valid_initial_value and valid_iterations and valid_transient:
        subprocess.run(["python", "LogisticsMap.py", str(initial_value), str(iterations), str(transient)])
        print("Logistics map processed")
    # If all variables are not valid tell user which are not and exit
    else:
        if not valid_initial_value:
            print("Initial value is out of range. The value should be between 3.57 and 4.0.")
        if not valid_iterations:
            print("Iterations are out of range. The value should be between 20 and 100.")
        if not valid_transient:
            print("Transient is out of range. The value should be between 100 and 500.")
        exit(1)

# Check if array is filled
if len(henonHeilesParams) == 5:
    # Set variables to parameters in proper datatype
    x = float(henonHeilesParams[0])
    y = float(henonHeilesParams[1])
    px = float(henonHeilesParams[2])
    py = float(henonHeilesParams[3])
    t_span = int(henonHeilesParams[4])

    # Set variables to boolean value based on if they fall in the correct range
    valid_x = 0.1 <= x <= 0.25
    valid_y = 0.1 <= y <= 0.25
    valid_px = 0.1 <= px <= 0.25
    valid_py = 0.1 <= py <= 0.25
    valid_t_span = 1000 <= t_span <= 100000

    # If all variables are valid calculate system
    if valid_x and valid_y and valid_px and valid_py and valid_t_span:
        subprocess.run(["python", "HénonHeilesSystem.py", str(x), str(y), str(px), str(py), str(t_span)])
        print("Hénon Heiles system processed")
    # If all variables are not valid tell user which are not and exit
    else:
        if not valid_x:
            print("Initial condition x is out of range. The value should be between 0.1 and 0.25.")
        if not valid_y:
            print("Initial condition y is out of range. The value should be between 0.1 and 0.25.")
        if not valid_px:
            print("Initial condition px is out of range. The value should be between 0.1 and 0.25.")
        if not valid_py:
            print("Initial condition py is out of range. The value should be between 0.1 and 0.25.")
        if not valid_t_span:
            print("Time span is out of range. The value should be between 1000 and 100,000.")
        exit(1)

print()

# Get acronyms for file mapping
acronyms = [item[:2] for item in key_parameter]

# Define dictionary to map acronyms to file names
file_mapping = {
    'HS': 'chaos_coordinates/henon_heiles_values.txt',
    'LM': 'chaos_coordinates/logistic_map_values.txt',
    'LS': 'chaos_coordinates/lorenz_values.txt',
    'RS': 'chaos_coordinates/rossler_values.txt'
}

# Create dictionary to hold file content in memory
file_contents = {acronym: open(file_mapping[acronym], 'r').readlines() for acronym in acronyms}

# Create output file for combined values
output_file = open(os.path.join('chaos_coordinates', 'combined_values.txt'), 'w')

# Create variable for prng seed
var = 1

# Create array to hold amount of lines in each file
acronymLines = []
for acronym in acronyms:
    acronymLines.append(len(file_contents[acronym]))

# Interlace the data
for i in range(int(50000 / len(acronyms))):
    # Loop through systems
    for index, acronym in enumerate(acronyms):
        # Get the amount of lines in a file
        maxLine = acronymLines[index]

        # Get target line for coordinate values
        target = random_target(var, maxLine)

        # Get line from chaos system and selected line
        line = file_contents[acronym][target - 1]
        output_file.write(f'{line}')

        # Get next prng seed by adding the coordinate values and take the absolute value
        values = line.split()
        var = abs(sum(float(value) for value in values))

print("Combined file data\n")
