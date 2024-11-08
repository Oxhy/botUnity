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
    async def help(self,ctx,command_type:str=None):
        authorId = ctx.author.id
        serverId = ctx.guild.id
        if str(serverId) in AUTHORIZED_SUPERSERVER_ACCESS:
            UserCommands = help_handler.getUserCommands(self,authorId,serverId)
            BankCommands = help_handler.getBankCommands(self,authorId,serverId)
            TransactionCommands = help_handler.getTransactionCommands(self,authorId,serverId)
            RessourceUpCommands = help_handler.getRessourceUpCommands(self,authorId,serverId)
            AvancementCommands = help_handler.getAvancementCommands(self,authorId,serverId)
            if not isinstance(command_type, str):
                    command_type = ""
            # Charger l'image pour l'embed principal
            file_main = discord.File('./image/banniere.png', filename="banniere.png")
            # Charger l'image pour la miniature
            file_thumbnail = discord.File('./image/logo_Prometheus.png', filename="logo_Prometheus.png")
            if command_type.upper() in ('USER', 'USERS', 'UTILISATEUR', 'UTILISATEURS'):
                embed = Embed(title="Liste des Commandes ", description="Voici les commandes utilisateurs disponibles pour vous :", color=0x00ff00)
                embed.add_field(name="**Utilisateurs**", value=UserCommands, inline=False)
            elif command_type.upper() in ('BANK','BANKS','BANQUE','BANQUES'):
                embed = Embed(title="Liste des Commandes ", description="Voici les commandes banque disponibles pour vous :", color=0x00ff00)
                embed.add_field(name="**Banque**", value=BankCommands, inline=False)
            elif command_type.upper() in ('TRANSACTION','TRANSACTIONS','TRANS','TRANSAC'):
                embed = Embed(title="Liste des Commandes ", description="Voici les commandes transactions disponibles pour vous :", color=0x00ff00)
                embed.add_field(name="**Transaction**", value=TransactionCommands, inline=False)
            elif command_type.upper() in ('RESSOURCEUP','RESSOURCE_UP'):
                embed = Embed(title="Liste des Commandes ", description="Voici les commandes ressource pour up disponibles pour vous :", color=0x00ff00)
                embed.add_field(name="**Ressources nécessaire**", value=RessourceUpCommands, inline=False)
            elif command_type.upper() in ('AVANCEMENT','AVANCEMENTS'):
                embed = Embed(title="Liste des Commandes ", description="Voici les commandes avancement disponibles pour vous :", color=0x00ff00)
                embed.add_field(name="**Avancement**", value=AvancementCommands, inline=False)
            else:
                embed = Embed(title="Liste des Commandes", description="Voici les commandes disponibles pour vous :", color=0x00ff00)
                embed.add_field(name="**Utilisateurs**", value=UserCommands, inline=False)
                embed.add_field(name="**Banque**", value=BankCommands, inline=False)
                embed.add_field(name="**Transaction**", value=BankCommands, inline=False)
                embed.add_field(name="**Ressources nécessaires**", value=RessourceUpCommands, inline=False)
                embed.add_field(name="**Avancement**", value=AvancementCommands, inline=False)
            embed.set_image(url="attachment://banniere.png")
            embed.set_thumbnail(url="attachment://logo_Prometheus.png")
            await ctx.send(embed=embed,files=[file_main, file_thumbnail])
        else:
            # Charger l'image pour l'embed principal
            file_main = discord.File('./image/banniere.png', filename="banniere.png")
            # Charger l'image pour la miniature
            file_thumbnail = discord.File('./image/logo_Prometheus.png', filename="logo_Prometheus.png")
            embed.set_image(url="attachment://banniere.png")
            embed.set_thumbnail(url="attachment://logo_Prometheus.png")
            embed.add_field(name="Commandes",value='Aucune commande', inline=False)
            await ctx.send(embed=embed,files=[file_main,file_thumbnail])

async def setup(bot):
    await bot.add_cog(Help(bot))