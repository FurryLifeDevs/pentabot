import os

import discord
from discord.ext import tasks, commands

from music import download_audio, search, string2link


class VoiceCommands(commands.Cog):
    def __init__(self):
        # self.bot = bot
        self.is_playing = False
        self.paused = False
        # self.is_playing = False
        self.channel = None
        self.vc = None

    @commands.command()
    async def join(self, ctx: commands.Context):
        if not ctx.author.voice:
            await ctx.reply("пожалуйста, зайдите на канал!", mention_author=False)
            return
        self.channel = ctx.author.voice.channel
        self.vc = await self.channel.connect(self_deaf=True)

    @commands.command()
    async def leave(self, ctx: commands.Context):
        if self.channel is not None:
            await self.vc.disconnect()
            self.channel = None
            await ctx.reply(f"я отключился от голосового канала!", mention_author=False)

    @commands.command()
    async def play(self, ctx: commands.Context, link: str = None):
        if link is None:
            await ctx.reply("пожалуйста, укажите ссылку или название!", mention_author=False)
            return
        if "http" not in link:
            link = await string2link(link)
        if ctx.author.voice.channel != self.channel:
            await self.join(ctx)
        video_title = None
        file_name = f"data/{ctx.guild.id}/{hash(link)}.m4a"
        if not os.path.isfile(file_name):
            video_title = download_audio(link, ctx.guild.id)
        if self.is_playing:
            self.vc.stop()
            self.is_playing = False
        self.vc.play(discord.FFmpegPCMAudio(file_name))
        self.is_playing = True
        await ctx.reply(f'Сейчас играет: "{video_title}"', mention_author=False)

    @commands.command()
    async def search(self, ctx: commands.Context, *args):
        name = ' '.join(args)
        search_result = search(name, 5)
        msg = '\n'.join(f"Название: {video['title']}\nСсылка: {'https://www.youtube.com' + video['url_suffix']}" for video in search_result)
        await ctx.reply(msg, mention_author=False)

    @commands.command()
    async def pause(self, ctx: commands.Context):
        if not self.paused:
            self.vc.pause()
            self.paused = True

    @commands.command()
    async def resume(self, ctx: commands.Context):
        if self.paused:
            self.vc.resume()
            self.paused = False

