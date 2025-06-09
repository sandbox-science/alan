from matrix.bot import Context


async def echo(ctx: Context):
    """
    If the user typed "!echo", reply with the same message.
    """
    get_event = getattr(ctx.event, "body", "")
    find_message = get_event.find(" ")
    message = get_event[find_message + 1:]

    await ctx.send(message)
