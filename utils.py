import discord
from discord.ext import commands
from discord.ui import View, Button
from supabase import create_client, Client
import os
from dotenv import load_dotenv
import unicodedata
import re

# Charger les variables d'environnement
load_dotenv()

# Récupérer le token du bot depuis le fichier .env
TOKEN = os.getenv('DISCORD_TOKEN')

# ID de l'utilisateur autorisé
AUTHORIZED_USER_ID = os.getenv('ADMIN_USER')
AUTHORIZED_SUPERUSER_ID = os.getenv('SUPERADMIN_USER')

# Initialiser Supabase
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(url, key)

async def response_discord(ctx,title,description):
    # Charger l'image pour l'embed principal
    file_main = discord.File('./image/banniere.png', filename="banniere.png")
    # Charger l'image pour la miniature
    file_thumbnail = discord.File('./image/blason.png', filename="blason.png")
    # Créer l'embed avec l'image principale et la miniature
    embed = discord.Embed(title=title, 
                          description=description,
                          color=0xfe0404)
    # Définir l'image principale
    embed.set_image(url="attachment://banniere.png")
    # Définir la miniature
    embed.set_thumbnail(url="attachment://blason.png")
    # Envoyer l'embed avec les deux fichiers images
    await ctx.send(embed=embed, files=[file_main, file_thumbnail])

def supprimer_accents_et_convertir_maj(chaine):
    # Normaliser la chaîne en forme décomposée
    chaine = unicodedata.normalize('NFD', chaine)
    # Supprimer les caractères accentués
    chaine_sans_accents = ''.join(c for c in chaine if unicodedata.category(c) != 'Mn')
    chaine_majuscule = chaine_sans_accents.upper()
    return chaine_majuscule