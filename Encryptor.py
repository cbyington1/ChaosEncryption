import base64
import shutil
import subprocess
import time
import hashlib
from cryptography.fernet import Fernet

# Example parsed values
# Full example: "LS[10][28][100][100][0.5][0.5][0.5], LM[3.57][100][500], RS[0.2][5][200][200][0.5][0.5][0.5], HS[0.25][0.15][0.22][0.12][100000]"

# Get user input
parameter_key = "LM[3.57][100][500]"
string = "pin-pon!"

# Record the start time
start_time = time.time()

try:
    proc = subprocess.run(["python", "FileSetup.py", parameter_key], check=True)
except subprocess.CalledProcessError:
    exit(1)

# Get final values
file_path = 'chaos_coordinates/combined_values.txt'
with open(file_path, 'r') as file:
    plaintext = file.read()

# Use SHA-256 to compute the hash
sha256 = hashlib.sha256()
sha256.update(plaintext.encode('utf-8'))
hash_value = sha256.digest()

# Convert the hash value to base64-encoded key
key = base64.urlsafe_b64encode(hash_value)

# Create a Fernet symmetric key cipher
cipher_suite = Fernet(key)

# Encrypt string
encrypted_string = cipher_suite.encrypt(string.encode('utf-8'))

# Print the encrypted string
print("Encrypted String:", encrypted_string)

# Calculate and print the execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"\nExecution time: {execution_time} seconds")

#Removes folders and contents
#shutil.rmtree("chaos_coordinates", ignore_errors=True)
#shutil.rmtree("chaos_graphs", ignore_errors=True)