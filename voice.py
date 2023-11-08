from discord.ext import commands
import wavelink


class VoiceCommands(commands.Cog):
    def __init__(self):
        pass

    @commands.command()
    async def play(self, ctx: commands.Context, search: str) -> None:
        """Simple play command."""

        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        tracks = await wavelink.YouTubeTrack.search(search)
        if not tracks:
            await ctx.reply(f'По запросу: `{search}` треков не найдено ;(', mention_author=False)
            return

        track = tracks[0]
        await vc.play(track)
        await ctx.reply(f"Сейчас играет: {track}", mention_author=False)

    @commands.command()
    async def disconnect(self, ctx: commands.Context) -> None:
        """Simple disconnect command.

        This command assumes there is a currently connected Player.
        """
        vc: wavelink.Player = ctx.voice_client
        await vc.disconnect()
