import time

# 🔥 TEST SIGNAL FUNCTION (replace later with real alerts)
def send_signal(message):
    print(f"SIGNAL: {message}")

# 🔍 YOUR STRATEGY FUNCTION
def check_for_setups():
    print("Checking market...")

    # 👉 TEMP TEST (forces a signal every loop)
    send_signal("TEST BUY | SL: 10 | TP: 40")

    # 🚫 REMOVE ABOVE LATER
    # Replace with your ICC logic like:
    # if condition:
    #     send_signal("REAL TRADE")

# 🚀 START BOT
print("🚀 BOT STARTED")

# 🔁 MAIN LOOP (THIS IS WHAT YOU WERE MISSING)
while True:
    try:
        check_for_setups()
        time.sleep(10)  # runs every 10 seconds (change to 60 later)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
