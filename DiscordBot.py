from discord.ext import commands
import asyncio
import threading
import os
import discord


bot = commands.Bot(command_prefix="!")
TOKEN = None
CHANNEL = None

def setToken(tk):
    global TOKEN
    TOKEN = tk

async def _start():
    await bot.start(TOKEN)

def _run_it_forever(loop):
    loop.run_forever()


@bot.event
async def on_ready():
    print("Discord bot connected")

@bot.command()
async def isConnected(ctx):
    await ctx.send("YES I AM")

@bot.command()
async def here(ctx):
    global CHANNEL
    CHANNEL = ctx.channel
    print(ctx.channel)
    await ctx.send("channel has been set to " + ctx.channel.name)

def runDiscordBot():
    loop = asyncio.get_event_loop()
    loop.create_task(_start())

    thread = threading.Thread(target=_run_it_forever, args=(loop,))
    thread.start()



def sendText( txt ):
    print(txt)
    print(CHANNEL)
    loop = asyncio.get_event_loop()
    loop.create_task(CHANNEL.send(txt))
    

