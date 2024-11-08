import discord
from discord.ext import commands

class RoleSelectorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_message_id = None  # ID du message final avec le menu de rôles
        self.role_emoji_map = {}     # Associe les émojis aux rôles

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def rolemenu(self, ctx):
        """Demande un titre et des paires émoji/rôle pour créer un menu de sélection de rôle par réaction."""

        def check_author(m):
            return m.author == ctx.author and m.channel == ctx.channel

        # Capture le message de la commande `!rolemenu`
        command_message = ctx.message

        # Demande le titre pour le menu
        await ctx.send("Veuillez entrer le titre du menu de sélection des rôles :")
        try:
            title_msg = await self.bot.wait_for("message", check=check_author, timeout=60.0)
            title = title_msg.content
        except TimeoutError:
            await ctx.send("Temps écoulé. Veuillez relancer la commande.")
            return

        # Initialisation du dictionnaire des rôles et émojis
        role_emoji_map = {}

        # Boucle pour ajouter des paires émoji/rôle
        while True:
            await ctx.send("Entrez un émoji pour le rôle (ou tapez `fin` pour terminer) :")
            try:
                emoji_msg = await self.bot.wait_for("message", check=check_author, timeout=60.0)
                if emoji_msg.content.lower() == "fin":
                    break
                emoji = emoji_msg.content
            except TimeoutError:
                await ctx.send("Temps écoulé. Veuillez relancer la commande.")
                return

            # Demande le nom du rôle associé à l'émoji
            await ctx.send("Entrez le nom du rôle associé à cet émoji :")
            try:
                role_msg = await self.bot.wait_for("message", check=check_author, timeout=60.0)
                role_name = role_msg.content
            except TimeoutError:
                await ctx.send("Temps écoulé. Veuillez relancer la commande.")
                return

            # Vérifie si le rôle existe sur le serveur
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if role is None:
                await ctx.send(f"Le rôle `{role_name}` n'existe pas sur ce serveur. Veuillez réessayer.")
                continue

            # Enregistre l'association émoji-rôle
            role_emoji_map[emoji] = role

        if not role_emoji_map:
            await ctx.send("Aucun rôle n'a été défini. Commande annulée.")
            return

        # Création de l'embed avec le titre défini par l'utilisateur
        embed = discord.Embed(title=title, description="Réagissez avec les émojis ci-dessous pour recevoir ou retirer le rôle associé.", color=discord.Color.blue())
        for emoji, role in role_emoji_map.items():
            embed.add_field(name=f"{emoji} {role.name}", value=f"Réagissez avec {emoji} pour obtenir ou retirer le rôle {role.name}.", inline=False)

        # Envoie le message embed et ajoute les réactions
        final_message = await ctx.send(embed=embed)
        self.role_message_id = final_message.id
        self.role_emoji_map = role_emoji_map

        # Ajoute les réactions à l'embed
        for emoji in role_emoji_map.keys():
            await final_message.add_reaction(emoji)

        # Supprime les messages entre `!rolemenu` (inclus) et le message final
        await self.cleanup_messages(ctx.channel, command_message.id, final_message.id)

    async def cleanup_messages(self, channel, start_message_id, end_message_id):
        """Supprime les messages dans un canal entre deux messages spécifiés par leurs IDs, en incluant le message de début."""
        try:
            messages_to_delete = []
            async for message in channel.history(after=discord.Object(id=start_message_id - 1), before=discord.Object(id=end_message_id)):
                messages_to_delete.append(message)
            await channel.delete_messages(messages_to_delete)
        except discord.Forbidden:
            await channel.send("Je n'ai pas la permission de supprimer les messages.")
        except discord.HTTPException:
            await channel.send("Une erreur est survenue lors de la suppression des messages.")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """Attribue le rôle lorsque l'utilisateur ajoute une réaction."""
        if payload.message_id != self.role_message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        emoji = str(payload.emoji)
        role = self.role_emoji_map.get(emoji)
        if role is None:
            return

        member = guild.get_member(payload.user_id)
        if member is None or member.bot:
            return

        # Attribue le rôle sans envoyer de message privé
        try:
            await member.add_roles(role)
        except discord.Forbidden:
            channel = guild.get_channel(payload.channel_id)
            if channel:
                await channel.send("Je n'ai pas la permission d'ajouter ce rôle à l'utilisateur.")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """Retire le rôle lorsque l'utilisateur retire une réaction."""
        if payload.message_id != self.role_message_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        emoji = str(payload.emoji)
        role = self.role_emoji_map.get(emoji)
        if role is None:
            return

        member = guild.get_member(payload.user_id)
        if member is None or member.bot:
            return

        # Retire le rôle sans envoyer de message privé
        try:
            await member.remove_roles(role)
        except discord.Forbidden:
            channel = guild.get_channel(payload.channel_id)
            if channel:
                await channel.send("Je n'ai pas la permission de retirer ce rôle à l'utilisateur.")

# Fonction de setup pour ajouter le cog
async def setup(bot):
    await bot.add_cog(RoleSelectorCog(bot))
