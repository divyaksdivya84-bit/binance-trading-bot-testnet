from order_manager import OrderManager
from risk_manager import RiskManager
from config import SYMBOL, TRADE_QTY
from logger import logger

class TradingBot:
    def __init__(self):
        self.order_mgr = OrderManager()
        self.risk_mgr = RiskManager()
    
    def run(self):
        logger.info("Bot started")
        if self.risk_mgr.check_order(TRADE_QTY):
            self.order_mgr.place_market_buy(SYMBOL, TRADE_QTY)
        logger.info("Bot finished")

if __name__ == "__main__":
    bot = TradingBot()
    bot.run()
