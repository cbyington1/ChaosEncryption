import base64
import shutil
import subprocess
import time
import hashlib
from cryptography.fernet import Fernet

# Get user input
parameter_key = "LM[3.57][100][500]"
encoded_message = b'gAAAAABlSvmuIunJ1bEULebBoNAIi1ZZ4HOr0yLaz4CBb2qYV9mdIwaA0uHVCzuwPNb52ak7OH-c2iP0oi2h4bj8gV6hk2p1KA=='

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

# Decrypt string
#Error occurs here when key and byte string do not match
try:
    decrypted_string = cipher_suite.decrypt(encoded_message)

except:
    print("Parameter key and encoded message do not match")
    exit(1)


# Print the decrypted string
print("Decrypted String:", decrypted_string.decode('utf-8'))

# Calculate and print the execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"\nExecution time: {execution_time} seconds")

#Removes folders and contents
#shutil.rmtree("chaos_coordinates", ignore_errors=True)
#shutil.rmtree("chaos_graphs", ignore_errors=True)