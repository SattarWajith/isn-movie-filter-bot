from database.mongodb import get_mongo

async def on_message(client, message):
    if message.text and message.text.lower() == "/stats":
        db = get_mongo()
        user_count = db.users.count_documents({})
        movie_count = db.movies.count_documents({})
        await message.reply_text(f"Bot users: {user_count}\nMovies stored: {movie_count}")