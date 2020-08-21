from discord.ext import commands
import asyncio
import threading
import os
import discord


bot = commands.Bot(command_prefix="!")
TOKEN = None
CHANNEL = None
MENTION= None

class DBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def setBot(tk):
    global TOKEN
    TOKEN = tk
    
def setPrefix(pref):
    global bot
    bot =  commands.Bot(command_prefix=pref)

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
    global MENTION
    CHANNEL = ctx.channel
    print(ctx.channel)
    MENTION = ctx.message.author.mention
    print(MENTION)
    await ctx.send("channel has been set to " + ctx.channel.name + " for user " + MENTION)

def runDiscordBot():
    loop = asyncio.get_event_loop()
    loop.create_task(_start())

    thread = threading.Thread(target=_run_it_forever, args=(loop,))
    thread.start()



def sendText(txt):
    loop = asyncio.get_event_loop()
    loop.create_task(CHANNEL.send(MENTION+" " + txt))

def sendEmbed(content, title, description, fields, color):
    embed=discord.Embed(title=str(title), color=color, description=description)
    for k,v in fields.items():
        embed.add_field(name=k, value = v, inline=False);
    loop = asyncio.get_event_loop()
    loop.create_task(CHANNEL.send(content = content, embed=embed))

