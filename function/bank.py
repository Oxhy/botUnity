# bank.py
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from utils import supprimer_accents_et_convertir_maj

# Charger les variables d'environnement
load_dotenv()

class Bank:
    def __init__(self):
        # Récupérer les informations de connexion de Supabase
        SUPABASE_URL = os.getenv('SUPABASE_URL')
        SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        # Créer une instance du client Supabase
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def get_all_ressource(self):
        # Interroger la table 'Bank' pour sélectionner les lignes avec quantity > 0
        response = self.supabase.table('BANK').select('*').gt('QUANTITY', 0).execute()
        return response

    def search_ressource(self,ress_name):
        #ress_name = supprimer_accents_et_convertir_maj(ress_name)
        print(ress_name)
        response = self.supabase.table('BANK').select('*').eq('RESSOURCE_NAME',ress_name).execute()
        print(response)
        return response
    
    def update_quantity(self,ress_name,qty):
        ress_name = supprimer_accents_et_convertir_maj(ress_name)
        response = self.supabase.table('BANK').update({'QUANTITY',qty}).eq('RESSOURCE_NAME',ress_name).execute()
        return response