def validate_currency(currency, available_currencies):
    if currency not in available_currencies:
        raise ValueError(f"Currency {currency} is not supported.")
