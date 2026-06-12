from trading_bot import TradingBot
from logger import logger

def main():
    print("Binance Testnet Bot Starting...")
    logger.info("Application started")
    bot = TradingBot()
    bot.run()
    print("Bot execution completed. Check log file.")

if __name__ == "__main__":
    main()
