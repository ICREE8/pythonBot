import user_input
import calculations

def main():
    # Get user input
    amount, currency = user_input.get_user_amount_and_currency()

    # Calculate the value of crypto vs fiat
    crypto_value = calculations.calculate_crypto_equivalent(amount, currency)

    # Print result
    print(f"If you had invested {amount} {currency} in crypto, it would be worth: {crypto_value}")

if __name__ == "__main__":
    main()