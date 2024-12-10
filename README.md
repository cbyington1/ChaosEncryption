# Chaos-Based Encryption System

This project implements a novel encryption system that uses chaos theory and dynamical systems to generate encryption keys. The system combines multiple chaotic attractors to create unique, deterministic encryption keys based on specific parameter sets.

# System Overview

The encryption system consists of three main components:

1. **Chaotic Systems Generator**: Multiple implementation files (Lorenz, Rossler, etc.) that generate chaotic coordinates based on specific parameters
2. **Encryptor**: Converts messages into encrypted byte strings using chaos-derived keys
3. **Decryptor**: Recovers original messages using matching parameter keys

# Key Features

- Parameter-based key generation using chaotic systems
- Symmetric encryption using Fernet (implementation of AES)
- Deterministic key generation from chaotic coordinates
- Multi-threaded chaotic system computation
- Visualization capabilities for chaotic attractors

# Prerequisites

- Python 3.7+
- Required Python packages:
```
cryptography
numpy
matplotlib
scipy
```

# Installation

1. Clone the repository
2. Install required packages:
```bash
pip install cryptography numpy matplotlib scipy
```
3. Ensure all system files are in the same directory

# Usage

## Encryption
```python
# Example encryption command
python encryptor.py "LM[3.57][100][500]" "Your message here"
```

Parameter key format: `SystemType[param1][param2]...[paramN]`

Available system types:
- LS: Lorenz System
- RS: Rossler System
- LM: Logistic Map
- HS: Henon System

## Decryption
```python
# Example decryption command
python decryptor.py "LM[3.57][100][500]" "encrypted_message_bytes"
```

**Note**: The parameter key must match the one used for encryption exactly.

# Parameter Key Format

Each chaotic system requires specific parameters. Here's the format for each:

## Lorenz System (LS)
```
LS[sigma][rho][time][iterations][x0][y0][z0]
Example: LS[10][28][100][100][0.5][0.5][0.5]
```

## Logistic Map (LM)
```
LM[r][iterations][population]
Example: LM[3.57][100][500]
```

## Rossler System (RS)
```
RS[a][b][time][iterations][x0][y0][z0]
Example: RS[0.2][5][200][200][0.5][0.5][0.5]
```

## Henon System (HS)
```
HS[a][b][x0][y0][iterations]
Example: HS[0.25][0.15][0.22][0.12][100000]
```

# How It Works

1. **Key Generation**:
- The system uses the provided parameters to generate chaotic coordinates
- These coordinates are combined and hashed using SHA-256
- The hash is converted to a base64-encoded Fernet key

2. **Encryption Process**:
- Creates chaotic coordinates using the parameter key
- Generates a deterministic encryption key
- Uses Fernet symmetric encryption to encrypt the message

3. **Decryption Process**:
- Recreates the same chaotic coordinates using the parameter key
- Regenerates the identical encryption key
- Decrypts the message using Fernet

# File Structure
```
├── encryptor.py
├── decryptor.py
├── FileSetup.py
├── LorenzSystem.py
├── RosslerSystem.py
├── LogisticMap.py
├── HenonSystem.py
└── /chaos_coordinates/
    └── combined_values.txt
└── /chaos_graphs/
    └── system_visualization.png
```

# Security Considerations

- The security of the system depends on keeping the parameter key secret
- The chaotic systems provide deterministic but highly sensitive key generation
- Parameter keys should be transmitted securely between parties
- The system uses standard cryptographic libraries for the actual encryption/decryption

# Error Handling

The system includes error handling for:
- Mismatched parameter keys and encrypted messages
- Invalid parameter formats
- File system errors
- Encryption/decryption failures

# Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

# License

[Insert your chosen license here]
