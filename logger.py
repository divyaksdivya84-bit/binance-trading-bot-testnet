import logging
from datetime import datetime

def setup_logger():
    logging.basicConfig(
        filename=f'bot_{datetime.now().strftime("%Y%m%d")}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

logger = setup_logger()
