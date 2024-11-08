import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv

# Importer les classes
from function.transaction import Transaction
from utils import response_discord,transformer_ressources

# Charger les variables d'environnement
load_dotenv()

# Créer une instance des Classes
trans_handler = Transaction()

#Vérification si autorisation serveurs et joueurs:
AUTHORIZED_SERVER_ACCESS = os.getenv('SERVER_ACCESS')
AUTHORIZED_SUPERSERVER_ACCESS = os.getenv('SUPER_SERVER_ACCESS')
AUTHORIZED_USER_ID = os.getenv('ADMIN_USER')
AUTHORIZED_SUPERUSER_ID = os.getenv('SUPERADMIN_USER')

class Transaction(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def add(self,ctx, *, ressources: str):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
            # Transformer la chaîne en une liste de ressources
            liste_ressources = transformer_ressources(ressources)
            response = trans_handler.add_ressource_trans_in(liste_ressources,ctx.author.id)
            await response_discord(ctx,response,f"Les transactions IN ont été ajouté. La bank a été mis à jour")
        else:
            await response_discord(ctx,"Commande interdite", "Vous n'avez pas accès à cette commande")

    @commands.command()
    async def retrait(self,ctx, *, ressources: str):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
            # Transformer la chaîne en une liste de ressources
            liste_ressources = transformer_ressources(ressources)
            response = trans_handler.retrait_ressource_trans_in(liste_ressources,ctx.author.id)
            await response_discord(ctx,response,f"Les transactions OUT ont été ajouté. La bank a été mis à jour")
        else:
            await response_discord(ctx,"Commande interdite", "Vous n'avez pas accès à cette commande")


async def setup(bot):
    await bot.add_cog(Transaction(bot))