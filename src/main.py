
from subprocess import Popen, PIPE
from threading import Thread
from time import sleep
from re import search
import os
import datetime
# emoji chill
from discord.ext import commands
from requests import get
from flask import Flask, render_template
import discord

# COÑO YOINS PON AQUI ABAJO EL PUTO TOKEN
token: str = "the token"

bot = commands.Bot(command_prefix='*', description="Test bot")
app = Flask(__name__)

admins: list = [570980870110969857, 448238667325112320, 709183027913424998]


def write_logs(ctx, args) -> None:
    logs: str = (
        f'date: {datetime.datetime.utcnow()}\\ncommand: {args}\\nmessage from: {ctx.author}\\nserver: {ctx.guild.name}\\n')
    print(f'{"=="*32}\n{logs}{"=="*32}'.replace("\\n", "\n"))

    # os.system("touch logs.html") # create the archive

    logs_file: open = open("public/logs.html", "a")
    logs_file.write(f"<h2>{logs}</h2>")
    logs_file.close()  # write the logs


def get_ngrok() -> str:
    ngrok_body = get("http://127.0.0.1:4040/api/tunnels").content
    return search("https://*.ngrok.io", ngrok_body)


@bot.command(name="monda")
async def monda(ctx, *, args) -> None:
    global admins
    if (ctx.message.author.id in admins):  # if the id from the user is on the admins list
        # pipe:subprocess
        cmd: Popen = Popen(f"{args}",  stdout=PIPE, shell=True)
        sleep(1)  # wait a second
        cmd.terminate()  # finished the process
        await bot.change_presence(activity=discord.Game(name=f"{args}"))

        # send you the message

        await ctx.send(f"```" + cmd.stdout.read().decode('utf-8')[:1800] + "```")
    else:
        # if the user is not in the admins list they cant do nothing and only returns this
        await ctx.send('ñao ñao no tiene permiso')
    write_logs(ctx, args)


@bot.command(name="ngrok")
async def ngrok(ctx) -> None:
    global admins
    if (ctx.message.author.id in admins):
        try:
            await ctx.author.send(get_ngrok())
        except:
            await ctx.send("no pude enviarte el link")


@app.route("/")
def send_logs():
    f: open = open("public/logs.html", "r")
    html = f.read().replace("\\n", "<br>")
    f.close()
    return html


def main():
    #x = threading.Thread(target=thread_function, args=(1,))

    server: Thread = Thread(target=app.run, args=("0.0.0.0", 5000))
    server.start()

    bot.run(token)

    while True:
        cmd: Popen = Popen(
            "ngrok http 5000", stdout=PIPE, shell=True)
        sleep(7200)
        cmd.terminate()


if __name__ == "__main__":
    main()
