import requests

# Defining the function to convert currencies
def converting_currency():
    print("***--- WELCOME TO THE CURRENCY CONVERTER ---***")
    print("Example currencies: USD, INR, EUR, JPY, AUD, CAD, and so on...\n")

    # Using try-except blocks to handle exceptions
    try:
        # Getting input from the user
        amount = float(input("Enter the amount: "))
        from_currency = input("Convert from: ").upper()
        to_currency = input("Convert to: ").upper()

        # Setting up the API URL
        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        response = requests.get(url)

        # Parsing the API response into a dictionary named 'data'
        data = response.json()

        # Checking whether the API call was successful
        if data["result"] == 'success':
            # Retrieving the exchange rate
            rate = data["rates"].get(to_currency)

            if rate:
                # Performing the currency conversion
                result = rate * amount
                print(f"\nCurrent exchange rate: 1 {from_currency} = {rate:.4f} {to_currency}")
                print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            else:
                print(f"Currency code '{to_currency}' not found.")
        else:
            print("Conversion failed. Please check the currency codes.")

    except ValueError:
        print("Please enter a valid numeric value.")
    except requests.exceptions.RequestException:
        print("Failed to connect. Please check your internet connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Loop for multiple conversions
while True:
    converting_currency()
    again = input("\nDo you want to convert another amount? (Yes/No): ").lower()
    if again != "yes" and again != 'y':
        print("\nThank you for using the currency converter!")
        break
