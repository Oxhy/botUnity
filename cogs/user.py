import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv

# Importer les classes
from function.user import User
from utils import response_discord

# Charger les variables d'environnement
load_dotenv()

# Créer une instance des Classes
user_handler = User()

#Vérification si autorisation serveurs et joueurs:
AUTHORIZED_SERVER_ACCESS = os.getenv('SERVER_ACCESS')
AUTHORIZED_SUPERSERVER_ACCESS = os.getenv('SUPER_SERVER_ACCESS')
AUTHORIZED_USER_ID = os.getenv('ADMIN_USER')
AUTHORIZED_SUPERUSER_ID = os.getenv('SUPERADMIN_USER')

class User(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
   
    @commands.command()
    async def addUser(self, ctx: commands.Context, pseudo: str):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
            # Ajouter l'utilisateur à la base de données
            response = user_handler.ajouter_utilisateur(pseudo,ctx.author.id)
            await response_discord(ctx,f'Utilisateur ajouté!',response)
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def updateTeam(self,ctx,pseudo:str,arg2):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
            try:
                # Vérifier si arg2 est un nombre (donc une équipe)
                idTeam = int(arg2)
                # Appeler la fonction update_teamNumber si arg2 est un entier
                response = user_handler.update_teamNumber(pseudo, idTeam)
                await response_discord(ctx,f'Team changé!',f"L'utilisateur {pseudo} a eu sa team changé en {idTeam} avec succès!")            
            except ValueError:
                # Si arg2 n'est pas un entier, il est considéré comme un pseudo
                pseudo2 = arg2
                response = user_handler.update_teamPseudo(pseudo, pseudo2)
                await response_discord(ctx,f'Team changé!', f"L'utilisateur {pseudo} a eu sa team changé avec le même ID de l'équipe de {pseudo2} avec succès!")
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")


    @commands.command()
    async def deleteUser(self,ctx,pseudo:str):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
            if str(ctx.author.id) in AUTHORIZED_SUPERUSER_ID:
                response = user_handler.delete_user(pseudo)
                await response_discord(ctx,f'Utilisateur supprimé!',f"L'utilisateur {pseudo} a été supprimé avec succès!")
            else:
                await response_discord(ctx,f"Pas autorisé", "Vous n'avez pas accès à cette commande avec vos droits")
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")

    @commands.command()
    async def updatePseudo(self,ctx,pseudo:str,newPseudo:str):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
            response = user_handler.update_Pseudo(pseudo,newPseudo,ctx.author.id)
            await response_discord(ctx,f'Utilisateur update!',f"L'utilisateur {pseudo} a eu son pseudo changer en {newPseudo} avec succès!")
        else:
            await response_discord(ctx,f"Pas autorisé", "Vous n'êtes pas sur un serveur qui a accès à cette commande")


async def setup(bot):
    await bot.add_cog(User(bot))