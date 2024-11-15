from redbot.core import commands
import discord
from discord.ui import Button, Modal, TextInput, View

class ScamDetect(commands.Cog):
    """Checks account age and interaction and sends a notification if they're suspected to be a scammer"""

    def __init__(self, bot):
        self.bot = bot
        self.min_account_age = 2 * 365 * 24 * 60 * 60
        self.min_interaction_time = None
        self.log_channel_id = None

    @commands.group(name="scamdetect", aliases=["sd"])
    async def scamdetect(self, ctx):
        """ScamDetect commands"""
        pass
	
    @scamdetect.command(name="settime")
    @commands.has_permissions(manage_guild=True)
    async def settime(self, ctx, weeks: int):
        """sets the minimum interaction time in weeks"""
        self.min_interaction_time = weeks * 7 * 24 * 60 * 60
        await ctx.send(f"Minimum interaction time set to {weeks} weeks.")
	
    @scamdetect.command(name="setchannel")
    @commands.has_permissions(manage_guild=True)
    async def setchannel(self, ctx, channel: discord.TextChannel):
        self.log_channel_id = channel.id
        await ctx.send(f"Log channel has been set to {channel.mention}.")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        checks a user's account age and interaction on the server when they join
        """
        await self.check_and_log_user(member)
		
    async def check_and_log_user(self, member: discord.Member):
        now = datetime.utcnow()
        account_age = (now - member.created_at).total_seconds()
        last_message = max(message.created_at for message in member.history(limit=1)) if member.history else None
        last_interaction_time = (now - last_message).total_seconds() if last_message else 0
		
        if account_age < self.min_account_age and last_interaction_time < self.min_interaction_time:
            log_channel = self.bot.get_channel(self.log_channel_id)
            if log_channel:
                await log_channel.send(f"User {member.name} ({member.id}) might be suspected to be a Scam account.\nPROCEED WITH CAUTION!")
	
	