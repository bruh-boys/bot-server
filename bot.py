import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='*', description="Test bot")
# Event
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Game(name="monda"))
   print("\033[4;35m"+"bot on")


@bot.command()
async def uno(ctx,arg):
    os.system(f"{arg}")
    await ctx.send(f"{arg} commands execute")

@bot.command()
async def dos(ctx,arg,arg2):
    os.system(f"{arg} {arg2}")
    await ctx.send(f"{arg} {arg2} commands execute")

@bot.command()
async def tres(ctx,arg,arg2,arg3):
    os.system(f"{arg} {arg2} {arg3}")
    await ctx.send(f"{arg} {arg2} {arg3} commands execute")

@bot.command()
async def cuatro(ctx,arg,arg2,arg3,arg4):
    os.system(f"{arg} {arg2} {arg3} {arg4}")
    await ctx.send(f"{arg} {arg2} {arg3} {arg4} commands execute")

@bot.command()
async def cinco(ctx,arg,arg2,arg3,arg4,arg5):
    os.system(f"{arg} {arg2} {arg3} {arg4} {arg5}")
    await ctx.send(f"{arg} {arg2} {arg3} {arg4} {arg5} commands execute")

bot.run('')
