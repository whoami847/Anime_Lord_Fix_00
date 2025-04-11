import os
import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, API_TOKEN

# লগিং সেটআপ
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
    workers=2
)

@app.on_message(filters.command("start"))
async def start(client, message):
    logger.info(f"New user: {message.from_user.id}")
    await message.reply("🚀 বট সফলভাবে কাজ করছে!")

if __name__ == "__main__":
    logger.info("বট শুরু হচ্ছে...")
    app.run()
