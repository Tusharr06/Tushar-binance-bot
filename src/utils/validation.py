from typing import Any, Optional

def safe_float(value: Any, default: Optional[float] = None) -> Optional[float]:
    """
    Safely converts a value to float.
    
    Args:
        value: The value to convert.
        default: The default value to return if conversion fails.
        
    Returns:
        The float value or default.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def validate_symbol(symbol: str) -> bool:
    """
    Validates a trading symbol.
    
    Rules:
    - Must be alphanumeric
    - Must not contain spaces or slashes
    - Must be uppercase only
    
    Args:
        symbol: The symbol string to validate.
        
    Returns:
        True if valid, False otherwise.
    """
    if not isinstance(symbol, str):
        return False
    if not symbol:
        return False
    if " " in symbol or "/" in symbol:
        return False
    if not symbol.isalnum():
        return False
    if not symbol.isupper():
        return False
    return True

def validate_quantity(quantity: Any) -> bool:
    """
    Validates a trading quantity.
    
    Rules:
    - Must be a number
    - Must be greater than 0
    
    Args:
        quantity: The quantity to validate.
        
    Returns:
        True if valid, False otherwise.
    """
    val = safe_float(quantity)
    return val is not None and val > 0

def validate_price(price: Any) -> bool:
    """
    Validates a trading price.
    
    Rules:
    - Must be a number
    - Must be greater than 0
    
    Args:
        price: The price to validate.
        
    Returns:
        True if valid, False otherwise.
    """
    val = safe_float(price)
    return val is not None and val > 0
