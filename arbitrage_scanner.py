import ccxt
import time
import winsound
from datetime import datetime

"""
============================================================
🌙 CRYPTO ARBITRAGE SCANNER
============================================================

This script performs real-time spread analysis for selected
cryptocurrency pairs on Binance and logs potential arbitrage
opportunities.

The threshold (0.0003%) is intentionally extremely low to
trigger alerts frequently in a DEMO/EDUCATIONAL environment.

Real arbitrage trading requires much higher thresholds due to:
- trading fees
- slippage
- execution delays
- transfer times between exchanges
- liquidity limitations

This project demonstrates alert + logging system architecture.
============================================================
"""


# ============================================================
# 🌙 SYSTEM PARAMETERS
# ============================================================

THRESHOLD_PCT = 0.0003           # 0.0003% – tiny for demo purposes
CYCLE_COUNT = 20                 # cycles per session
WAIT_SECONDS = 5                 # wait 5 sec between checks
SYMBOLS = ["BTC/USDT", "ETH/USDT"]
LOG_FILE = "arbitrage_log.txt"


# ============================================================
# 🌙 LOGGING FUNCTION
# ============================================================
def log_message(message):
    """Writes a timestamped message to the log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}]  {message}\n")


# ============================================================
# 🌙 MAIN EXECUTION
# ============================================================
exchange = ccxt.binance()

print("\n======================================================================")
print("                    🌙  LIVE ARBITRAGE ANALYSIS  🌙                    ")
print("======================================================================\n")

log_message("=== Arbitrage Session Started ===")

for cycle in range(1, CYCLE_COUNT + 1):

    print(f"\n🌙 CYCLE {cycle}/{CYCLE_COUNT}\n")
    log_message(f"Cycle {cycle}/{CYCLE_COUNT} Started")

    for symbol in SYMBOLS:

        ticker = exchange.fetch_ticker(symbol)
        bid = ticker["bid"]
        ask = ticker["ask"]

        spread = ask - bid
        spread_pct = (spread / bid) * 100 if bid else 0

        print(f"{symbol} | Bid: {bid} | Ask: {ask}")
        print(f"Spread: {spread:.4f} USD ({spread_pct:.4f}%)\n")

        log_message(f"{symbol} | Bid={bid}, Ask={ask}, Spread={spread_pct:.6f}%")

        # =====================================================
        # 🚨 ARBITRAGE ALERT
        # =====================================================
        if spread_pct >= THRESHOLD_PCT:

            alert_text = (
                f"🚨🚨🚨  ARBITRAGE OPPORTUNITY DETECTED!  🚨🚨🚨\n"
                f"BUY at {bid}   →   SELL at {ask}\n"
                f"Profit Potential: {spread_pct:.4f}%\n"
            )

            print(alert_text)
            log_message("⚡ ARBITRAGE DETECTED → " + alert_text.replace("\n", " | "))

            # Built-in Windows alert (no external file)
            winsound.Beep(1200, 300)
            winsound.Beep(1500, 300)

        else:
            print("→ No significant arbitrage opportunity.\n")
            log_message(f"No opportunity for {symbol} (Spread={spread_pct:.6f}%)")

    time.sleep(WAIT_SECONDS)

log_message("=== Arbitrage Session Ended ===")
print("\n✨ Analysis Completed.")
