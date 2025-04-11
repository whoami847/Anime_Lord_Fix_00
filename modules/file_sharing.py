async def file_link_handler(client, message):
    if message.reply_to_message and message.reply_to_message.document:
        file_id = message.reply_to_message.document.file_id
        file_link = f"https://t.me/{client.me.username}?start=file_{file_id}"
        await message.reply(f"📁 File Link: {file_link}")
    else:
        await message.reply("❌ Please reply to a file with /genlink.")
