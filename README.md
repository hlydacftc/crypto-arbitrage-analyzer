# 🌙 Crypto Arbitrage Analyzer  
*A real-time cryptocurrency spread tracker with automatic alerts and logging.*

## 📌 Overview  
This project analyzes **live bid–ask spreads** of selected cryptocurrency pairs using the **Binance API via ccxt**.  
If a profitable arbitrage-like spread is detected above a defined threshold, the system:

- ⚠️ Prints a visual alert  
- 🔔 Plays an alarm sound (Windows)  
- 📝 Saves the event to a log file with timestamp  
- 🔄 Repeats checks in cycles with configurable intervals  

This project demonstrates my ability to:
- Learn Python quickly  
- Use real APIs  
- Process live financial data  
- Build functional automation tools  
- Document and publish code professionally  

---

## 🚀 Features  
- ✔ Real-time price tracking (via `ccxt`)  
- ✔ Supports multiple crypto pairs  
- ✔ Customizable profit threshold  
- ✔ Audible arbitrage alarm  
- ✔ Automatic timestamped logging  
- ✔ Cycle-based operation (20 checks → rest → repeat)  
- ✔ Clean, readable code  
- ✔ Fully documented and open-source  

---

## 🛠 Technology Stack  
| Component | Description |
|----------|-------------|
| **Python 3.x** | Main programming language |
| **ccxt** | Crypto exchange API wrapper |
| **winsound** | Windows alarm notifications |
| **Binance** | Price data source |
| **Logging** | Events saved to `arbitrage_log.txt` |

---

## 📂 Project Structure  
crypto-arbitrage-analyzer/
│
├── arbitrage_scanner.py # Main program file (real-time analyzer)
├── arbitrage_log.txt # Automatically generated log file
├── README.md # Project documentation
└── .gitignore # Ignored files (optional)


---

## ⚙️ How It Works  
At each cycle, the script:

1. Fetches **bid** and **ask** prices for each symbol  
2. Calculates:  
   - Absolute spread  
   - Spread percentage  
3. Compares % spread with your threshold  
4. If profitable:  
   - Displays warning  
   - Plays alarm (`winsound.Beep`)  
   - Logs detailed entry to file  

The process repeats every 5 seconds  
→ and every 20 checks, the system rests 10 seconds and resumes.

---

## 📈 Example Output  

🌙 CYCLE 1/20

BTC/USDT | Bid: 94809.71 | Ask: 94809.72
Spread: 0.0100 USD (0.0000%)
→ No significant arbitrage opportunity.

ETH/USDT | Bid: 3097.64 | Ask: 3097.65
Spread: 0.0100 USD (0.0003%)

🚨🚨 ARBITRAGE OPPORTUNITY DETECTED! 🚨🚨
⭐ PROFITABLE SPREAD FOUND ⭐


---

## 🔧 Configuration  
You can adjust all parameters at the top of the script:

```python
SYMBOLS = ["BTC/USDT", "ETH/USDT"]
SPREAD_THRESHOLD = 0.0003        # % threshold
CYCLE_COUNT = 20
SLEEP_BETWEEN_CHECKS = 5
REST_AFTER_CYCLE = 10
LOG_FILE = "arbitrage_log.txt"

▶️ How to Run

Install the required library: pip install ccxt

Run the script: python arbitrage_loop.py

Windows will play a sound when a profitable spread is detected.

📝 Log File Example (auto-generated)

[2025-02-15 18:42:23] ETH/USDT | Spread: 0.0100 USD (0.0003%) | Bid: 3097.64 | Ask: 3097.65

📌 Notes

This is a learning + demonstration project.

Designed to show analytical thinking, automation skills, and fast Python learning ability.

Not intended for live trading without further development.
✨ Author

Hilayda Çiftci
Material & R&D Engineer | Python Learner | Data Automation Enthusiast
GitHub: https://github.com/hlydacftc


---

