import asyncio
from pyrogram import Client
from config import FEATURES
from bot.config import API_ID, API_HASH, BOT_TOKEN

def load_features():
    import importlib
    loaded = {}
    for feature, enabled in FEATURES.items():
        if enabled:
            try:
                mod = importlib.import_module(f"features.{feature}")
                loaded[feature] = mod
            except ImportError:
                print(f"Feature {feature} module not found!")
    return loaded

app = Client("movie_filter_bot")

features = load_features()

@app.on_message()
async def handle_message(client, message):
    for fname, fmod in features.items():
        if hasattr(fmod, "on_message"):
            await fmod.on_message(client, message)

if __name__ == "__main__":
    app.run()
