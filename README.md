# tushar-binance-bot

## 1. Project Overview

This is a **CLI-based Binance USDT-M Futures trading bot** designed for automated trading strategies. It supports multiple order types including Market, Limit, and skeletons for advanced strategies like OCO (One-Cancels-the-Other) and TWAP (Time-Weighted Average Price). The bot features robust input validation, structured logging, a safety-first dry-run mode, and a modular architecture for easy extensibility.

## 2. Order Types Implemented

The bot currently supports the following order types:

*   **Market Orders**: Immediate execution at the current market price. Fully implemented with validation and live/dry-run modes.
*   **Limit Orders**: Placed at a specific price. Fully implemented with validation and live/dry-run modes.
*   **OCO Orders (Skeleton)**: Structure for One-Cancels-the-Other orders. Validates inputs and returns a mock response in dry-run.
*   **TWAP Strategy (Skeleton)**: Structure for Time-Weighted Average Price strategy. Calculates slices and returns a plan in dry-run logic.

## 3. Architecture Overview

The project follows a modular design:

*   **`src/config.py`**: Handles environment variable loading (`.env`) and configuration validation using `dataclasses`.
*   **`src/logger.py`**: Provides a singleton-like logger with rotating file handlers and console output.
*   **`src/orders/binance_client.py`**: A wrapper around the `binance-connector-python` library. It handles authentication and toggles between real API calls and dry-run simulations.
*   **`src/orders/market_orders.py`**: Logic for placing market orders.
*   **`src/orders/limit_orders.py`**: Logic for placing limit orders.
*   **`src/orders/advanced/`**: Directory for advanced strategies like `oco.py` and `twap.py`.

## 4. Dry-Run Mode

**Safety First**: The bot includes a `DRY_RUN` mode, configurable via the `.env` file or CLI flag `--dry-run`.

*   **No Real Trades**: In this mode, no requests are sent to the Binance matching engine.
*   **Safe for Testing**: Ideal for validating logic, configuration, and API connectivity without risking capital.
*   **Response Simulation**: The bot returns structured JSON responses mimicking API behavior.

## 5. Usage & Example Outputs

### Market Order (Dry-Run)
```bash
python src/cli.py market BTCUSDT BUY 0.001 --dry-run
```
**Output:**
```json
{
  "status": "dry-run",
  "action": "create_market_order",
  "payload": {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "MARKET",
    "quantity": 0.001,
    "reduceOnly": false
  }
}
```

### Limit Order (Dry-Run)
```bash
python src/cli.py limit BTCUSDT BUY 0.001 45000 --dry-run
```
**Output:**
```json
{
  "status": "dry-run",
  "action": "create_limit_order",
  "payload": {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "quantity": 0.001,
    "price": "45000.0",
    "timeInForce": "GTC",
    "reduceOnly": false
  }
}
```

## 6. Installation

1.  **Clone repo**:
    ```bash
    git clone https://github.com/yourusername/tushar-binance-bot.git
    cd tushar-binance-bot
    ```
2.  **Create virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate # Windows
    source venv/bin/activate # Linux/Mac
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Setup Environment**:
    Copy `.env.example` to `.env` and configure your API keys.

## 7. How to Extend

This bot is designed to be a foundation for a more complex trading system.

*   **Stop-Limit**: Implement logic similar to `limit_orders.py` but with `STOP` or `STOP_MARKET` types.
*   **Trailing Stop**: Add a callback mechanism to adjust stop prices based on market movement.
*   **Grid Trading**: utilize the `src/orders/advanced/` folder to build a stateful grid runner.
*   **Real TWAP**: Convert the skeleton into a loop that executes `market_orders` over the specified interval.
