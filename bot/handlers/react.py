from matrix.bot import Context


async def react(ctx: Context):
    """
    React to a message with a wave emoji if the user types "hello".
    """
    # TODO: update this when matrix.py has send_reaction() implemented
    await ctx.send("👋")
