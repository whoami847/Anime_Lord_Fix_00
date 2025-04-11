import os
import logging
import time
from pyrogram import Client, filters
from config import API_ID, API_HASH, API_TOKEN

# লগিং কনফিগার করুন
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=API_TOKEN,
    workers=4,
    sleep_threshold=30,  # সময় সিঙ্ক্রোনাইজেশনের জন্য গুরুত্বপূর্ণ
    max_concurrent_transmissions=2,
    retries=5,
    in_memory=True  # Koyeb-এর জন্য জরুরি
)

@app.on_message(filters.command("start"))
async def start(client, message):
    logger.info(f"New user: {message.from_user.id}")
    await message.reply("✅ বট সফলভাবে কাজ করছে!")

if __name__ == "__main__":
    logger.info("বট শুরু হচ্ছে...")
    
    # সময় সিঙ্ক্রোনাইজেশন নিশ্চিত করুন
    time.sleep(10)
    
    app.run()
