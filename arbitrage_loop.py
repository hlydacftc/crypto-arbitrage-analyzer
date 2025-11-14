import ccxt
import time
import winsound
from datetime import datetime

# ============================================================
# 🌙 SYSTEM PARAMETERS
# ============================================================

# NOTE:
# The threshold value (0.0003%) is intentionally set *extremely low*.
# Reason:
#     This project is designed as an educational/demo arbitrage scanner.
#     A very small threshold ensures:
#         - frequent "opportunity" detections,
#         - real-time validation of alert + logging system,
#         - continuous testing even in calm markets.
#
# IMPORTANT (Real-World Trading):
#     Actual arbitrage requires a much higher threshold
#     because of trading fees, slippage, transfer delays,
#     and execution risks.
#
# This note demonstrates awareness of real arbitrage limitations
# and explains why a tiny threshold is chosen for project/testing purposes.
threshold_pct = 0.0003   # 0.0003%

cycle_count = 20          # 20 loops
wait_seconds = 5          # wait 5 seconds between cycles
symbols = ["BTC/USDT", "ETH/USDT"]

log_file = "arbitrage_log.txt"


# ============================================================
# 🌙 LOGGING FUNCTION
# ============================================================
def log_message(message):
    """Writes a timestamped message to the log file."""
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}]  {message}\n")


# ============================================================
# 🌙 MAIN EXECUTION
# ============================================================
exchange = ccxt.binance()

print("\n======================================================================")
print("                    🌙  LIVE ARBITRAGE ANALYSIS  🌙                    ")
print("======================================================================\n")

log_message("=== Arbitrage Session Started ===")

for cycle in range(1, cycle_count + 1):

    print(f"\n🌙 CYCLE {cycle}/{cycle_count}\n")
    log_message(f"Cycle {cycle}/{cycle_count} Started")

    for symbol in symbols:
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
        if spread_pct >= threshold_pct:

            alert_text = (
                f"🚨🚨🚨  ARBITRAGE OPPORTUNITY DETECTED!  🚨🚨🚨\n"
                f"BUY at {bid}   →   SELL at {ask}\n"
                f"Profit Potential: {spread_pct:.4f}%\n"
            )

            print(alert_text)
            log_message("⚡ ARBITRAGE DETECTED → " + alert_text.replace("\n", " | "))

            # Simple sound alert (no external file needed)
            winsound.Beep(1200, 300)
            winsound.Beep(1500, 300)

        else:
            print("→ No significant arbitrage opportunity.\n")
            log_message(f"No opportunity for {symbol} (Spread={spread_pct:.6f}%)")

    time.sleep(wait_seconds)

log_message("=== Arbitrage Session Ended ===")
print("\n✨ Analysis Completed.")



