import currency_data
import crypto_data

def calculate_crypto_equivalent(amount, currency):
    # Get inflation data
    inflation_data = currency_data.get_inflation_data()
    
    # Get crypto price data
    crypto_prices = crypto_data.get_crypto_data()
    
    # Calculate equivalent value for BTC and ETH
    btc_value = (amount / inflation_data[currency]['current_value']) * crypto_prices['bitcoin']['usd']
    eth_value = (amount / inflation_data[currency]['current_value']) * crypto_prices['ethereum']['usd']
    
    return {'BTC': btc_value, 'ETH': eth_value}
