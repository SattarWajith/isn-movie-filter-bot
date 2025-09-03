async def on_message(client, message):
    if message.text and message.text.lower().startswith("/broadcast "):
        text = message.text[11:]
        success = 0
        fail = 0
        # Example: iterate users from DB
        # for user_id in get_all_users():
        #     try:
        #         await client.send_message(user_id, text)
        #         success += 1
        #     except Exception: fail += 1
        await message.reply_text(f"Broadcast completed!\nSuccess: {success}\nFail: {fail}")