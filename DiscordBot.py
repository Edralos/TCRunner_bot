from discord.ext import commands
import asyncio
import threading
import os
import discord





class DBot(commands.Bot):
    TOKEN = None
    CHANNEL = None
    MENTION= None
    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TOKEN = token


    

    async def _start(self):
        await self.start(self.TOKEN)

    def _run_it_forever(self,loop):
        loop.run_forever()


    
    async def on_ready(self):
        print("Discord bot connected")

    
    async def isConnected(self,ctx):
        await ctx.send("YES I AM")

    
    async def here(self,ctx):
        
        self.CHANNEL = ctx.channel
        print(ctx.channel)
        self.MENTION = ctx.message.author.mention
        print(self.MENTION)
        await ctx.send("channel has been set to " + ctx.channel.name + " for user " + self.MENTION)

    def runDiscordBot(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self._start())
    
        thread = threading.Thread(target=self._run_it_forever, args=(loop,))
        thread.start()



    def sendText(self,txt):
        loop = asyncio.get_event_loop()
        loop.create_task(self.CHANNEL.send(self.MENTION+" " + txt))

    def sendEmbed(self, title, description, fields, color,content=None):
        embed=discord.Embed(title=str(title), color=color, description=description)
        for k,v in fields.items():
            embed.add_field(name=k, value = v, inline=False)
        loop = asyncio.get_event_loop()
        loop.create_task(self.CHANNEL.send(content = content, embed=embed))

