import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL")
DISCUSSION_GROUP = int(os.getenv("DISCUSSION_GROUP"))

RULES_TEXT = """📌 Discussion Rules:

1. No spam or suspicious links.
2. No insults.
3. Stay on-topic.
4. Violations will result in comment deletion or ban.
"""

bot = TelegramClient("adoperatorrules_bot", API_ID, API_HASH)


@bot.on(events.NewMessage(chats=CHANNEL))
async def on_new_channel_post(event):
    print(f"NEW POST DETECTED: {event.message.id}")

    try:
        await bot.send_message(
            entity=CHANNEL,
            message=RULES_TEXT,
            comment_to=event.message.id,
            link_preview=False
        )

        print("RULES SENT SUCCESSFULLY")

    except Exception as e:
        print(f"ERROR: {repr(e)}")


async def main():
    await bot.start(bot_token=BOT_TOKEN)
    print("Bot is running...")
    await bot.run_until_disconnected()


bot.loop.run_until_complete(main())