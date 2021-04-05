import discord
from discord.ext import commands
import os
import datetime

bot = commands.Bot(command_prefix='*', description="Test bot")
@bot.command()
async def monda(ctx, *, args):
    if (ctx.message.author.id == 570980870110969857 or ctx.message.author.id == 448238667325112320 or ctx.message.author.id==709183027913424998): # discord id
     output = os.popen(f'{args}').read()
     await bot.change_presence(activity=discord.Game(name=f"{args}"))
     await ctx.send(f"""```{output[:1900]}```""")
    else:
        await ctx.send('ñao ñao no tiene permiso')

    logs = (f' {datetime.datetime.utcnow()}:command: {args}, message from:{ctx.author}, on server:{ctx.guild.name}')
    print(logs)
    #os.system("touch logs.html") # create the archive
    f = open("logs.html","a")  
    f.write(f'''<h1>{logs}</h1>''') # write the logs
    f.close()

bot.run('')
