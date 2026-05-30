import sys
import requests

# check for command-line argument
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

# if argument is not a number, print error message and exit
try:
    n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

# get current price of bitcoin in USD
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=6bb407337027939a8c49896da777fcc2ba40ec123e01f56bdeede1a1ff618f15")
    data = response.json()
    price = float(data["data"]["priceUsd"])
    price *= n
except requests.RequestException:
    print("Error fetching data from API")
    sys.exit(1)

print(f"${price:,.4f}")