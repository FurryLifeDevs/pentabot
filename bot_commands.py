import discord
from discord.ext import commands

import datetime
import random as rd


class CustomCommands(commands.Cog):
    def __init__(self):
        # self.bot = bot
        pass

    @commands.command()
    async def about(self, ctx: commands.Context):
        description = f"* <@607950706971770921> — основной разработчик\n### [Исходный код Octobot](" \
                      f"https://github.com/LabsDevelopment/Octobot)"
        embed = discord.Embed(title="Разработчик:", color=discord.Color.blue(), description=description)
        embed.set_author(name="Об Octobot", icon_url=ctx.bot.user.avatar)
        embed.set_image(url="https://mctaylors.ddns.net/cdn/octobot-banner.png")
        await ctx.reply(embed=embed, mention_author=False)
        await ctx.message.delete()

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="Нгьес!", color=discord.Color.green(),
                              description=f"{round(ctx.bot.latency * 1000)}мс")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f"{ctx.bot.user.name}#{ctx.bot.user.discriminator}", icon_url=ctx.bot.user.avatar)
        await ctx.reply(embed=embed, mention_author=False)
        await ctx.message.delete()

    @commands.command()
    async def random(self, ctx, first: int, second: int = None):
        defaulted = ""
        if second is None:
            defaulted = " (по умолчанию)"
            second = 0
        if first > second:
            first, second = second, first
        value = rd.randint(first, second)
        embed = discord.Embed(color=discord.Color.dark_blue(),
                              description=f"# {value}\n" + f"* Минимальное число: `{first}`{defaulted}\n" + f"* Максимальное число: `{second}`")
        embed.set_author(name=f"Случайное число для @{ctx.author.name}:", icon_url=ctx.author.avatar)
        await ctx.reply(embed=embed, mention_author=False)
        await ctx.message.delete()

    @commands.command()
    async def timestamp(self, ctx):
        _time = int(ctx.message.created_at.timestamp())

        description = f"""# {_time}
        * `<t:{_time}:d>` → <t:{_time}:d>
        * `<t:{_time}:D>` → <t:{_time}:D>
        * `<t:{_time}:t>` → <t:{_time}:t>
        * `<t:{_time}:T>` → <t:{_time}:T>
        * `<t:{_time}:f>` → <t:{_time}:f>
        * `<t:{_time}:F>` → <t:{_time}:F>
        * `<t:{_time}:R>` → <t:{_time}:R>
        """
        embed = discord.Embed(color=discord.Color.dark_blue(), description=description)
        embed.set_author(name=f"Временная метка для @{ctx.author.name}:", icon_url=ctx.author.avatar)
        await ctx.reply(embed=embed, mention_author=False)
        await ctx.message.delete()

    @commands.command()
    async def userinfo(self, ctx: commands.Context, target: discord.Member = None):
        roles = ""
        if target is None:
            target = ctx.author
        if len(target.roles) > 1:
            list_roles = target.roles.copy()
            list_roles.pop(0)
            print(list_roles)
            roles += "\n* Роли\n"
            roles += ', '.join([str(role.mention) for role in list_roles])
        name = f"* Отображаемое имя\n`{target.display_name}`" if target.name != target.display_name else ""
        description = f"""### <@{target.id}>
        {name}
        * Вступил в Discord\n<t:{int(target.created_at.timestamp())}:f>
        * Вступил на сервер\n<t:{int(target.joined_at.timestamp())}:f>{roles}
        """
        embed = discord.Embed(color=discord.Color.blue(), description=description)
        embed.set_author(name=f"Информация о @{target.name}", icon_url=ctx.bot.user.avatar)
        embed.set_thumbnail(url=target.avatar)
        embed.set_footer(text=f"ID: {target.id}")
        await ctx.reply(embed=embed, mention_author=False)
        await ctx.message.delete()

    @commands.command()
    async def guildinfo(self, ctx: commands.Context):
        description = f"""## {ctx.guild.name}
        * Описание сервера\n`{ctx.guild.description}`
        * Дата создания\n<t:{int(ctx.guild.created_at.timestamp())}:f>
        * Владелец сервера\n<@{ctx.guild.owner_id}>\n### Буст сервера
        * Уровень буста: `{ctx.guild.premium_tier}`
        * Количество бустов: `{ctx.guild.premium_subscription_count}`
        """
        embed = discord.Embed(color=discord.Color.pink(), description=description)
        embed.set_author(name=f"Информация о {ctx.guild.name}", icon_url=ctx.bot.user.avatar)
        embed.set_thumbnail(url=ctx.guild.icon)
        embed.set_footer(text=f"ID: {ctx.guild.id}")
        await ctx.reply(embed=embed, mention_author=False)
        await ctx.message.delete()

    # @commands.command()
    # async def remind(self, ctx: commands.Context, time: int = None, text: str = None):
    #     if time is None or text is None:
    #         await ctx.reply("Пожалуйста, укажите время и текст напоминания!", mention_author=False)
    #         return
    #     description = f"* Текст напоминания: `{text}`\n* Время отправки напоминания: <t:{int(ctx.message.created_at.timestamp() + time)}:f>"
    #     first_embed = discord.Embed(color=discord.Color.green(), description=description)
    #     first_embed.set_author(name=f"Напоминание для @{ctx.author.name} создано")
    #     await ctx.reply(embed=first_embed, mention_author=False)
    #     await asyncio.sleep(time)
    #     second_embed = discord.Embed(color=discord.Color.pink(), description=f"Вы просили напомнить вам `{text}`")
    #     second_embed.set_author(name=f"Напоминание для @{ctx.author.name}", icon_url=ctx.author.avatar)
    #     await ctx.send(ctx.author.mention, embed=second_embed)
    #     await ctx.message.delete()
