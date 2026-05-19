<<<<<<< HEAD
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL = os.getenv("CHANNEL")
DISCUSSION_GROUP = os.getenv("DISCUSSION_GROUP")

RULES_TEXT = """📌 Discussion Rules:

1. No spam or suspicious links.
2. No insults.
3. Stay on-topic.
4. Violations will result in comment deletion or ban.
"""

bot = TelegramClient("adoperatorrules_bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(chats=CHANNEL))
async def on_new_channel_post(event):
    if not event.message or event.message.grouped_id:
        return

    post_id = event.message.id

    try:
        await bot.send_message(
            entity=DISCUSSION_GROUP,
            message=RULES_TEXT,
            comment_to=post_id,
            link_preview=False,
        )
        print(f"Rules comment added under post {post_id}")

    except Exception as e:
        print(f"Failed to comment under post {post_id}: {e}")


print("Bot is running...")
=======
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL = os.getenv("CHANNEL")
DISCUSSION_GROUP = os.getenv("DISCUSSION_GROUP")

RULES_TEXT = """📌 Discussion Rules:

1. No spam or suspicious links.
2. No insults.
3. Stay on-topic.
4. Violations will result in comment deletion or ban.
"""

bot = TelegramClient("adoperatorrules_bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(chats=CHANNEL))
async def on_new_channel_post(event):
    if not event.message or event.message.grouped_id:
        return

    post_id = event.message.id

    try:
        await bot.send_message(
            entity=DISCUSSION_GROUP,
            message=RULES_TEXT,
            comment_to=post_id,
            link_preview=False,
        )
        print(f"Rules comment added under post {post_id}")

    except Exception as e:
        print(f"Failed to comment under post {post_id}: {e}")


print("Bot is running...")
>>>>>>> cc13a39a2d8e67dbc5ed9bd8d141050a8fabd21a
bot.run_until_disconnected()