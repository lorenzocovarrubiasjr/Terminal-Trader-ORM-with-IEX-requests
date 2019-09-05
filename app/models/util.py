import requests
from app.models.position import Position


def get_stock_current_price(symbol):
    iex_api = "https://ws-api.iextrading.com/1.0/tops/last"

    query = {"symbols": symbol}

    response = requests.get(iex_api, query)
    stock_data = response.json()
    return stock_data[0]["price"]

        