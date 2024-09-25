# avancement.py
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from utils import supprimer_accents_et_convertir_maj,supprimer_accents

# Charger les variables d'environnement
load_dotenv()

class Avancement:
    def __init__(self):
        # Récupérer les informations de connexion de Supabase
        SUPABASE_URL = os.getenv('SUPABASE_URL')
        SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        # Créer une instance du client Supabase
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    def modif_level(self,categorie,level):
        response = self.supabase.table('AVANCEMENT').update({'LEVEL':level}).eq('NAME',categorie).execute()
        return response

    def level(self):
        response = self.supabase.table('AVANCEMENT').select('*').execute()
        return response