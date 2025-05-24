import time
from bot.utils import embed_md


async def on_ping(match, bot, start):
    """
    If the user typed "!ping", reply with a markdown‐styled card showing
    the latency in milliseconds.
    """
    if not match.command("ping"):
        return

    # Measure latency in ms
    end        = time.monotonic_ns()
    latency_ms = (end - start) / 1_000_000

    embed = embed_md.make_embed(
        title="🏓 Pong!",
        description="Here’s how fast I’m thinking:",
        field=f"Latency {latency_ms:.2f} ms"
    )
    await bot.api.send_markdown_message(match.room.room_id, embed)
