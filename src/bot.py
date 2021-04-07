
import subprocess
import datetime

import time
import os

import flask
import discord

from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

token = ""
if os.getenv("TOKEN"):
    token = os.getenv("TOKEN")
else:
    raise Exception("no value found")

bot = commands.Bot(command_prefix='*', description="Test bot")
admins = [570980870110969857, 448238667325112320, 709183027913424998]


@bot.command()
async def monda(ctx, *, args) -> None:
    if (ctx.message.author.id in admins):  # if the id from the user is on the admins list
        pipe = ""
        cmd = subprocess.popen(f"{args}",  stdout=pipe, shell=True)
        time.sleep(1)
        cmd.kill()
        await bot.change_presence(activity=discord.Game(name=f"{args}"))
        await ctx.send(f"""```{pipe.read()[:1900]}```""")
    else:
        # if the user is not in the admins list they cant do nothing and only returns this
        await ctx.send('ñao ñao no tiene permiso')

    logs = (f' {datetime.datetime.utcnow()}:command: {args}, message from:{ctx.author}, on server:{ctx.guild.name}')
    print(logs)

    # os.system("touch logs.html") # create the archive
    f = open("logs.html", "a")
    f.write(f'''<h1>{logs}</h1>''')  # write the logs
    f.close()

bot.run(token)
