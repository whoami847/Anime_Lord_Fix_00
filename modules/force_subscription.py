from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def force_subscription_check(client, message):
    user_id = message.from_user.id
    try:
        member = await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        if member.status in ("member", "administrator", "creator"):
            return True
    except Exception:
        pass
    await message.reply(
        f"⚠️ **Subscription Required**\n\nPlease join {FORCE_SUB_CHANNEL} to use this bot!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Join Channel", url=f"https://t.me/{FORCE_SUB_CHANNEL}")]
        ])
    )
    return False
