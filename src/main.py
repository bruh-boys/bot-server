
from subprocess import Popen, PIPE
from threading import Thread
from time import sleep
from re import search
import os
import datetime
# emoji chill chill
from discord.ext import commands
from requests import get
from flask import Flask, render_template
import discord

# COÑO YOINS PON AQUI ABAJO EL PUTO TOKEN
token: str = ""
# AQUI SOLO DEBES DE PONER EL ID DE LOS ADMINS
admins: list = [570980870110969857, 448238667325112320, 709183027913424998,467030554131562506]

# ESTO NO LO MUEVAS NI POR TUS HUEVOS
bot = commands.Bot(command_prefix='*', description="Test bot")
app = Flask(__name__)


# ESTO LO UNICO QUE HACE ES ESCRIBIR LOS LOGS
def write_logs(ctx, args) -> None:
    logs: str = (
        f'date: {datetime.datetime.utcnow()}\\ncommand: {args}\\nmessage from: {ctx.author}\\nserver: {ctx.guild.name}\\n')
    print(f'{"=="*32}\n{logs}{"=="*32}'.replace("\\n", "\n"))

    # os.system("touch logs.html") # create the archive

    logs_file: open = open("templates/logs.html", "a")
    logs_file.write(f"<h2>{logs}</h2>")
    logs_file.close()  # write the logs

# ESTO OBTIENE NGROK CON REGEX


def get_ngrok() -> str:

    ngrok_body = get("http://127.0.0.1:4040/api/tunnels")
    print(ngrok_body.json())

    return search("https://+[A-Za-z0-9]+.ngrok.io", ngrok_body.content)

# ESTO EJECUTA NGROK


def finish_and_take_ngrok() -> None:
    while True:
        cmd: Popen = Popen(
            "ngrok http 5000", stdout=PIPE, shell=True)
        sleep(7200)
        cmd.terminate()

# es el main , que crees?


def main():

    server: Thread = Thread(target=app.run, args=("0.0.0.0", 5000))
    ngrok = Thread(target=finish_and_take_ngrok)
    ngrok.start()
    server.start()
    bot.run(token)




# esto maneja los comandos que le envies


@bot.command(name="monda")
async def monda(ctx, *, args) -> None:
    global admins
    if (ctx.message.author.id in admins):  # if the id from the user is on the admins list
        # pipe:subprocess
        cmd: Popen = Popen(f"{args}",  stdout=PIPE, shell=True)
        sleep(4)  # wait 4 seconds
        cmd.terminate()  # finish the process
        await bot.change_presence(activity=discord.Game(name=f"{args}"))

        # send you the message

        await ctx.send(f"```" + cmd.stdout.read().decode('utf-8')[:1800] + "```")
    else:
        # if the user is not in the admins list they cant do nothing and only returns this
        await ctx.send('ñao ñao no tiene permiso')
    write_logs(ctx, args)

# esto SESUPONE que deberia de enviarte el link a ngrok


@bot.command(name="ngrok")
async def ngrok(ctx) -> None:
    global admins

    await ctx.send(get_ngrok())

# solo te envia los logs


@app.route("/")
def send_logs():

    return render_template("logs.html").replace("\\n", "<br>")


# esto solo ejecuta el main
if __name__ == "__main__":
    main()
