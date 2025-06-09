from matrix.bot import Context


async def ping(ctx: Context):
    """
    Reply if the user typed "!ping"
    """
    print(f"{ctx.sender} invoked {ctx.body} in room {ctx.room_name}.")

    await ctx.send("Pong!")
