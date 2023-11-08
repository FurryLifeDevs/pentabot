import logging

import discord
from discord.ext import commands

import wavelink

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
        print(f'We have logged in as {self.user} | {self.user.id}')
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

    async def setup_hook(self) -> None:
        # Wavelink 2.0 has made connecting Nodes easier... Simply create each Node
        # and pass it to NodePool.connect with the client/bot.
        node1: wavelink.Node = wavelink.Node(uri='lava1.horizxon.tech:443', password='horizxon.tech', secure=True, retries=3)
        node2: wavelink.Node = wavelink.Node(uri='lava2.horizxon.tech:443', password='horizxon.tech', secure=True, retries=3)
        node3: wavelink.Node = wavelink.Node(uri='lava3.horizxon.tech:443', password='horizxon.tech', secure=True, retries=3)
        node4: wavelink.Node = wavelink.Node(uri='suki.nathan.to:443', password='adowbongmanacc', secure=True, retries=3)
        node5: wavelink.Node = wavelink.Node(uri='oce-lavalink.lexnet.cc:443', password='lexn3tl@val!nk', secure=True, retries=3)
        node6: wavelink.Node = wavelink.Node(uri='lavalink.ordinaryender.my.eu.org:443', password='ordinarylavalink', secure=True, retries=3)
        node7: wavelink.Node = wavelink.Node(uri='lavalink.justapie.net:443', password='pieajust12@XyZ', secure=True, retries=3)
        await wavelink.NodePool.connect(client=self, nodes=[node7])


if __name__ == "__main__":
    bot = Pentabot()
    bot.run(TOKEN, log_handler=Pentabot.handler, log_level=logging.DEBUG)
