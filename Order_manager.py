from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL
from logger import logger

class OrderManager:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.API_URL = BASE_URL
    
    def place_market_buy(self, symbol, qty):
        try:
            order = self.client.order_market_buy(symbol=symbol, quantity=qty)
            logger.info(f"Buy order placed: {order['orderId']}")
            return order
        except Exception as e:
            logger.error(f"Order failed: {e}")
            return None
