import discord
from discord.ext import commands

class Spammy:
    """SPAM!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def spam(self):
        """SPAM!"""

        #Your code will go here
        await self.bot.say("Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! Spam! ")

def setup(bot):
    bot.add_cog(Spammy(bot))
