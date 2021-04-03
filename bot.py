import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='*', description="Test bot")
# Event

@bot.command()
async def monda(ctx, *, args):
    output = os.popen(f'{args}').read()
    await bot.change_presence(activity=discord.Game(name=f"{args}"))
    await ctx.send(f"""
        ```py
        {output[:1900]}
        ```
                   """)

bot.run('')
