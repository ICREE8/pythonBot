# Python Currency Bot
A Python currency bot is a basic application that allows users to quickly and easily convert between different currencies. By leveraging a currency exchange API, such as the one provided by Fixer.io, the bot can access real-time exchange rates and provide accurate conversions.

## Functionality
The bot's core functionality involves:

- Retrieving Exchange Rates: Using the Fixer.io API, the bot fetches the latest exchange rates for various currency pairs.
- User Input: The bot prompts the user to enter the amount they wish to convert, the base currency, and the target currency.
- Conversion Calculation: Based on the provided information and the retrieved exchange rates, the bot performs the necessary calculations to determine the converted amount.
- Displaying Results: The bot presents the calculated result to the user, along with the date and time of the conversion.

# Enhanced Bot Experience

## To improve the user experience, the bot can incorporate additional features such as:

- History: Storing a record of previous conversions for easy reference.
- Favorites: Allowing users to save frequently used currency pairs.
- Multiple Languages: Supporting different languages to cater to a wider audience.
- Integration: Integrating with messaging platforms or voice assistants for convenient access.

By implementing these enhancements, the currency bot becomes a more versatile and user-friendly tool for various needs.

```
import requests

def get_exchange_rate(base_currency, target_currency):
    api_key = "YOUR_API_KEY"
    url = f"https://api.fixer.io/latest?base={base_currency}&access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

# Get user input
amount = float(input("Enter the amount to convert: "))
base_currency = input("Enter the base currency (e.g., USD): ")
target_currency = input("Enter the target currency (e.g., EUR): ")

# Perform conversion
result = convert_currency(amount, base_currency, target_currency)

# Display result
print(f"{amount} {base_currency} is equal to {result} {target_currency}")

```

