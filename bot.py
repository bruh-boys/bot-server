import discord
from discord.ext import commands
import os
import subprocess

bot = commands.Bot(command_prefix='*', description="Test bot")
# Event
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Game(name="servidor desde venezula"))
   print("\033[4;35m"+"bot on")

@bot.command()
async def monda(ctx, *, args):
    output = os.popen(f'{args}').read()
    await ctx.send(f"""
        ```
        {output[:1800]}
        ```
                   """)

bot.run('')
