import logging

import discord
from discord.ext import commands

from admin import AdminCommands
from config import TOKEN
from bot_commands import CustomCommands
from voice import VoiceCommands


class Pentabot(commands.Bot):
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self) -> None:
        print(f'We have logged in as {bot.user}')
        await self.add_cog(CustomCommands())
        print(f'The CustomCommands cog has been initialized')
        await self.add_cog(VoiceCommands())
        print(f'The VoiceCommands cog has been initialized')
        await self.add_cog(AdminCommands())
        print(f'The AdminCommands cog has been initialized')

    async def on_message(self, message):
        if message.author.bot:
            return
        # do some extra stuff here

        await self.process_commands(message)


if __name__ == "__main__":
    bot = Pentabot()
    bot.run(TOKEN, log_handler=Pentabot.handler, log_level=logging.DEBUG)
