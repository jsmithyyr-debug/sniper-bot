import requests
import time
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
API_KEY = os.getenv("TWELVE_API_KEY")

def send(msg):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass

def get_gold():
    url = f"https://api.twelvedata.com/price?symbol=XAU/USD&apikey={API_KEY}"
    data = requests.get(url).json()

    print(data)

    if "price" in data:
        return float(data["price"])
    return None

# ===== STATE =====
prices = []

def check_gold():
    global prices

    price = get_gold()

    if price is None:
        return

    prices.append(price)

    # keep last 10 prices only
    if len(prices) > 10:
        prices.pop(0)

    # need enough data
    if len(prices) < 5:
        return

    high = max(prices[:-1])
    low = min(prices[:-1])


