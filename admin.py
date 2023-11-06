from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self):
        # self.bot = bot
        pass

    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def clear(self, ctx: commands.Context, amount: int = None):
    #     await ctx.message.delete()
    #     if amount is None:
    #         await ctx.channel.purge()
    #     else:
    #         await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx: commands.Context, text: str):
        await ctx.send(text)
        await ctx.message.delete()
