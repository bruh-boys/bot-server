
import subprocess
import datetime

import time
import os

import flask
import discord

from discord.ext import commands



#COÑO YOINS PON AQUI ABAJO EL PUTO TOKEN


token = ""


bot = commands.Bot(command_prefix='*', description="Test bot")
admins = [570980870110969857, 448238667325112320, 709183027913424998]


@bot.command()
async def monda(ctx, *, args) -> None:
    if (ctx.message.author.id in admins):  # if the id from the user is on the admins list
        # pipe:subprocess
        cmd = subprocess.Popen(f"{args}",  stdout=subprocess.PIPE, shell=True)
        time.sleep(1)  # wait a second
        cmd.terminate()  # finished the process
        await bot.change_presence(activity=discord.Game(name=f"{args}"))

        # send you the message
    
        await ctx.send(f"```{cmd.stdout.read().decode('utf-8')[:1800]}```")
    else:
        # if the user is not in the admins list they cant do nothing and only returns this
        await ctx.send('ñao ñao no tiene permiso')

    logs = (f' {datetime.datetime.utcnow()}:command: {args}, message from:{ctx.author}, on server:{ctx.guild.name}')
    print(logs)

    # os.system("touch logs.html") # create the archive

    f = open("logs.html", "a")
    f.write(f'''<h1>{logs}</h1>''')
    f.close()  # write the logs


bot.run(token)
