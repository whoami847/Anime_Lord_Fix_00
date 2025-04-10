# Anime Lord Bot

Anime Lord Bot is a Telegram bot for anime-related content sharing. You can use it to generate links, share files, and more.

## Setup Instructions

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `config.py` file and add your Bot API token, admin IDs, and other configurations.
4. Run the bot: `python main.py`
5. Optionally, deploy on a platform like Heroku.

## Features

- `/start`: Start the bot and check for force subscription
- `/help`: Get help on how to use the bot
- `/about`: Learn more about the bot
- `/genlink`: Generate a file link
- `/batch`: Generate multiple file links at once

## Admin Commands

- `/forcesub`: Manage force subscription channels
- `/auto_del`: Enable automatic deletion of messages
- `/restart`: Restart the bot
- `/broadcast`: Send a broadcast message to all users
- `/button-c`: Create custom buttons
