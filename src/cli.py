import argparse
import sys
import json
from .orders.market_orders import place_market_order
from .orders.limit_orders import place_limit_order
from .orders.binance_client import BinanceClient
from .logger import get_logger

logger = get_logger(__name__)

def main():
    # Parent parser for shared arguments
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("--dry-run", action="store_true", help="Force dry-run mode (no real trades)")

    parser = argparse.ArgumentParser(description="Tushar Binance Bot CLI", parents=[parent_parser])
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Market Order Parser
    market_parser = subparsers.add_parser("market", help="Place a Market Order", parents=[parent_parser])
    market_parser.add_argument("symbol", type=str, help="Trading symbol (e.g. BTCUSDT)")
    market_parser.add_argument("side", type=str, choices=["BUY", "SELL"], help="Order side (BUY/SELL)")
    market_parser.add_argument("quantity", type=float, help="Order quantity")

    # Limit Order Parser
    limit_parser = subparsers.add_parser("limit", help="Place a Limit Order", parents=[parent_parser])
    limit_parser.add_argument("symbol", type=str, help="Trading symbol (e.g. BTCUSDT)")
    limit_parser.add_argument("side", type=str, choices=["BUY", "SELL"], help="Order side (BUY/SELL)")
    limit_parser.add_argument("quantity", type=float, help="Order quantity")
    limit_parser.add_argument("price", type=float, help="Limit price")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Initialize Client
    try:
        # If --dry-run is present, pass True. Otherwise pass None to let config decide.
        dry_run_override = True if args.dry_run else None
        client = BinanceClient(dry_run=dry_run_override)
        
        response = None

        if args.command == "market":
            response = place_market_order(
                client=client,
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity
            )
            
        elif args.command == "limit":
            response = place_limit_order(
                client=client,
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price
            )

        # Output the result
        if response:
            print(json.dumps(response, indent=2))
            
    except Exception as e:
        logger.error(f"Command failed: {e}")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
