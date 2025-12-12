from typing import Dict, Any
from ..utils.validation import validate_symbol, validate_quantity, validate_price
from ..logger import get_logger

logger = get_logger(__name__)

def place_limit_order(client, symbol: str, side: str, quantity: float, price: float) -> Dict[str, Any]:
    """
    Places a limit order after validating inputs.
    
    Args:
        client: Instance of BinanceClient.
        symbol: Trading pair symbol (e.g. BTCUSDT).
        side: "BUY" or "SELL".
        quantity: Order quantity.
        price: Limit price.
        
    Returns:
        Structured API response from BinanceClient.
        
    Raises:
        ValueError: If validation fails.
    """
    logger.info(f"Received Limit Order Request: {side} {quantity} {symbol} @ {price}")
    
    # 1. Validate Symbol
    if not validate_symbol(symbol):
        error_msg = f"Invalid symbol: {symbol}"
        logger.error(error_msg)
        raise ValueError(error_msg)
        
    # 2. Validate Quantity
    if not validate_quantity(quantity):
        error_msg = f"Invalid quantity: {quantity}"
        logger.error(error_msg)
        raise ValueError(error_msg)

    # 3. Validate Price
    if not validate_price(price):
        error_msg = f"Invalid price: {price}"
        logger.error(error_msg)
        raise ValueError(error_msg)
        
    # 4. Validate Side
    if side not in ["BUY", "SELL"]:
        error_msg = f"Invalid side: {side}. Must be BUY or SELL."
        logger.error(error_msg)
        raise ValueError(error_msg)
        
    logger.debug("Validation successful. Executing limit order...")
    
    try:
        response = client.create_limit_order(symbol, side, quantity, price)
        logger.info(f"Limit Order executed successfully: {response}")
        return response
    except Exception as e:
        logger.exception(f"Error executing limit order for {symbol}")
        raise e
