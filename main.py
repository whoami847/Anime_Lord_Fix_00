from pyrogram import Client, filters
from config import API_TOKEN, ADMIN_IDS, FORCE_SUB_CHANNEL, HELP_MESSAGE, ABOUT_MESSAGE
from modules.user_commands import start_handler, help_handler, about_handler
from modules.admin_commands import restart_handler, broadcast_handler
from modules.force_subscription import force_subscription_check
from modules.file_sharing import file_link_handler
from modules.auto_delete import auto_delete_handler
from modules.button_manager import button_manager

app = Client("anime_lord_bot", bot_token=API_TOKEN)

# Force Subscription check
@app.on_message(filters.command("start"))
async def start(client, message):
    if await force_subscription_check(message):
        await start_handler(client, message)
    else:
        await message.reply(WELCOME_MESSAGE)

# Other command handlers
@app.on_message(filters.command("help"))
async def help(client, message):
    await help_handler(client, message)

@app.on_message(filters.command("about"))
async def about(client, message):
    await about_handler(client, message)

@app.on_message(filters.command("restart") & filters.user(ADMIN_IDS))
async def restart(client, message):
    await restart_handler(client, message)

@app.on_message(filters.command("broadcast") & filters.user(ADMIN_IDS))
async def broadcast(client, message):
    await broadcast_handler(client, message)

# File sharing handler
@app.on_message(filters.command("genlink"))
async def genlink(client, message):
    await file_link_handler(client, message)

# Auto-delete handler
@app.on_message(filters.command("auto_del"))
async def auto_del(client, message):
    await auto_delete_handler(client, message)

# Button management handler
@app.on_message(filters.command("button-c") & filters.user(ADMIN_IDS))
async def button(client, message):
    await button_manager(client, message)

app.run()
