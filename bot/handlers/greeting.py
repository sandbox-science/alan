from bot.utils import embed_md


async def on_greeting(match, bot):
    """
    If the user typed "!greet", reply with "Hello, World!".
    """
    if match.command("greet"):
        embed = embed_md.make_embed(
            description="Hello, World! 😊",
        )
        await bot.api.send_text_message(
            match.room.room_id,
            embed
        )

async def on_join(event, room, bot):
    """
    If the user joined the room, reply with "Welcome!".
    """
    user     = event.source.get("state_key")
    index = user.find(":", 1)
    
    text = f"👋 Welcome @{user[1:index]}! Good to have you here!"
    embed = embed_md.make_embed(
        title="Welcome!",
        description=text,
    )
    if event.content.get("membership") == "join":
        print(f"User {user} joined the room.")
        await bot.api.send_text_message(
            room.room_id,
            embed
        )