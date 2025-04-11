import os
from threading import Thread
from flask import Flask
from pyrogram import Client, filters
from config import API_ID, API_HASH, API_TOKEN

# Flask App (Keep-Alive)
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    flask_app.run(host='0.0.0.0', port=8080)

# Pyrogram Bot
app = Client(
    "anime_lord_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=API_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello from Anime Lord Bot!")

if __name__ == "__main__":
    # Start Flask in a separate thread
    Thread(target=run_flask, daemon=True).start()
    
    print("Bot started!")
    app.run()
