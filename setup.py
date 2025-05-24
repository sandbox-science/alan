import time
import os

from simplematrixbotlib import Bot, Creds, MessageMatch
from config import load_config
from handlers import echo, ping, greeting, react
from nio import RoomMemberEvent


def setup_bot():
    cfg   = load_config()
    creds = Creds(cfg["CLIENT"], cfg["USERNAME"], cfg["PASSWORD"])

    return Bot(creds), cfg["PREFIX"]

def setup_handlers(bot, prefix):
    """
    Setup the bot handlers for different events.
    """
    @bot.listener.on_message_event
    async def _on_message(room, event):
        latency_start = time.monotonic()
        match         = MessageMatch(room, event, bot, prefix)
        if match.is_not_from_this_bot() and match.prefix():
            await ping.on_ping(match, bot, latency_start)
            await echo.on_echo(match, bot)
            await greeting.on_greeting(match, bot)
        else:
            await react.on_react(room, event, bot)

    @bot.listener.on_custom_event(RoomMemberEvent)
    async def _on_member(room, event):
        if event.membership == "join" and \
           event.source.get("unsigned", {}).get("prev_content", {}).get("membership") != "join":
            await greeting.on_join(event, room, bot)

def main():
    """
    Entry point for the bot.
    """
    # Check if the config.yaml file exists
    if not os.path.exists('config.yaml'):
        print("config.yaml file not found. Please create one.")
        return

    os.system('pip3 install -r requirements.txt') # Install dependencies

    # Load the configuration and create the bot instance
    bot, prefix = setup_bot()
    setup_handlers(bot, prefix)

    bot.run()

if __name__ == "__main__":
    main()
