import discord
from discord.ext import commands
from discord import Embed
import os
from dotenv import load_dotenv
import asyncio

# Charger les variables d'environnement
load_dotenv()

# Récupérer le token du bot depuis le fichier .env
TOKEN = os.getenv('DISCORD_TOKEN')

# Créer une instance de bot avec les intentions nécessaires
intents = discord.Intents.default()
intents.message_content = True  # Activer l'accès au contenu des messages
intents.members = True  # Activer l'accès aux membres du serveur

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user.name} ({bot.user.id})')
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            await bot.load_extension(f"cogs.{name}")

if __name__ == "__main__":
    # Démarrer le bot avec votre token
    bot.run(TOKEN)