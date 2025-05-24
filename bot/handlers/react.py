from simplematrixbotlib import MessageMatch


async def on_react(room, event, bot):
    """
    React to a message with a wave emoji if the user types "hello".
    """
    match = MessageMatch(room, event, bot)
    if match.is_not_from_this_bot() and match.command("hello"):
        await bot.api.send_reaction(
            room.room_id,
            event.event_id,
            key="👋"
        )
