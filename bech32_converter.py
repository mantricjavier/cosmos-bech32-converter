import sys
import bech32


def convert_bech32_address(address, new_hrp):
    # Split the address into HRP and data
    current_hrp, data = bech32.bech32_decode(address)

    # Check if the address is a valid Bech32 address
    if not data:
        print(f"Invalid Bech32 address: {address}")
        return None

    # Replace the HRP with the new one
    new_address = bech32.bech32_encode(new_hrp, data)

    return new_address


def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_addresses.py <new_hrp>")
        sys.exit(1)

    new_hrp = sys.argv[1]

    try:
        with open("addresses.txt", "r") as f:
            addresses = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("addresses.txt not found")
        sys.exit(1)

    converted_addresses = []
    for address in addresses:
        converted_address = convert_bech32_address(address, new_hrp)
        if converted_address:
            converted_addresses.append(converted_address)

    with open(f"addresses-{new_hrp}.txt", "w") as f:
        for address in converted_addresses:
            f.write(address + "\n")


if __name__ == "__main__":
    main()
