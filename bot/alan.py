import os

from matrix.bot import Bot
from config.config import load_config

from bot.handlers.echo import echo
from bot.handlers.react import react
from bot.handlers.weather import weather
from bot.handlers.greeting import welcome_handler, greeting
from bot.handlers.ping import ping


COMMANDS = {
    "ping": ping,
    "echo": echo,
    "greet": greeting,
    "react": react,
    "weather": weather,
    "welcome": welcome_handler,
}


def setup_bot():
    cfg = load_config()
    username = cfg["USERNAME"]
    password = cfg["PASSWORD"]

    return Bot(username=username, password=password)


def setup_handlers(bot):
    """
    Setup the bot handlers for different events.
    """
    for name, func in COMMANDS.items():
        register_command(bot, name, func)


def register_command(bot, name, handler):
    @bot.command(name)
    async def _wrapper(ctx):
        await handler(ctx)


def start():
    """
    Entry point for the bot.
    """
    # Check if the config.yaml file exists
    if not os.path.exists("config/config.yaml"):
        print("config.yaml file not found. Please create one.")
        return

    # Load the configuration and create the bot instance
    bot = setup_bot()
    setup_handlers(bot)

    bot.start()


start()
