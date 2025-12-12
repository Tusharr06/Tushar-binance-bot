@echo off
echo ==============================================
echo Tushar Binance Bot - Market Order Runner
echo ==============================================
echo.
echo Running in DRY-RUN mode...
echo.
python -m src.cli market BTCUSDT BUY 0.001 --dry-run
echo.
echo ==============================================
echo If you see the JSON output above, it works!
echo ==============================================
pause
