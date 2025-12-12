from typing import Dict, Any
from ..utils.validation import validate_symbol, validate_quantity
from ..logger import get_logger

logger = get_logger(__name__)

def place_market_order(client, symbol: str, side: str, quantity: float) -> Dict[str, Any]:
    """
    Places a market order after validating inputs.
    
    Args:
        client: Instance of BinanceClient.
        symbol: Trading pair symbol (e.g. BTCUSDT).
        side: "BUY" or "SELL".
        quantity: Order quantity.
        
    Returns:
        Structured API response from BinanceClient.
        
    Raises:
        ValueError: If validation fails.
    """
    logger.info(f"Received Market Order Request: {side} {quantity} {symbol}")
    
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
        
    # 3. Validate Side
    if side not in ["BUY", "SELL"]:
        error_msg = f"Invalid side: {side}. Must be BUY or SELL."
        logger.error(error_msg)
        raise ValueError(error_msg)
        
    logger.debug("Validation successful. Executing order...")
    
    try:
        response = client.create_market_order(symbol, side, quantity)
        logger.info(f"Market Order executed successfully: {response}")
        return response
    except Exception as e:
        logger.exception(f"Error executing market order for {symbol}")
        raise e
