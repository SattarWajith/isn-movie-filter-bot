from config import FEATURES

async def on_message(client, message):
    if message.text and FEATURES.get("welcome_message", False):
        if message.text.lower() == "/start":
            await message.reply_text("👋 Welcome to Movie Filter Bot!")