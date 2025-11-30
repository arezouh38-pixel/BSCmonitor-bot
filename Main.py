from web3 import Web3
import asyncio
import json

# --- تنظیمات شما ---
# آدرس WSS (WebSocket) خود را از QuickNode اینجا قرار دهید 
WSS_URL = 'wss://intensive-greatest-glade.bsc.quiknode.pro/6ad479ba7a8dc4cad7f58e5f832179d178defaac'
# --------------------

# اتصال به شبکه BSC از طریق WebSocket
try:
    w3 = Web3(Web3.WebsocketProvider(WSS_URL))
    if w3.is_connected():
        print("✅ اتصال موفقیت‌آمیز به بایننس اسمارت چین (BSC)")
    else:
        print("❌ خطا در اتصال به نود QuickNode.")
except Exception as e:
    print(f"❌ خطای اتصال: {e}")

# تابعی که هر بار یک تراکنش جدید در ممپول پیدا شود، اجرا می‌شود
async def handle_transaction(tx_hash_hex):
    print("-" * 50)
    print(f"🔍 تراکنش جدید در ممپول مشاهده شد (Hash): {tx_hash_hex}")
    
    try:
        tx = w3.eth.get_transaction(tx_hash_hex)
        if tx:
            print(f" فرستنده (From): {tx['from']}")
            print(f" گیرنده (To):   {tx['to']}")
            value_bnb = w3.from_wei(tx['value'], 'ether')
            print(f" مقدار (Value): {value_bnb} BNB")
            # print(f" داده ورودی (Data): {tx['input']}")

            # *** محل اضافه کردن فیلترهای شما ***
            # if tx['to'] == "0x...آدرس قرارداد شما...":
            #     print("!!! 🚨 هشدار: تراکنش مربوط به قرارداد ما پیدا شد 🚨 !!!")

    except Exception as e:
        print(f"❌ خطا در دریافت جزئیات تراکنش: {e}")

# تابع اصلی برای راه‌اندازی ربات
async def main():
    global w3 # این خط مشکل NameError را حل می‌کند
    w3.eth.subscribe('newPendingTransactions', handle_transaction)
    print("👂 ربات در حال گوش دادن به ممپول BSC است... منتظر تراکنش‌های در حال انتظار باشید.")
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
