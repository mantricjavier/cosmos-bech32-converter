# Cosmos Bech32 Converter

Convert Bech32 addresses from one HRP to another.

## Usage

`python convert_addresses.py <new_hrp>`
Replace <new_hrp> with the actual HRP you want to use (e.g., cosmos, terra, etc.).

### Input File
The script reads addresses from a file named addresses.txt. Each line should contain a single Bech32 address.

### Output File
The converted addresses are written to a file named addresses-<new_hrp>.txt, where <new_hrp> is the HRP used in the command (e.g., addresses-cosmos.txt).

## Requirements
Python 3.x
bech32 library (`pip install bech32`)

## Notes
The script assumes that each line in addresses.txt contains a single Bech32 address.
If an invalid Bech32 address is found, the script will print an error message and skip it.

## Disclaimer
Use at your own risk. Careful with Terra as they use a different coin type and the derived address will likely not be the one you expect.