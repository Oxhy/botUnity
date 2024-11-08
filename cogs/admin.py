import discord
from discord.ext import commands
from datetime import datetime
import os

# Créer une instance des Classes
from function.admin import Admin

# Charger les variables d'environnement
from dotenv import load_dotenv
load_dotenv()

WELCOME_CHANNEL_ID = 1304498971531808808
LEAVE_CHANNEL_ID = 1304498992645931008
LOG_CHANNEL_ID = 1304495633717268622

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def create_embed(self, title, description, color=discord.Color.green(), footer_text=None, thumbnail_url=None, author=None):
        """Créer un embed standard avec un titre, description, et optionnellement un footer, un emblème, et un auteur (avatar)"""
        embed = discord.Embed(title=title, description=description, color=color)
        if footer_text:
            embed.set_footer(text=footer_text)
        if thumbnail_url:
            embed.set_thumbnail(url=thumbnail_url)  # Ajouter l'emblème ici
        if author:
            embed.set_author(name=author.name, icon_url=author.avatar.url)  # Correction ici pour utiliser `avatar.url`
        return embed

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        if log_channel is None:
            return

        if before.nick != after.nick:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            embed = self.create_embed(
                title="Changement de pseudo",
                description=( 
                    f"{after.mention} a changé de pseudo\n"
                    f"Avant : {before.nick if before.nick else 'Aucun'}\n"
                    f"Après : {after.nick if after.nick else 'Aucun'}\n"
                    f"ID: {after.id} - {timestamp}"
                ),
                author=after  # Ajouter l'avatar du membre
            )
            await log_channel.send(embed=embed)

        if before.avatar != after.avatar:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            embed = self.create_embed(
                title="Changement d'avatar",
                description=f"{after.mention} a changé d'avatar\nID: {after.id} - {timestamp}",
                author=after  # Ajouter l'avatar du membre
            )
            await log_channel.send(embed=embed)

        added_roles = [role for role in after.roles if role not in before.roles]
        removed_roles = [role for role in before.roles if role not in after.roles]

        if added_roles:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            embed = self.create_embed(
                title="Rôle ajouté",
                description=( 
                    f"{after.mention} a reçu le(s) rôle(s) : {', '.join([role.name for role in added_roles])}\n"
                    f"ID: {after.id} - {timestamp}",
                ),
                author=after  # Ajouter l'avatar du membre
            )
            await log_channel.send(embed=embed)

        if removed_roles:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            embed = self.create_embed(
                title="Rôle retiré",
                description=( 
                    f"{after.mention} a perdu le(s) rôle(s) : {', '.join([role.name for role in removed_roles])}\n"
                    f"ID: {after.id} - {timestamp}",
                ),
                author=after  # Ajouter l'avatar du membre
            )
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
        if log_channel is not None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # URL de l'emblème (par exemple, l'URL de votre image de serveur ou logo)
            thumbnail_url = "https://example.com/your_logo.png"  # Remplacez par l'URL de votre image

            embed = self.create_embed(
                title="Bienvenue sur le serveur !",
                description=f"{member.mention} a rejoint le serveur\nID: {member.id} - {timestamp}",
                thumbnail_url=thumbnail_url,  # Ajout de l'emblème
                author=member  # Ajouter l'avatar du membre
            )
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel = self.bot.get_channel(LEAVE_CHANNEL_ID)
        if log_channel is not None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            embed = self.create_embed(
                title="Utilisateur quitté",
                description=f"{member.mention} a quitté le serveur\nID: {member.id} - {timestamp}",
                author=member  # Ajouter l'avatar du membre
            )
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.content != after.content:
            log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
            if log_channel is not None:
                user = before.author
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                embed = self.create_embed(
                    title="Message édité",
                    description=( 
                        f"{user.mention}\n"
                        f"Message modifié dans {before.channel.mention}\n"
                        f"Avant : {before.content or 'Aucun contenu'}\n"
                        f"Après : {after.content or 'Aucun contenu'}\n"
                        f"ID: {user.id} - {timestamp}",
                    ),
                    author=user  # Ajouter l'avatar de l'utilisateur
                )
                await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        if log_channel is not None:
            user = message.author
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            embed = self.create_embed(
                title="Message supprimé",
                description=( 
                    f"{user.mention}\n"
                    f"Message supprimé dans {message.channel.mention}\n"
                    f"{message.content or 'Aucun contenu'}\n"
                    f"ID: {user.id} - {timestamp}",
                ),
                author=user  # Ajouter l'avatar de l'utilisateur
            )
            await log_channel.send(embed=embed)

# Fonction de setup pour ajouter le cog
async def setup(bot):
    await bot.add_cog(Admin(bot))
