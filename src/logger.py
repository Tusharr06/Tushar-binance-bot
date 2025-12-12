import logging
import sys
import os
from typing import Optional
from logging.handlers import RotatingFileHandler

# Default log format
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_logger(name: str, logfile: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """
    Returns a configured logger with rotating file handler and console handler.
    
    Args:
        name: Name of the logger.
        logfile: Path to the log file. If None, uses environment variable or default.
        level: Logging level.
        
    Returns:
        Configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False
    
    # Avoid adding duplicate handlers
    if logger.handlers:
        return logger
        
    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    
    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File Handler
    if logfile is None:
        logfile = os.getenv("BOT_LOGFILE", "bot.log")
        
    file_handler = RotatingFileHandler(
        logfile,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
