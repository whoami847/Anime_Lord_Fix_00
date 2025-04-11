from dotenv import load_dotenv
import os

load_dotenv()

# Telegram API ID and API Hash (required for Client API)
API_ID = int(os.getenv("API_ID"))  # Load from .env file
API_HASH = os.getenv("API_HASH")  # Load from .env file

# Telegram Bot API Token
API_TOKEN = os.getenv("API_TOKEN")  # Load from .env file

if not API_TOKEN:
    raise ValueError("API_TOKEN is not set in environment variables")

# Other configurations
ADMIN_IDS = [7282066033]  # Replace with your admin IDs
FORCE_SUB_CHANNEL = "@just_test_only_0"  # Replace with your channel

WELCOME_MESSAGE = "Welcome to Anime Lord Bot! Please subscribe to the channel and try again."
HELP_MESSAGE = "Here is how you can use the bot:\n/start - Start the bot\n/help - Help message\n/about - About the bot"
ABOUT_MESSAGE = "Anime Lord Bot is designed to share anime-related content easily. Created by YourName."
FILE_STORAGE_PATH = "/path/to/storage"  # Path to store files
