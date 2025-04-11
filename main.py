from pyrogram import Client, filters
from config import API_TOKEN, API_ID, API_HASH, WELCOME_MESSAGE, ADMIN_IDS, FORCE_SUB_CHANNEL

# Client সেটআপ
app = Client(
    "anime_lord_bot",
    api_id=API_ID,  # API_ID যোগ করা হয়েছে
    api_hash=API_HASH,  # API_HASH যোগ করা হয়েছে
    bot_token=API_TOKEN  # Bot Token যোগ করা হয়েছে
)

# /start কমান্ড হ্যান্ডলার
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(WELCOME_MESSAGE)

# বট চালানো
app.run()
