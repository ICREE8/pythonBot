import json

def get_inflation_data():
    with open('../data/currency_inflation_data.json', 'r') as file:
        return json.load(file)
