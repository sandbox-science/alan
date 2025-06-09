from bot.utils import embed_md
from matrix.bot import Context


async def greeting(ctx: Context):
    """
    If the user typed "!greet", reply with "Hello, World!".
    """
    embed = embed_md.make_embed(
        description="Hello, World! 😊",
    )
    await ctx.send(embed)


async def welcome_handler(ctx: Context):
    """
    If the user joined the room, reply with "Welcome!".
    """
    user = ctx.event.source.get("state_key")
    index = user.find(":", 1)

    text = f"👋 Welcome @{user[1:index]}! Good to have you here!"
    embed = embed_md.make_embed(
        title="Welcome!",
        description=text,
    )
    if ctx.event.content.get("membership") == "join":
        print(f"User {user} joined the room.")
        await ctx.send(embed)
