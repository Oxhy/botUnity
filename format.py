import discord
from discord.ext import commands
from discord.ui import View, Button
from supabase import create_client, Client
import os
from dotenv import load_dotenv
import unicodedata
import re
from utils import get_quantity_from_bank

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

def format_ressources_name_ressUp(data):
    formatted_list = []
    ress_list = []
    for item in data:
        if item['RESSOURCE_NAME'] in ress_list:
            qty = item['QUANTITY'] - get_quantity_from_bank({item['RESSOURCE_NAME']})
        else:
            qty = item['QUANTITY']
            ress_list.append(item['RESSOURCE_NAME'])
        if(qty > 0):
            formatted_string = (
                f"Il manque {item['RESSOURCE_NAME']} en quantité {qty} pour {item['NAME']} {item['LEVEL']}"
            )
        else:
            formatted_string = (
                f"Il manque {item['RESSOURCE_NAME']} en quantité 0 pour {item['NAME']} {item['LEVEL']}"
            ) 
        formatted_list.append(formatted_string)
    return "\n".join(formatted_list)