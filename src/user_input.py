def get_user_amount_and_currency():
    amount = float(input("Enter the amount you want to calculate: "))
    currency = input("Enter the currency (e.g., USD): ").upper()
    return amount, currency
