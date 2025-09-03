from pyrogram import Client, filters

API_ID = "26255490"
API_HASH = "0fc813f29ca3e1ce96f448106e0618db"
BOT_TOKEN = "8278588474:AAHSXK7Pkie3sNxqA-75CEWm66k82keQ-8M"

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
