from src.logger import get_logger

log = get_logger(__name__)
log.info("Logger test INFO")
log.error("Logger test ERROR")
print("Logger test completed.")
