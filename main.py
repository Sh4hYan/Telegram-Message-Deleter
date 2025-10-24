from telethon import TelegramClient
import asyncio
from config import API_ID, API_HASH, TARGET_CHANNEL

client = TelegramClient("YOUR_SESSION", API_ID, API_HASH)

async def main():
    await client.start()
    print("Logged in done...")

    channel = await client.get_entity(TARGET_CHANNEL)
    count = 0
    msgs = []

    async for msg in client.iter_messages(channel):
        msgs.append(msg.id)
        if len(msgs) >= 100:
            await client.delete_messages(channel, msgs)
            count += len(msgs)
            msgs = []
            await asyncio.sleep(0.2)

    if msgs:
        await client.delete_messages(channel, msgs)
        count += len(msgs)

    print(f"✅ Successfully deleted ({count} Message)")

asyncio.run(main())
