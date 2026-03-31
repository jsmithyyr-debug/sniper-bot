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

last_price = None

while True:
    try:
        price = get_gold()

        if price is None:
            time.sleep(60)
            continue

        if last_price:
            if price > last_price:
                send(f"📈 GOLD BUY\nPrice: {price}")
            elif price < last_price:
                send(f"📉 GOLD SELL\nPrice: {price}")

        last_price = price
        time.sleep(60)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(60)

