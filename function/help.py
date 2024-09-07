# user.py
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from utils import supprimer_accents_et_convertir_maj

# Charger les variables d'environnement
load_dotenv()

#Vérification si autorisation serveurs et joueurs:
AUTHORIZED_SERVER_ACCESS = os.getenv('SERVER_ACCESS')
AUTHORIZED_SUPERSERVER_ACCESS = os.getenv('SUPER_SERVER_ACCESS')
AUTHORIZED_USER_ID = os.getenv('ADMIN_USER')
AUTHORIZED_SUPERUSER_ID = os.getenv('SUPERADMIN_USER')

class Help:
    def __init__(self):
        # Récupérer les informations de connexion de Supabase
        SUPABASE_URL = os.getenv('SUPABASE_URL')
        SUPABASE_KEY = os.getenv('SUPABASE_KEY')
        # Créer une instance du client Supabase
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    @staticmethod
    def getUserCommands(self,ctxUser,ctxServer):
        if ctxUser in AUTHORIZED_SUPERUSER_ID and ctxServer in AUTHORIZED_SUPERSERVER_ACCESS:
            return (
                "`!addUser: [pseudo]`\n"
                "`!updateTeam: [pseudo] [idTeam|pseudo autre joueur] | nécessite les droits admins`\n"
                "`!updatePseudo: [pseudo] [newPseudo]`\n"
                "`!deleteUser: [pseudo] | nécessite les droits admins`\n"
            )
        elif ctxUser not in AUTHORIZED_SUPERUSER_ID and ctxServer in AUTHORIZED_SUPERSERVER_ACCESS:
            return (
                "`!addUser: [pseudo]`\n"
                "`!updateTeam: [pseudo] [idTeam|pseudo autre joueur] | nécessite les droits admins`\n"
                "`!updatePseudo: [pseudo] [newPseudo]`\n"
            )
        else:
            return (
                "`!addUser: [pseudo]`\n"
                "`!updatePseudo: [pseudo] [newPseudo]`\n"
            )