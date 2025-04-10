import time
from threading import Timer

async def auto_delete_handler(client, message):
    delete_time = 20 * 60  # 20 minutes in seconds
    Timer(delete_time, delete_message, [message]).start()

def delete_message(message):
    try:
        message.delete()
    except Exception as e:
        print(f"Failed to delete message: {e}")
