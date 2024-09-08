# bank.py
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from utils import supprimer_accents_et_convertir_maj,supprimer_accents
from function.user import User

# Charger les variables d'environnement
load_dotenv()

user_handler = User()

class RessourceUp:
    def __init__(self):
        # Récupérer les informations de connexion de Supabase
        SUPABASE_URL = os.getenv('SUPABASE_URL')
        SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        # Créer une instance du client Supabase
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def ajout_ligne(self,ctx,ress,qty,lvl,nom,info,idTeam):
        ress = supprimer_accents(ress)
        nom = supprimer_accents_et_convertir_maj(nom)
        info = supprimer_accents_et_convertir_maj(info)
        if info in ('METIER','STUFF','METIERS','STUFFS'):
            if info == 'METIERS': info = 'METIER'
            if info == 'STUFFS': info = "METIER"
            data = {
                'RESSOURCE_NAME':ress,
                'QUANTITY':qty,
                'NAME':nom,
                'LEVEL':lvl,
                'STUFF_METIER':info,
                'IDTEAM':idTeam
            }
            self.supabase.table('RESSOURCE_UP').insert(data).execute()
            response = self.supabase.table('BANK').select('*').eq('RESSOURCE_NAME',ress).execute()
            if not response.data : 
                data_bank ={
                    'RESSOURCE_NAME':ress,
                    'QUANTITY':0,
                    'NEED_QTY':qty
                }
                self.supabase.table('BANK').insert(data_bank).execute()
            else:
                qty = response.data[0]['NEED_QTY'] + qty
                self.supabase.table('BANK').update({'NEED_QTY':qty}).eq('RESSOURCE_NAME',ress).execute()
        else:
            return 'Il faut mettre METIER ou STUFF comme nom'
        return 'Ressource ajoutée'

    def ajout_lignes(self,ctx,lignes):
        responses = []
        ajout_success = 0
        ajout_echec = 0
        for ligne in lignes:
            ressource_name = ligne['RESSOURCE_NAME'].strip('[]')
            name = ligne['NAME'].upper()
            RessourceUp.ajout_ligne(self,ctx,ressource_name,int(ligne['QUANTITY']),int(ligne['LEVEL']),ligne['NAME'],ligne['STUFF_METIER'],user_handler.getIdTeam(ctx.author.id))
            result = self.supabase.table('RESSOURCE_UP').select('*').eq('RESSOURCE_NAME',ressource_name).eq('QUANTITY',int(ligne['QUANTITY'])).eq('LEVEL',int(ligne['LEVEL'])).eq('NAME',ligne['NAME'].upper()).eq('STUFF_METIER',ligne['STUFF_METIER']).execute()
            print(result)
            if result.data:
                ajout_success += 1
                response = f"La ressource {ressource_name} a été ajoutée en quantité {ligne['QUANTITY']} au level {ligne['LEVEL']} pour {ligne['NAME']}"
            else:
                ajout_echec += 1
                response = f"Echec de l'ajout de la ressource {ressource_name} en quantité {ligne['QUANTITY']} au level {ligne['LEVEL']} pour {ligne['NAME']}"
            responses.append(response)
        responses.append(f"{ajout_success} lignes ont été ajoutés et {ajout_echec} n'ont pas été ajoutée")
        return responses
    
    def search_all_ressource(self,ress):
        ress = supprimer_accents(ress)
        response = self.supabase.table('RESSOURCE_UP').select('*').eq('RESSOURCE_NAME',ress).execute()
        return response