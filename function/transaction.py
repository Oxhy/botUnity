# transaction.py
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from utils import supprimer_accents_et_convertir_maj

# Charger les variables d'environnement
load_dotenv()

class Transaction:
    def __init__(self):
        # Récupérer les informations de connexion de Supabase
        SUPABASE_URL = os.getenv('SUPABASE_URL')
        SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        # Créer une instance du client Supabase
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def add_ressource_trans_in(self,liste,user):
        # Insérer chaque ressource dans la base de données (ou traiter selon votre logique)
        user = self.supabase.table('USER').select('*').eq('DISCORD_ID', user).execute()
        for ressource in liste:
            response= self.supabase.table('BANK').select('*').eq('RESSOURCE_NAME',ressource['RESSOURCE_NAME']).execute()
            if response.data:
                data = {
                    'IDRESSOURCE': response.data[0]['ID_RESSOURCE'],
                    'IDUSER': user.data[0]['IDUSER'],
                    'TRANSACTIONNAME': 'IN',
                    'QUANTITY': int(ressource['QTY'])
                }
                qty = response.data[0]['QUANTITY'] + int(ressource['QTY'])
                self.supabase.table('BANK').update({'QUANTITY': qty}).eq('ID_RESSOURCE',response.data[0]['ID_RESSOURCE']).execute()
            else:
                self.supabase.table('BANK').insert({'RESSOURCE_NAME':ressource['RESSOURCE_NAME'],'QUANTITY': int(ressource['QTY']),'NEED_QTY': 0}).execute()
                response= self.supabase.table('BANK').select('*').eq('RESSOURCE_NAME',ressource['RESSOURCE_NAME']).execute()
                data = {
                    'IDRESSOURCE': response.data[0]['ID_RESSOURCE'],
                    'IDUSER': user.data[0]['IDUSER'],
                    'TRANSACTIONNAME': 'IN',
                    'QUANTITY': int(ressource['QTY'])
                }
            # Exemple d'insertion dans une base Supabase
            self.supabase.table('TRANSACTION').insert(data).execute()
        return 'Insertion en banque'
    
    def retrait_ressource_trans_in(self,liste,user):
        # Insérer chaque ressource dans la base de données (ou traiter selon votre logique)
        user = self.supabase.table('USER').select('*').eq('DISCORD_ID', user).execute()
        for ressource in liste:
            response= self.supabase.table('BANK').select('*').eq('RESSOURCE_NAME',ressource['RESSOURCE_NAME']).execute()
            data = {
                    'IDRESSOURCE': response.data[0]['ID_RESSOURCE'],
                    'IDUSER': user.data[0]['IDUSER'],
                    'TRANSACTIONNAME': 'IN',
                    'QUANTITY': int(ressource['QTY'])
                }
            qty = response.data[0]['QUANTITY'] - int(ressource['QTY'])
            self.supabase.table('BANK').update({'QUANTITY': qty}).eq('ID_RESSOURCE',response.data[0]['ID_RESSOURCE']).execute()
            # Exemple d'insertion dans une base Supabase
            self.supabase.table('TRANSACTION').insert(data).execute()
        return 'Retrait Banque'