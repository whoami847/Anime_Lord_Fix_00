from config import FORCE_SUB_CHANNEL

async def force_subscription_check(message):
    user = message.from_user.id
    # Assuming we use a check method (this can be an API call to check if the user is subscribed)
    is_subscribed = check_subscription(user, FORCE_SUB_CHANNEL)
    
    if not is_subscribed:
        await message.reply(f"You need to subscribe to {FORCE_SUB_CHANNEL} to use this bot.")
        return False
    return True

def check_subscription(user_id, channel):
    # Placeholder function to simulate subscription check
    # Replace with actual API or method to check if user is subscribed to a channel
    return True  # For demonstration purposes, we return True
