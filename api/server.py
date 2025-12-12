from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

# Add parent dir to path so we can import src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.orders.binance_client import BinanceClient
from src.logger import get_logger
from src.config import CONFIG

logger = get_logger("API_SERVER")
app = Flask(__name__)
CORS(app) # Enable CORS for frontend

# Initialize Binance Client (respects DRY_RUN from .env/config)
client = BinanceClient()

@app.route('/api/ping', methods=['GET'])
def ping():
    logger.info("API: Ping request received")
    return jsonify({"status": "ok", "message": "Pong", "dry_run": client.dry_run})

@app.route('/api/market', methods=['POST'])
def market_order():
    try:
        data = request.json
        symbol = data.get('symbol')
        side = data.get('side')
        quantity = float(data.get('quantity'))
        
        logger.info(f"API: Market Order Request - {side} {quantity} {symbol}")
        
        # Call existing logic
        response = client.create_market_order(symbol, side, quantity)
        return jsonify(response)
    except Exception as e:
        logger.error(f"API: Market Order Failed - {str(e)}")
        return jsonify({"error": str(e)}), 400

@app.route('/api/limit', methods=['POST'])
def limit_order():
    try:
        data = request.json
        symbol = data.get('symbol')
        side = data.get('side')
        quantity = float(data.get('quantity'))
        price = float(data.get('price'))
        
        logger.info(f"API: Limit Order Request - {side} {quantity} {symbol} @ {price}")
        
        # Call existing logic
        response = client.create_limit_order(symbol, side, quantity, price)
        return jsonify(response)
    except Exception as e:
        logger.error(f"API: Limit Order Failed - {str(e)}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = 5000
    print(f"Starting generic Flask API on port {port}...")
    print(f"DRY_RUN Mode: {client.dry_run}")
    app.run(debug=True, port=port)
