import os

from matrix.bot import Bot
from config.config import load_config

from bot.handlers.echo import echo
from bot.handlers.react import react
from bot.handlers.weather import weather
from bot.handlers.greeting import welcome_handler, greeting
from bot.handlers.ping import ping

from logging import critical

COMMANDS = {
    "ping": ping,
    "echo": echo,
    "greet": greeting,
    "react": react,
    "weather": weather,
    "welcome": welcome_handler,
}


class Alan:
    def __init__(self):
        cfg = load_config()

        self.username = cfg["USERNAME"]
        self.password = cfg["PASSWORD"]
        self.bot = Bot(username=self.username, password=self.password)

    def register_command(self, bot, name, handler):
        @bot.command(name)
        async def _wrapper(ctx):
            await handler(ctx)

    def setup_handlers(self):
        """
        Setup the bot handlers for different events.
        """
        for name, func in COMMANDS.items():
            self.register_command(self.bot, name, func)

    def start(self):
        """
        Entry point for the bot.
        """
        if not os.path.exists("config/config.yaml"):
            critical("config/config.yaml file not found. Please create one.")
            return

        self.setup_handlers()
        self.bot.start()
