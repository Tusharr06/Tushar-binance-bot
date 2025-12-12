# tushar-binance-bot

## 1. Project Overview

This is a **CLI-based Binance USDT-M Futures trading bot** designed for automated trading strategies. It supports multiple order types including Market, Limit, and planned support for Stop-Limit, OCO (One-Cancels-the-Other), TWAP (Time-Weighted Average Price), and Grid trading strategies. The bot features robust input validation, structured logging, a safety-first dry-run mode, and a modular architecture for easy extensibility.

## 2. Features

*   **Market Order execution**: Immediate execution at current market price.
*   **Limit Orders**: Place orders at a specific price.
*   **Stop-Limit Orders (planned)**: Trigger limit orders based on stop price.
*   **OCO Orders (planned)**: Conditional orders where one cancels the other.
*   **TWAP strategy (planned)**: Execute large orders over time to minimize market impact.
*   **Grid strategy (planned)**: Automated grid trading functionality.
*   **Config loader (`.env`)**: Secure environment variable management.
*   **Structured logging (`bot.log`)**: Detailed logs for debugging and auditing.
*   **Input validation utilities**: Ensures data integrity before execution.

## 3. Installation

1.  **Python version**: Ensure you have Python 3.8 or higher installed.
2.  **Clone repo**:
    ```bash
    git clone https://github.com/yourusername/tushar-binance-bot.git
    cd tushar-binance-bot
    ```
3.  **Create virtual environment**:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```
4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 4. Environment Setup (`.env`)

Create a `.env` file in the root directory. You can use `.env.example` as a template.

**Sample Configuration:**
```ini
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_here
DRY_RUN=true
BOT_LOGFILE=bot.log
DEFAULT_SYMBOL=BTCUSDT
DEFAULT_QUANTITY=0.001
```

**DRY_RUN Mode**: When set to `true`, the bot will simulate order execution without placing actual trades on the exchange. This is essential for testing strategies safely.

## 5. CLI Usage Examples

**Market order (dry-run):**
```bash
python src/cli.py market BTCUSDT BUY 0.001 --dry-run
```

**Limit order (dry-run):**
```bash
python src/cli.py limit BTCUSDT BUY 0.001 45000 --dry-run
```

## 6. Project Folder Structure

```
tushar-binance-bot/
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── logger.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── validation.py
│   ├── orders/
│   │   ├── __init__.py
│   │   ├── market_orders.py
│   │   ├── limit_orders.py
│   │   └── advanced/
│   │       ├── __init__.py
│   │       ├── oco.py
│   │       └── twap.py
│   └── config.py
├── bot.log
├── README.md
├── report.pdf
├── requirements.txt
├── .gitignore
└── .env.example
```

## 7. Future Enhancements

*   **OCO implementation**: Full support for One-Cancels-the-Other orders.
*   **TWAP scheduler**: Time-based execution logic.
*   **Grid trading**: Grid bot strategy implementation.
*   **API client wrapper**: Abstracted Binance API interaction.
*   **Error-handling improvements**: Enhanced resilience and error reporting.
*   **`report.pdf` documentation**: Comprehensive documentation include in the repo.
