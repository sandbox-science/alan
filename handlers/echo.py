async def on_echo(match, bot):
    """
    If the user typed "!echo", reply with the same message.
    """
    if match.command("echo"):
        await bot.api.send_text_message(
            match.room.room_id,
            " ".join(match.args())
        )
