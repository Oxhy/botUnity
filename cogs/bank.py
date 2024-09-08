import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv

# Importer les classes
from function.bank import Bank
from utils import response_discord

# Charger les variables d'environnement
load_dotenv()

# Créer une instance des Classes
bank_handler = Bank()

#Vérification si autorisation serveurs et joueurs:
AUTHORIZED_SERVER_ACCESS = os.getenv('SERVER_ACCESS')
AUTHORIZED_SUPERSERVER_ACCESS = os.getenv('SUPER_SERVER_ACCESS')
AUTHORIZED_USER_ID = os.getenv('ADMIN_USER')
AUTHORIZED_SUPERUSER_ID = os.getenv('SUPERADMIN_USER')

class Bank(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def allRess(self,ctx):
        if ctx.guild.id in AUTHORIZED_SUPERSERVER_ACCESS:
            response = bank_handler.get_all_ressource()
            await response_discord(ctx,f"Affichage ressources",response)
        else:
            await response_discord(ctx,"Commande interdite", "Vous n'avez pas accès à cette commande")
    
    @commands.command()
    async def searchRess(self,ctx, *,ress_name: str):
        if ctx.guild.id in AUTHORIZED_SUPERSERVER_ACCESS:
            # Retirer les crochets s'ils existent et convertir en majuscules
            ress_name = ress_name.strip("[]")
            print(ress_name)
            response = bank_handler.search_ressource(ress_name)
            await response_discord(ctx,f"Affichage ressource", response)
        else:
            await response_discord(ctx,"Commande interdite", "Vous n'avez pas accès à cette commande")
    
    @commands.command()
    async def updateQty(self,ctx,*,ress_name:str,qty):
        if ctx.guild.id in AUTHORIZED_SUPERSERVER_ACCESS:
            ress_name = ress_name.strip("[]")
            response = bank_handler.update_quantity(ress_name,qty)
            await response_discord(ctx,f"Ressource update",response)
        else:
            await response_discord(ctx,"Commande interdite", "Vous n'avez pas accès à cette commande")

async def setup(bot):
    await bot.add_cog(Bank(bot))