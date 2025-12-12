from src.utils.validation import validate_symbol, validate_quantity, validate_price
print("Symbol BTCUSDT:", validate_symbol("BTCUSDT"))
print("Symbol BTC/USDT:", validate_symbol("BTC/USDT"))
print("Qty 0.01:", validate_quantity(0.01))
print("Qty -1:", validate_quantity(-1))
print("Price 45000:", validate_price(45000))
