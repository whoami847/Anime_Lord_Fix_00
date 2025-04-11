import asyncio

async def auto_delete_handler(client, message):
    await asyncio.sleep(1200)  # 20 মিনিট অপেক্ষা করুন
    await message.delete()
