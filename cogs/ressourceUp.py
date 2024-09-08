import json
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import re

# Importer les classes
from function.ressourceUp import RessourceUp
from function.user import User
from utils import response_discord
from format import format_ressources_name_ressUp

# Charger les variables d'environnement
load_dotenv()

# Créer une instance des Classes
ressUp_handler = RessourceUp()
user_handler = User()

#Vérification si autorisation serveurs et joueurs:
AUTHORIZED_SERVER_ACCESS = os.getenv('SERVER_ACCESS')
AUTHORIZED_SUPERSERVER_ACCESS = os.getenv('SUPER_SERVER_ACCESS')
AUTHORIZED_USER_ID = os.getenv('ADMIN_USER')
AUTHORIZED_SUPERUSER_ID = os.getenv('SUPERADMIN_USER')

class RessourceUp(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def addRess(self, ctx, *, args: str):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
            # Regex pour capturer la ressource entre crochets
            match = re.search(r'\[(.*?)\]', args)
            if not match:
                await ctx.send("Erreur : le format de la ressource est incorrect. Veuillez utiliser des crochets.")
                return
            
            # Extraire la ressource
            ress = match.group(1)

            # Enlever la ressource de la chaîne restante
            args = args.replace(f'[{ress}]', '').strip()

            # Séparer les autres arguments
            try:
                qty, lvl, nom, info = args.split(' ', 3)
                qty = int(qty)  # Convertir en entier
                lvl = int(lvl)  # Convertir en entier
            except ValueError:
                await ctx.send("Erreur : veuillez fournir des valeurs numériques pour 'qty' et 'lvl'.")
                return

            # Logique de traitement ici
            response = ressUp_handler.ajout_ligne(ress, qty, lvl, nom, info, user_handler.getIdTeam(ctx.author.id))
            await response_discord(ctx, response, f"Vous avez bien rajouté la ressource {ress} en quantité {qty}, niveau {lvl}, pour {nom} en tant que {info}.")
        else:
            await response_discord(ctx,"Commande interdite", "Vous n'avez pas accès à cette commande")

    @commands.command()
    async def addXRess(self, ctx, *, json_data: str):
        if str(ctx.guild.id) in AUTHORIZED_SUPERSERVER_ACCESS:
            try:
                # Convertir les données JSON en liste de dictionnaires
                lignes = json.loads(json_data)
                result = ""
                # Valider le format des données
                if isinstance(lignes, list) and all(isinstance(ligne, dict) for ligne in lignes):
                    # Appeler la méthode pour ajouter les lignes une par une
                    responses = ressUp_handler.ajout_lignes(ctx,lignes)
                    # Envoyer les réponses pour chaque ligne ajoutée
                    for response in responses:
                        result += f"`{response}`\n"
                    await response_discord(ctx,"Lignes ajoutées",result)
                else:
                    await response_discord(ctx, "Format invalide", "Assurez-vous que les données sont une liste de dictionnaires.")
            except json.JSONDecodeError:
                await response_discord(ctx, "Erreur de format", "Les données JSON sont invalides.")
        else:
           await response_discord(ctx,"Commande interdite", "Vous n'avez pas accès à cette commande")
 
    @commands.command()
    async def getAllRessName(self,ctx,*,nom: str):
        ress_name = nom.strip("[]")
        response = ressUp_handler.search_all_ressource(ress_name)
        resp = format_ressources_name_ressUp(response.data)
        await response_discord(ctx,f'Liste des besoins en {nom}',resp)

async def setup(bot):
    await bot.add_cog(RessourceUp(bot))