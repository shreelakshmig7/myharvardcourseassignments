import json
import requests
import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    try:
        no_of_bitcoins = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_info = response.json()
        price = bitcoin_info["bpi"]["USD"]["rate_float"]
        final_price = no_of_bitcoins * price
        print(f"${final_price:,.4f}")

    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit("Unsuccessful Request")


if __name__ == "__main__":
    main()
