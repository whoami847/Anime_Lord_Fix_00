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
    in_memory=True  # Koyeb-এর জন্য গুরুত্বপূর্ণ
)

@app.on_message(filters.command("start"))
async def start(client, message):
    logger.info(f"Received /start from {message.from_user.id}")
    await message.reply("✅ বট সচল রয়েছে!")

if __name__ == "__main__":
    logger.info("বট শুরু হচ্ছে...")
    app.run()
    logger.info("বট বন্ধ হচ্ছে")
