import os
from dataclasses import dataclass
from typing import Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

@dataclass
class BotConfig:
    BINANCE_API_KEY: Optional[str]
    BINANCE_API_SECRET: Optional[str]
    DRY_RUN: bool
    BOT_LOGFILE: str
    DEFAULT_SYMBOL: str
    DEFAULT_QUANTITY: float

def load_config() -> BotConfig:
    dry_run_str = os.getenv("DRY_RUN", "true").lower()
    dry_run = dry_run_str in ("true", "1", "yes", "on")

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    # Validate API keys only if not in dry-run mode
    if not dry_run:
        if not api_key or not api_secret:
            raise ValueError("BINANCE_API_KEY and BINANCE_API_SECRET are required when DRY_RUN is false.")

    try:
        default_quantity = float(os.getenv("DEFAULT_QUANTITY", "0.001"))
        if default_quantity <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("DEFAULT_QUANTITY must be a positive float.")

    return BotConfig(
        BINANCE_API_KEY=api_key,
        BINANCE_API_SECRET=api_secret,
        DRY_RUN=dry_run,
        BOT_LOGFILE=os.getenv("BOT_LOGFILE", "bot.log"),
        DEFAULT_SYMBOL=os.getenv("DEFAULT_SYMBOL", "BTCUSDT"),
        DEFAULT_QUANTITY=default_quantity
    )

CONFIG: BotConfig = load_config()
