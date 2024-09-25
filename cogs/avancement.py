import json
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import re

# Importer les classes
from function.avancement import Avancement
from utils import response_discord
from format import format_ressources_name_ressUp

# Charger les variables d'environnement
load_dotenv()

# Créer une instance des Classes
avancement_handler = Avancement()

#Vérification si autorisation serveurs et joueurs:
AUTHORIZED_SERVER_ACCESS = os.getenv('SERVER_ACCESS')
AUTHORIZED_SUPERSERVER_ACCESS = os.getenv('SUPER_SERVER_ACCESS')
AUTHORIZED_USER_ID = os.getenv('ADMIN_USER')
AUTHORIZED_SUPERUSER_ID = os.getenv('SUPERADMIN_USER')

class Avancement(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def cra(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('CRA',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")
    
    @commands.command()
    async def tailleur(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('TAILLEUR',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")
    
    @commands.command()
    async def cordo(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('CORDONNIER',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def bijou(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('BIJOUTIER',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")
    @commands.command()
    async def sculpteur(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('SCULPTEUR',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def forgeron(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('FORGERON',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def faco(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('FACONNEUR',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def mineur(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('MINEUR',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")
    
    @commands.command()
    async def bucheron(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('BUCHERON',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def alchi(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('ALCHIMISTE',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def pecheur(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('PECHEUR',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def paysan(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('PAYSAN',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def brico(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('BRICOLEUR',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def chasseur(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('CHASSEUR',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def joillo(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('JOILLOMAGE',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def cordommage(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('CORDOMMAGE',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def costu(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('COSTUMAGE',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def forgemage(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('FORGEMAGE',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def sculptemage(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('SCULPTEMAGE',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")
    
    @commands.command()
    async def facomage(self,ctx,lvl):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.modif_level('FACOMAGE',lvl)
             await response_discord(ctx,f"Modification effectué", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")
    
    @commands.command()
    async def level(self,ctx):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
             response = avancement_handler.level()
             await response_discord(ctx,f"Liste level", response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

async def setup(bot):
    await bot.add_cog(Avancement(bot))