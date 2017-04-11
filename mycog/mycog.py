import discord
from discord.ext import commands

class Mycog:
    """Will say hi."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """Says hi."""

        #Your code will go here
        await self.bot.say("Hi.")

def setup(bot):
    bot.add_cog(Mycog(bot))
