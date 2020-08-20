from discord.ext import commands
import asyncio
import threading

global channel

class DBot:
    
    
    bot = commands.Bot(command_prefix="!")
    token = None
    
    def __init__(self, tk):
        self.token = tk
    
    async def _start(self):
        await self.bot.start(self.token)
        
    def _run_it_forever(self,loop):
        loop.run_forever()
    
    
    @bot.event
    async def on_ready():
        print("Discord bot connected")
    
    @bot.command()
    async def isConnected(ctx):
        await ctx.send("YES I AM")
        
    @bot.command()
    async def here(ctx):
        global channel
        channel = ctx.channel
        print(channel)
        await ctx.send("channel has been set to " + channel.name)
    
    def runDiscordBot(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self._start())
        
        thread = threading.Thread(target=self._run_it_forever, args=(loop,))
        thread.start()
            
            
            
    async def sendText(self, txt):
        print(DiscordBot.channel)
        await DiscordBot.channel.send(content=txt)

    