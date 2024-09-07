import discord
from discord.ext import commands, tasks
from discord import Embed
import os
from dotenv import load_dotenv

# Importer les classes
from function.help import Help

# Charger les variables d'environnement
load_dotenv()

# Créer une instance des Classes
help_handler = Help()

#Vérification si autorisation serveurs et joueurs:
AUTHORIZED_SERVER_ACCESS = os.getenv('SERVER_ACCESS')
AUTHORIZED_SUPERSERVER_ACCESS = os.getenv('SUPER_SERVER_ACCESS')
AUTHORIZED_USER_ID = os.getenv('ADMIN_USER')
AUTHORIZED_SUPERUSER_ID = os.getenv('SUPERADMIN_USER')

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def help(self,ctx,type:str=None):
        authorId = ctx.author.id
        serverId = ctx.guild.id
        str = help_handler.getUserCommands(self,authorId,serverId)
        if not isinstance(type, str):
                type = ""
        # Charger l'image pour l'embed principal
        file_main = discord.File('./image/banniere.png', filename="banniere.png")
        # Charger l'image pour la miniature
        file_thumbnail = discord.File('./image/blason.png', filename="blason.png")
        if type.upper() in ('USER', 'USERS', 'UTILISATEUR', 'UTILISATEURS'):
            embed = Embed(title="Liste des Commandes ", description="Voici les commandes utilisateurs disponibles pour vous :", color=0x00ff00)
            embed.add_field(name="**Utilisateurs**", value=str, inline=False)
        else:
            embed = Embed(title="Liste des Commandes", description="Voici les commandes disponibles pour vous :", color=0x00ff00)
            embed.add_field(name="**Utilisateurs**", value=str, inline=False)
        embed.set_image(url="attachment://banniere.png")
        embed.set_thumbnail(url="attachment://blason.png")
        await ctx.send(embed=embed,files=[file_main, file_thumbnail])

async def setup(bot):
    await bot.add_cog(Help(bot))