import os

# Telegram Bot API Token
API_TOKEN = os.getenv("API_TOKEN")

# Admin User IDs (can be a list of admin IDs)
ADMIN_IDS = [123456789]  # Replace with your admin IDs

# Force Subscription Channel (optional)
FORCE_SUB_CHANNEL = "@your_channel"  # Replace with your channel

# Bot settings
WELCOME_MESSAGE = "Welcome to Anime Lord Bot! Please subscribe to the channel and try again."
HELP_MESSAGE = "Here is how you can use the bot:\n/start - Start the bot\n/help - Help message\n/about - About the bot"
ABOUT_MESSAGE = "Anime Lord Bot is designed to share anime-related content easily. Created by YourName."

# File and Link settings
FILE_STORAGE_PATH = "/path/to/storage"  # Path to store files
