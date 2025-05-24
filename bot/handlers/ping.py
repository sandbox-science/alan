import time


async def on_ping(match, bot, start):
    """
    If the user typed "!ping", reply with "pong {latency in ms}".
    """
    if match.command("ping"):
        end     = time.monotonic_ns()
        latency = (end - start) / 1000000
        await bot.api.send_text_message(
            match.room.room_id,
            f"pong 🏓 {latency:.2f} ms"
        )