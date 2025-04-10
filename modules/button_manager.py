from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def button_manager(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Help", callback_data="help_button")],
        [InlineKeyboardButton("About", callback_data="about_button")]
    ])
    await message.reply("Here are your buttons:", reply_markup=keyboard)
