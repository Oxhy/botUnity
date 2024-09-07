# user.py
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from utils import supprimer_accents_et_convertir_maj

# Charger les variables d'environnement
load_dotenv()

class User:
    def __init__(self):
        # Récupérer les informations de connexion de Supabase
        SUPABASE_URL = os.getenv('SUPABASE_URL')
        SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        # Créer une instance du client Supabase
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def ajouter_utilisateur(self, pseudo,discordID):
        response = self.supabase.table('USER').select('*').eq('DISCORD_ID',discordID).execute()
        if not response.data:
            data = {
                'PSEUDO': supprimer_accents_et_convertir_maj(pseudo),
                'DISCORD_ID': discordID
            }
            self.supabase.table('USER').insert(data).execute()
            response = f"L'utilisateur {pseudo} a été ajouté avec succès!"
        else:
            response = f"Vous avez déjà un utilisateur associé à votre compte : {response.data[0]['PSEUDO']}"
        return response
    
    def update_teamNumber(self,pseudo, idTeam):
        response = self.supabase.table('USER').update({'IDTEAM': idTeam}).eq('PSEUDO', supprimer_accents_et_convertir_maj(pseudo)).execute()
        print('Réponse:', response)
        return response
    
    def update_teamPseudo(self,pseudo, pseudoTeam):
         # Récupérer l'idTeam de pseudo2
        response = self.supabase.table('USER').select('IDTEAM').eq('PSEUDO', supprimer_accents_et_convertir_maj(pseudoTeam)).execute()
        if response.data and len(response.data) > 0:
            idTeam_pseudo2 = response.data[0]['IDTEAM']
        else:
            return {"error": "Pseudo2 non trouvé ou pas d'idTeam associé"}     
        # Mettre à jour idTeam de pseudo1 avec l'idTeam de pseudo2
        update_response = self.supabase.table('USER').update({'IDTEAM': idTeam_pseudo2}).eq('PSEUDO', supprimer_accents_et_convertir_maj(pseudo)).execute()
        return update_response
    
    def delete_user(self,pseudo):
        response = self.supabase.table('USER').delete().eq('PSEUDO',supprimer_accents_et_convertir_maj(pseudo)).execute()
        return response
    
    def update_Pseudo(self,pseudo,newPseudo):
        response = self.supabase.table('USER').update({'PSEUDO': supprimer_accents_et_convertir_maj(newPseudo)}).eq('PSEUDO',supprimer_accents_et_convertir_maj(pseudo)).execute()
        return response