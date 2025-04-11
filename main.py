from pyrogram import Client, filters
from flask import Flask
from threading import Thread
from config import API_ID, API_HASH, API_TOKEN

# Flask App for Health Check
flask_app = Flask(__name__)

@flask_app.route('/')
def health_check():
    return "OK", 200

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
    await message.reply("Bot is running!")

if __name__ == "__main__":
    # Start Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    print("Starting Telegram Bot...")
    app.run()
