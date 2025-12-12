# Project Report – tushar-binance-bot

## 1. Introduction
The **tushar-binance-bot** is a command-line interface (CLI) tools designed to interact with the Binance USDT-M Futures market. It serves as a foundation for automated trading, allowing users to execute orders safely and efficiently. The project uses Python 3, strict typing, and a modular architecture to ensure reliability and maintainability.

## 2. System Architecture
The system relies on several core components:

*   **Config Loader**: A robust configuration management system (`src/config.py`) that loads sensitive keys and settings from environment variables, ensuring security.
*   **Logger**: A centralized logging module (`src/logger.py`) that captures execution details, errors, and trade information in both the console and rotating log files.
*   **Binance Client Wrapper**: An abstraction layer (`src/orders/binance_client.py`) over the official Binance connector. It provides a unified interface for orders and implements the critical "Dry-Run" logic.
*   **Order Modules**: Dedicated modules for each order type (Market, Limit, OCO, TWAP), ensuring separation of concerns.
*   **CLI Flow**: A user-friendly entry point (`src/cli.py`) utilizing `argparse` to parse commands and dispatch them to the appropriate handlers.

## 3. Features Implemented
*   **Market Orders**: Instant execution functionality with full validation.
*   **Limit Orders**: Precision (price-target) order placement.
*   **OCO Skeleton**: A foundational structure for One-Cancels-the-Other conditional orders.
*   **TWAP Skeleton**: A design pattern for Time-Weighted Average Price algorithmic execution.
*   **DRY_RUN Mode**: A simulation layer that allows full system testing without financial risk.

## 4. Execution Flow
1.  **User Input**: User issues a command via CLI (e.g., `market BTCUSDT BUY 0.1`).
2.  **Parsing**: `src/cli.py` parses arguments.
3.  **Validation**: Inputs are treated by `src/utils/validation.py` to ensure correctness (e.g., positive quantity, valid symbol format).
4.  **Handler**: The request is routed to the specific order module (e.g., `market_orders.py`).
5.  **Client Dispatch**: The `BinanceClient` checks for Dry-Run mode.
6.  **Execution**:
    *   If **Dry-Run**: A JSON object representing the would-be request is returned.
    *   If **Live**: The request is signed and sent to the Binance API.
7.  **Response**: The result is logged and printed to the standard output.

## 5. Testing and Validation
Testing was primarily conducted using **Dry-Run** mode. This allowed for:
*   Verification of the entire pipeline (CLI -> Validation -> Client -> Output) without needing real funds.
*   Validation of error handling (e.g., invalid symbols, negative quantities) by intentionally providing bad inputs.
*   Confirmation that the correct API parameters would be generated for live trading.

## 6. Future Enhancements
*   **Full OCO & TWAP**: Implementing the live logic for the skeletons.
*   **WebSocket Integration**: Listening to real-time market data for triggering automated strategies.
*   **Position Management**: Adding commands to view and manage open positions and PnL.
*   **Database**: Storing trade history in a local SQLite database for analysis.

## 7. Conclusion
The **tushar-binance-bot** successfully establishes a secure, modular, and extensible framework for algorithmic trading on Binance Futures. It meets all initial requirements for structure, safety, and basic order execution, paving the way for advanced strategy implementation.
