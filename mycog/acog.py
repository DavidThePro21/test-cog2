import discord
from discord.ext import commands

class Mycog:
    """A fuck messenger"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """Sends a fuck message"""

        #Your code will go here
        await self.bot.say("FUCK YOU.")

def setup(bot):
    bot.add_cog(Mycog(bot))
