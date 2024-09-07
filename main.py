import discord
from discord.ext import commands
from discord import Embed
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer le token du bot depuis le fichier .env
TOKEN = os.getenv('DISCORD_TOKEN')

# Créer une instance de bot avec les intentions nécessaires
intents = discord.Intents.default()
intents.message_content = True  # Activer l'accès au contenu des messages
intents.members = True  # Activer l'accès aux membres du serveur

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# ID de l'utilisateur autorisé
AUTHORIZED_USER_ID = os.getenv('ADMIN_USER')
AUTHORIZED_SUPERUSER_ID = os.getenv('SUPERADMIN_USER')

# Exemple d'événement qui se déclenche quand le bot est prêt
@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user.name}')

# Démarrer le bot
bot.run(TOKEN)