import os
import logging
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
    workdir="/tmp"  # Koyeb-এর জন্য বিশেষ সেটিং
)

@app.on_message(filters.command("start"))
async def start(client, message):
    logger.info(f"{message.from_user.id} থেকে /start কমান্ড পাওয়া গেছে")
    await message.reply("🎉 বট সফলভাবে কাজ করছে!")

if __name__ == "__main__":
    logger.info("বট চালু করা হচ্ছে...")
    app.run()
    logger.info("বট বন্ধ করা হয়েছে")
