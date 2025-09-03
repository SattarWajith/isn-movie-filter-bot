from database.mongodb import get_mongo

async def on_message(client, message):
    if message.text:
        db = get_mongo()
        movie = db.movies.find_one({"title": message.text.strip()})
        if movie:
            await message.reply_text(f"Found: {movie['title']}\nLink: {movie['link']}")