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
        response = bank_handler.get_all_ressource()
        await response_discord(ctx,f"Affichage ressources",response)
    
    @commands.command()
    async def searchRess(self,ctx, *,ress_name: str):
        # Retirer les crochets s'ils existent et convertir en majuscules
        ress_name = ress_name.strip("[]")
        response = bank_handler.search_ressource(ress_name)
        await response_discord(ctx,f"Affichage ressource", response)
    
    @commands.command()
    async def updateQty(self,ctx,*,ress_name:str,qty):
        ress_name = ress_name.strip("[]")
        response = bank_handler.update_quantity(ress_name,qty)
        await response_discord(ctx,f"Ressource update",response)

async def setup(bot):
    await bot.add_cog(Bank(bot))