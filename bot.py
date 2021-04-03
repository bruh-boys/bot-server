import discord
from discord.ext import commands
import os
import subprocess

bot = commands.Bot(command_prefix='*', description="Test bot")
# Event
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Game(name="monda"))
   print("\033[4;35m"+"bot on")


@bot.command()
async def uno(ctx,arg):
    output = os.popen(f'{arg}').read()
    await ctx.send(f"""
        ```
        {output[:1800]}
        ```
                   """)

@bot.command()
async def dos(ctx,arg,arg2):
    output2 = os.popen(f'{arg} {arg2}').read()
    await ctx.send(f"""
        ```
        {output2[:1800]}
        ```
                   """)

@bot.command()
async def tres(ctx,arg,arg2,arg3):
    output3 = os.popen(f'{arg} {arg2} {arg3}').read()
    await ctx.send(f"""
        ```
        {output3[:1800]}
        ```
                   """)

@bot.command()
async def cuatro(ctx,arg,arg2,arg3,arg4):
    output4 = os.popen(f'{arg} {arg2} {arg3} {arg4}').read()
    await ctx.send(f"""
        ```
        {output4[:1800]}
        ```
                   """)

@bot.command()
async def cinco(ctx,arg,arg2,arg3,arg4,arg5):
    output5 = os.popen(f'{arg} {arg2} {arg3} {arg4} {arg5}').read()
    await ctx.send(f"""
        ```
        {output5[:1800]}
        ```
                   """)

bot.run('')
