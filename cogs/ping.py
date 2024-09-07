import discord
from discord.ext import commands, tasks

class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send('Pong!')

async def setup(bot):
    await bot.add_cog(Ping(bot))