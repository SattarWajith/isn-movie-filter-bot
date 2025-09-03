import logging

logger = logging.getLogger("movie_filter_bot")

async def on_message(client, message):
    logger.info(f"Message from {message.from_user.id}: {message.text}")