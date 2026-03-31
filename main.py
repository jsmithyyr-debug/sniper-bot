import requests
import time
import os

# ===== ENV =====
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TWELVE_KEY = os.getenv("TWELVE_API_KEY")

# ===== TELEGRAM =====
def send(msg):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass

# ===== DATA =====
def get_gold():
    url = f"https://api.twelvedata.com/price?symbol=XAU/USD&apikey={TWELVE_KEY}"
    data = requests.get(url).json()
    return float(data["price"])

# ===== STATE =====
last_gold = None

# ===== LOGIC =====
def check_gold():
    global last_gold
    price = get_gold()

    if last_gold:
        if price > last_gold:
            entry = price
            sl = entry - 5
            tp = entry + (entry - sl) * 4

            send(f"""📈 GOLD BUY

Entry: {entry}
SL: {sl}
TP: {tp}
""")

        elif price < last_gold:
            entry = price
            sl = entry + 5
            tp = entry - (sl - entry) * 4

            send(f"""📉 GOLD SELL

Entry: {entry}
SL: {sl}
TP: {tp}
""")

    last_gold = price

# ===== LOOP =====
while True:
    check_gold()
    time.sleep(60)
