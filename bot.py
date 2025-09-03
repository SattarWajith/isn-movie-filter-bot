from pyrogram import Client, filters

API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

app = Client("movie_filter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Example movie database (replace with MongoDB or SQLite in production)
movies = {
    "Inception": "https://t.me/yourchannel/123",
    "Interstellar": "https://t.me/yourchannel/456"
}

@app.on_message(filters.text & filters.group)
async def movie_filter(client, message):
    query = message.text.strip()
    if query in movies:
        await message.reply_text(f"Found: {query}\nLink: {movies[query]}")
    else:
        await message.reply_text("Movie not found.")

app.run()