import ccxt
import time
import random
import logging
import requests
import os
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Load from .env file
load_dotenv()

# Fetch credentials securely
api_key = os.getenv('BITGET_API_KEY')
password = os.getenv('BITGET_API_PASSPHRASE')
pem_file_path = os.getenv('BITGET_PEM_FILE_PATH')  # Path to .pem file

# Load RSA private key from .pem file
def load_rsa_private_key(pem_file_path):
    try:
        with open(pem_file_path, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,  # Assume unencrypted; adjust if encrypted
                backend=default_backend()
            )
        # Convert to PEM format as bytes for CCXT
        pem_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
        return pem_key
    except Exception as e:
        raise ValueError(f"Failed to load RSA private key from {pem_file_path}: {e}")

# Load the RSA private key
rsa_private_key = load_rsa_private_key(pem_file_path)

symbol = 'PAWS/USDT'  # Target trading pair
base_amount = 10      # Base amount in USDT per round (e.g., $10 per trade)
max_volume = 505      # Stop after this total volume (USDT)

# === SETUP LOGGER ===
logging.basicConfig(filename='trade_log.txt', level=logging.INFO)

# === SETUP BITGET (via CCXT) ===
exchange = ccxt.bitget({
    'apiKey': api_key,
    'rsaPrivateKey': rsa_private_key,  # Use RSA private key instead of secret
    'password': password,  # Passphrase, if required by Bitget
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot',
    }
})

# === TELEGRAM ALERT ===
def send_telegram(message):
    try:
        telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
        telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
        url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
        payload = {
            'chat_id': telegram_chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

# === LOGGING ===
def log_trade(msg):
    logging.info(f"{time.ctime()} - {msg}")

# === MARKET ORDER TRADING ===
def place_order():
    global total_volume
    try:
        ticker = exchange.fetch_ticker(symbol)
        market_price = ticker['last']

        # Random USD amount between 9–11
        usd_amount = round(random.uniform(base_amount - 1, base_amount + 1), 2)
        amount = round(usd_amount / market_price, 6)

        # Market Buy
        buy_order = exchange.create_market_buy_order(symbol, amount)
        msg_buy = f"MARKET BUY: {amount} PAWS at ~${market_price} (≈ ${usd_amount})"
        print(msg_buy)
        log_trade(msg_buy)
        send_telegram(msg_buy)

        total_volume += usd_amount

        time.sleep(random.uniform(1.5, 3.5))

        # Market Sell
        sell_order = exchange.create_market_sell_order(symbol, amount)
        msg_sell = f"MARKET SELL: {amount} PAWS at ~${market_price}"
        print(msg_sell)
        log_trade(msg_sell)
        send_telegram(msg_sell)

    except Exception as e:
        error_msg = f"Trade error: {e}"
        print(error_msg)
        log_trade(error_msg)
        send_telegram(error_msg)

# === MAIN LOOP ===
total_volume = 0
while total_volume < max_volume:
    place_order()
    delay = random.uniform(10, 20)  # Adjust delay between trades
    time.sleep(delay)

# Final message
final_msg = f"✅ Done trading. Total volume: ${round(total_volume, 2)}"
print(final_msg)
send_telegram(final_msg)
log_trade(final_msg)