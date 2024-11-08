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
        if str(ctxUser) in AUTHORIZED_SUPERUSER_ID and str(ctxServer) in AUTHORIZED_SUPERSERVER_ACCESS:
            return (
                "`!addUser: [pseudo]`\n"
                "`!updateTeam: [pseudo] [idTeam|pseudo autre joueur]`\n"
                "`!updatePseudo: [pseudo] [newPseudo]`\n"
                "`!deleteUser: [pseudo]`\n"
            )
        elif str(ctxUser) not in AUTHORIZED_SUPERUSER_ID and str(ctxServer) in AUTHORIZED_SUPERSERVER_ACCESS:
            return (
                "`!addUser: [pseudo]`\n"
                "`!updateTeam: [pseudo] [idTeam|pseudo autre joueur]`\n"
                "`!updatePseudo: [pseudo] [newPseudo]`\n"
            )
        else:
            return (
                "`!addUser: [pseudo]`\n"
                "`!updatePseudo: [pseudo] [newPseudo]`\n"
            )
    
    @staticmethod
    def getBankCommands(self,ctxUser,ctxServer):
        if str(ctxServer) in AUTHORIZED_SUPERSERVER_ACCESS:
            return(
                "`!allRess`\n"
                "`!searchRess: [nom ressource entre crochet]`\n"
                "`!updateQty: [nom ressource entre crochet]`\n"
            )
        else:
            return "Aucune commande"
    
    @staticmethod
    def getTransactionCommands(self,ctxUser,ctxServer):
        if str(ctxServer) in AUTHORIZED_SUPERSERVER_ACCESS:
            return(
                "`!add: [nom ressource entre crochet] [Quantité] [.] | Répéter ce format suivant le nombre de ressource à ajouter`\n"
                "`!retrait: [nom ressource entre crochet] [Quantité] [.] | Répéter ce format suivant le nombre de ressource à retirer`\n"
            )
        else:
            return "Aucune commande"
    
    @staticmethod
    def getRessourceUpCommands(self,ctxUser,ctxServer):
        if str(ctxServer) in AUTHORIZED_SUPERSERVER_ACCESS:
            return(
                "`!getAllRessName: [nom ressource entre crochet]`\n"
                "`!getRessCat: [nom métier ou cra] [level de départ] [level d'arrivée] | !getRessCat Tailleur 3 5 donnera les ressources nécessaires pour le métier entre le level 3 et 5`\n"
                "`!getRessBf: [level] | Affiche les ressources nécessaires jusqu'au level  indiqué en fonction du level renseigné dans avancement`\n"
            )
        else:
            return "Aucune commande"
    
    @staticmethod
    def getAvancementCommands(self,ctxUser,ctxServer):
        if str(ctxServer) in AUTHORIZED_SUPERSERVER_ACCESS:
            return(
                "`!cra: [level]`\n"
                "`!tailleur: [level]`\n"
                "`!cordo: [level]`\n"
                "`!bijou: [level]`\n"
                "`!sculpteur: [level]`\n"
                "`!forgeron: [level]`\n"
                "`!faco: [level]`\n"
                "`!mineur: [level]`\n"
                "`!bucheron: [level]`\n"
                "`!alchi: [level]`\n"
                "`!pecheur: [level]`\n"
                "`!paysan: [level]`\n"
                "`!brico: [level]`\n"
                "`!chasseur: [level]`\n"
                "`!joillo: [level]`\n"
                "`!cordomage: [level]`\n"
                "`!costu: [level]`\n"
                "`!forgemage: [level]`\n"
                "`!sculptemage: [level]`\n"
                "`!facomage: [level]`\n"
                "`!level`\n"
            )
        else:
            return "Aucune commande"