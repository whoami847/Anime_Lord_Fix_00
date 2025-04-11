import os
from pyrogram import Client, filters
from config import API_ID, API_HASH, API_TOKEN

# Initialize Pyrogram Client
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=API_TOKEN,
    in_memory=True  # Important for Koyeb deployment
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Bot is now working perfectly on Koyeb!")

if __name__ == "__main__":
    print("Starting Telegram Bot...")
    app.run()
