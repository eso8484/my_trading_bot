
# 🦾 Bitget Market Order Trading Bot

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue?logo=docker)](https://www.docker.com/)
[![Bitget API](https://img.shields.io/badge/Exchange-Bitget-orange)](https://www.bitget.com/)
[![Telegram Notifications](https://img.shields.io/badge/Telegram-Enabled-blue?logo=telegram)](https://core.telegram.org/bots)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Automated Python trading bot for Bitget using **market orders**. Useful for reaching spot trading milestones, sending Telegram trade alerts, and running securely inside Docker.

---

## ⚙️ Features

- ✅ Market buy and sell orders for instant execution
- 📈 Target any trading pair (e.g., `PAWS/USDT`)
- 🧠 Randomized order size and time delays
- 🔔 Telegram alerts for each trade
- 📁 Logs all trades to `trade_log.txt`
- 🐳 Run easily using Docker

---

## 📦 Requirements

- Python 3.8+
- Bitget API key, secret, and passphrase
- Telegram Bot token & chat ID
- Docker (optional, but recommended)

---

## 🚀 Quick Setup

### 1. Clone the Project

```bash
git clone https://github.com/eso8484/my_trading_bot.git
cd my_trading_bot
```
### 2. Configure API Keys

Open bot.py and update these lines with your actual values:

- api_key = **`'YOUR_BITGET_API_KEY'`**
- secret = **`'YOUR_BITGET_API_SECRET'`**
- password = **`'YOUR_API_PASSPHRASE'`**

- telegram_token = **`'YOUR_TELEGRAM_BOT_TOKEN'`**
- telegram_chat_id = **`'YOUR_TELEGRAM_CHAT_ID'`**

## Methods of Running the Script

### 1. Run Locally (Optional)

```bash
pip install -r requirements.txt
python bot.py
```

### 2. 🐳 Run with Docker (Recommended)

- Step 1: Build the Docker Image

    ```bash
    docker build -t bitget-bot .
    ```
- Step 2: Run the Container

    ```bash
    docker run -d --name my-bitget-bot bitget-bot
    ```
- Step 3: Monitor Logs

    ```bash
    docker logs -f my-bitget-bot
    ```

## File Structure

---
```
my_trading_bot/
│
├── bot.py              # Main trading bot script
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build instructions
├── trade_log.txt       # Trade history log (auto-created)
└── README.md           # This file
```

---
## **🌐 Connect With Me**

[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/oche_21)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/eso8484)
[![Direct Contact](https://img.shields.io/badge/Direct_Contact-%23009688.svg?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/eso8484)
