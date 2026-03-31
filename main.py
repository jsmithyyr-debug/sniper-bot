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

def check_gold():
    global last_price

    price = get_gold()

    if price is None:
        return

    if last_price:
        move = price - last_price

        # ICC-style filter (only strong moves)
        if abs(move) > 2:

            if move > 0:
                send(f"""
📈 GOLD BUY (ICC)

Price: {price}
Momentum: Strong bullish move
Bias: Continuation
""")

