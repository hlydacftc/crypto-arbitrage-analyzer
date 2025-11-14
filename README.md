# 🌙 Crypto Arbitrage Analyzer  
*A real-time cryptocurrency spread tracker with automatic alerts and logging.*

---

## 📌 Overview  
This project analyzes **live bid–ask spreads** of selected cryptocurrency pairs using the **Binance API via CCXT**.  
When a profitable spread above the defined threshold is detected, the system:

- ⚠️ Prints a visual alert  
- 🔔 Plays an alarm sound (Windows)  
- 📝 Logs the event with a timestamp  
- 🔄 Repeats checks in configurable cycles  

This project demonstrates my ability to:
- Rapidly learn Python  
- Use real APIs  
- Process live financial data  
- Build functional automation tools  
- Professionally document and publish code  

---

## 🚀 Features  
- ✔ Real-time price tracking (via `ccxt`)  
- ✔ Supports multiple crypto pairs  
- ✔ Adjustable profit threshold  
- ✔ Audible arbitrage alert (Windows beep)  
- ✔ Timestamped logging  
- ✔ Cycle-based scanning: 20 checks → rest → repeat  
- ✔ Clean, modular structure  
- ✔ Fully documented and open-source  

---

## 🛠 Technology Stack  
| Component      | Description                       |
|----------------|-----------------------------------|
| **Python 3.x** | Main programming language         |
| **ccxt**       | Crypto exchange API wrapper       |
| **winsound**   | Windows-native alert sounds       |
| **Binance**    | Price data source                 |
| **Logging**    | Output saved to `arbitrage_log.txt` |

---

## 📂 Project Structure  
```text
crypto-arbitrage-analyzer/
│
├── arbitrage_scanner.py      # Main real-time analyzer
├── arbitrage_log.txt         # Auto-generated log file
├── README.md                 # Project documentation
└── .gitignore                # Optional ignored files



⚙️ How It Works

Each scan cycle performs the following steps:

Fetches bid and ask prices for each symbol

Calculates:

Absolute spread

Spread percentage

Compares the spread to a defined threshold

If the threshold is met or exceeded:

Displays an alert

Plays a Windows beep sound

Logs a detailed entry

The script checks prices every 5 seconds, and after 20 cycles, it pauses for 10 seconds before resuming.



📈 Example Output

🌙 CYCLE 1/20

BTC/USDT | Bid: 94809.71 | Ask: 94809.72
Spread: 0.0100 USD (0.0000%)
→ No significant arbitrage opportunity.

ETH/USDT | Bid: 3097.64 | Ask: 3097.65
Spread: 0.0100 USD (0.0003%)

🚨🚨 ARBITRAGE OPPORTUNITY DETECTED! 🚨🚨
⭐ PROFITABLE SPREAD FOUND ⭐


🔧 Configuration

SYMBOLS = ["BTC/USDT", "ETH/USDT"]
SPREAD_THRESHOLD = 0.0003
CYCLE_COUNT = 20
SLEEP_BETWEEN_CHECKS = 5
REST_AFTER_CYCLE = 10
LOG_FILE = "arbitrage_log.txt"

▶️ How to Run

Install the required package: pip install ccxt
Run the program: python arbitrage_scanner.py
Windows will play an alert sound when a profitable opportunity is found.

📝 Log File Example
[2025-02-15 18:42:23] ETH/USDT | Spread: 0.0100 USD (0.0003%) | Bid: 3097.64 | Ask: 3097.65


📌 Notes

This project is built for learning and demonstration purposes.
It highlights:

Analytical thinking

Real-time automation logic

Financial data processing

Professional documentation

This tool is not intended for live trading without further improvement.

✨ Author

Hilayda Çiftci
Material & R&D Engineer | Python Learner | Data Automation Enthusiast
🔗 GitHub: https://github.com/hlydacftc
---



