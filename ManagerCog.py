from discord.ext import commands


class ManagerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def here(self,ctx):
        if self.bot.MENTION is None:
            self.bot.CHANNEL = ctx.channel
            print(ctx.channel)
            self.bot.MENTION = ctx.message.author.mention
            print(self.bot.MENTION)
            await ctx.send("channel has been set to " + ctx.channel.name + " for user " + self.bot.MENTION)
        elif self.bot.MENTION == ctx.author.mention:
            self.bot.CHANNEL = ctx.channel
            await ctx.send("channel has been changed to " + ctx.channel.name + ". User won't be changed and is " + self.bot.MENTION)

