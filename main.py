import os
from pyrogram import Client, filters
from flask import Flask
from threading import Thread
from config import API_ID, API_HASH, API_TOKEN

# Initialize Flask app
flask_app = Flask(__name__)

@flask_app.route('/')
def health_check():
    return "OK", 200

# Initialize Pyrogram Client
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=API_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Bot is working!")

def run_flask():
    flask_app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    # Start Flask in a daemon thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    print("Starting Telegram Bot...")
    app.run()
