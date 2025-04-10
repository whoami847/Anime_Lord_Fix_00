from config import HELP_MESSAGE, ABOUT_MESSAGE

async def start_handler(client, message):
    await message.reply("Welcome to Anime Lord Bot!\n\n" + HELP_MESSAGE)

async def help_handler(client, message):
    await message.reply(HELP_MESSAGE)

async def about_handler(client, message):
    await message.reply(ABOUT_MESSAGE)
