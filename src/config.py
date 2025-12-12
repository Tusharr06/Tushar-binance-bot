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
    binance_api_key: Optional[str]
    binance_api_secret: Optional[str]
    dry_run: bool
    bot_logfile: str
    default_symbol: str
    default_quantity: float

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
        binance_api_key=api_key,
        binance_api_secret=api_secret,
        dry_run=dry_run,
        bot_logfile=os.getenv("BOT_LOGFILE", "bot.log"),
        default_symbol=os.getenv("DEFAULT_SYMBOL", "BTCUSDT"),
        default_quantity=default_quantity
    )

CONFIG: BotConfig = load_config()
