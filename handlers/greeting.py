async def on_greeting(match, bot):
    """
    If the user typed "!greet", reply with "Hello, World!".
    """
    if match.command("greet"):
        await bot.api.send_text_message(
            match.room.room_id,
            "Hello, World!"
        )

async def on_join(event, room, bot):
    """
    If the user joined the room, reply with "Welcome!".
    """
    user     = event.source.get("state_key")
    index = user.find(":", 1)
    
    text = f"👋 Welcome @{user[1:index]}! Feel free to introduce yourself."
    if event.content.get("membership") == "join":
        print(f"User {user} joined the room.")
        await bot.api.send_text_message(
            room.room_id,
            text
        )