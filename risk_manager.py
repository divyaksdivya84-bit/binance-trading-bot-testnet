from config import TRADE_QTY
from logger import logger

class RiskManager:
    def __init__(self, max_qty=TRADE_QTY):
        self.max_qty = max_qty
    
    def check_order(self, qty):
        if qty > self.max_qty:
            logger.warning(f"Order qty {qty} exceeds max {self.max_qty}")
            return False
        logger.info(f"Risk check passed for qty {qty}")
        return True
