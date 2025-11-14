🌙 Crypto Arbitrage Analyzer – A real-time cryptocurrency spread tracker with automatic alerts and logging.

📌 Overview
This project analyzes live bid–ask spreads of selected cryptocurrency pairs using the Binance API via CCXT. When a profitable spread above the defined threshold is detected, the system prints a visual alert, plays a Windows alarm sound, logs the event with a timestamp, and repeats checks in configurable cycles.
This project demonstrates my ability to rapidly learn Python, use real APIs, process live financial data, build functional automation tools, and document/publish code professionally.

🚀 Features
• Real-time price tracking (via ccxt)
• Supports multiple crypto pairs
• Adjustable profit threshold
• Audible arbitrage alert (Windows beep)
• Timestamped logging
• Cycle-based scanning: 20 checks → rest → repeat
• Clean, modular structure
• Fully documented and open-source

🛠 Technology Stack
Python 3.x – Main programming language
ccxt – Crypto exchange API wrapper
winsound – Windows-native alert sounds
Binance – Price data source
Logging – Output saved to arbitrage_log.txt

📂 Project Structure
crypto-arbitrage-analyzer/
├── arbitrage_scanner.py (main analyzer)
├── arbitrage_log.txt (auto-generated log file)
├── README.md (project documentation)
└── .gitignore (optional)

⚙️ How It Works
Each scan cycle:

Fetches bid and ask prices

Calculates absolute spread and spread percentage

Compares spread with a defined threshold

If exceeded:
– Displays alert
– Plays Windows beep
– Logs a detailed entry
Script checks every 5 seconds and pauses 10 seconds after every 20 cycles.

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

Install dependency: pip install ccxt

Run the program: python arbitrage_scanner.py
Windows will play an alert sound when a profitable opportunity is detected.

📝 Log File Example
[2025-02-15 18:42:23] ETH/USDT | Spread: 0.0100 USD (0.0003%) | Bid: 3097.64 | Ask: 3097.65

📌 Notes
This project is for learning and demonstration.
Highlights: analytical thinking, automation logic, real-time data processing, and professional documentation.
Not intended for real trading without further development.

✨ Author
Hilayda Çiftci
Material & R&D Engineer | Python Learner | Data Automation Enthusiast
GitHub: https://github.com/hlydacftc



