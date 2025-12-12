import logging
import time
from typing import Optional, Dict, Any, List, Union
from src.config import CONFIG
from src.logger import get_logger

logger = get_logger(__name__)

class BinanceClient:
    def __init__(self, key: Optional[str] = None, secret: Optional[str] = None, dry_run: Optional[bool] = None):
        self.key = key or CONFIG.binance_api_key
        self.secret = secret or CONFIG.binance_api_secret
        self.dry_run = dry_run if dry_run is not None else CONFIG.dry_run
        
        self.client = None
        
        logger.info(f"Initializing BinanceClient (Dry Run: {self.dry_run})")
        
        if not self.dry_run:
            try:
                from binance.um_futures import UMFutures
                self.client = UMFutures(key=self.key, secret=self.secret)
                logger.info("Connected to Binance UMFutures Client")
            except ImportError:
                logger.error("binance-connector-python not installed. Live mode requires it.")
                raise ImportError("Please install 'binance-connector' to run in live mode.")

    def ping(self) -> Dict[str, Any]:
        logger.debug("Pinging Binance API...")
        if self.dry_run:
            return {"status": "dry-run", "serverTime": int(time.time() * 1000)}
        
        try:
            return self.client.time()
        except Exception as e:
            logger.exception("Error during ping")
            raise

    def get_account(self) -> Dict[str, Any]:
        logger.debug("Fetching account information...")
        if self.dry_run:
            return {
                "status": "dry-run",
                "assets": [],
                "positions": [],
                "canDeposit": True,
                "canTrade": True,
                "canWithdraw": True,
                "feeTier": 0,
                "updateTime": int(time.time() * 1000)
            }
        
        try:
            return self.client.account()
        except Exception as e:
            logger.exception("Error fetching account info")
            raise

    def get_balance(self, asset: str = "USDT") -> float:
        account = self.get_account()
        if self.dry_run:
            # Mock balance for dry run
            return 10000.0
        
        for bal in account.get("assets", []):
            if bal.get("asset") == asset:
                return float(bal.get("walletBalance", 0.0))
        return 0.0

    def create_market_order(self, symbol: str, side: str, quantity: float, reduce_only: bool = False) -> Dict[str, Any]:
        logger.info(f"Placing MARKET Order: {side} {quantity} {symbol} (ReduceOnly: {reduce_only})")
        
        if self.dry_run:
            return {
                "status": "dry-run",
                "action": "create_market_order",
                "payload": {
                    "symbol": symbol,
                    "side": side,
                    "type": "MARKET",
                    "quantity": quantity,
                    "reduceOnly": reduce_only
                }
            }
        
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": "MARKET",
                "quantity": quantity,
                "reduceOnly": reduce_only
            }
            response = self.client.new_order(**params)
            logger.info(f"Market Order Placed: {response.get('orderId')}")
            return response
        except Exception as e:
            logger.exception(f"Failed to place market order: {side} {symbol}")
            raise

    def create_limit_order(self, symbol: str, side: str, quantity: float, price: float, timeInForce: str = "GTC", reduce_only: bool = False) -> Dict[str, Any]:
        logger.info(f"Placing LIMIT Order: {side} {quantity} {symbol} @ {price} (ReduceOnly: {reduce_only})")
        
        if self.dry_run:
            return {
                "status": "dry-run",
                "action": "create_limit_order",
                "payload": {
                    "symbol": symbol,
                    "side": side,
                    "type": "LIMIT",
                    "quantity": quantity,
                    "price": str(price),
                    "timeInForce": timeInForce,
                    "reduceOnly": reduce_only
                }
            }
        
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": "LIMIT",
                "quantity": quantity,
                "price": str(price),
                "timeInForce": timeInForce,
                "reduceOnly": reduce_only
            }
            response = self.client.new_order(**params)
            logger.info(f"Limit Order Placed: {response.get('orderId')}")
            return response
        except Exception as e:
            logger.exception(f"Failed to place limit order: {side} {symbol} @ {price}")
            raise
