import requests

def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd'
    response = requests.get(url)
    return response.json()

def get_chainlink_data():
    url = 'CHAINLINK_COORDINATES_HERE'
    response = requests.get(url)
    return response.json()

def get_alpaca_data():
    url = 'ALPACA_API_RPC_URL'
    response = requests.get(url)
    return response.json()
