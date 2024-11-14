from redbot.core import commands
import discord
from discord.ui import Button, Modal, TextInput, View

class ArtistLinks(commands.Cog):
    """Links to Artist's sites"""

    def __init__(self, bot):
        self.bot = bot

	
    @commands.group(name="artistlinks", aliases=["al"])
    async def artistlinks(self, ctx):
        """ArtistLink commands"""
        pass
	
	
	
    @artistlinks.group(name="list")
    async def list(self, ctx):
        """Show the Artists that provided their links"""
        pass
		
		
    @artistlinks.command(name="author")
    async def author(self, ctx: commands.Context):
        """
        Display the author and editor information for this bot module.
        """
        author_name = "Kael"  # Replace this with your actual name or username
        author_discord_tag = "hg_dreamer"  # Replace with your Discord tag if you want

        embed = discord.Embed(
            title="Module Author",
            description=(
                f"This module was created by **{author_name}**.\n"
                f"if there are any issues please contact **{author_name}**"
            ),
            color=await ctx.embed_color()
        )
        await ctx.send(embed=embed)
	
    
    @list.command(name="theuser")
    async def theuser(self, ctx: commands.Context):
        """
        THEUSER's Links
        """
        guild_id = 1296779416088739873
        guild = self.bot.get_guild(guild_id)
        kofi_id = guild.get_emoji(1306596013011767346)
        x_id = guild.get_emoji(1306595956304908298)
        bsky_id = guild.get_emoji(1306595987833229343)
        derpi_id = guild.get_emoji(1306601999596392478)

        embed = discord.Embed(
            title="THEUSER",
            description=(
                f"{x_id} [THE_USER_001](https://x.com/THE_USER_001)\n"
                f"{bsky_id} [@theuser001](https://bsky.app/profile/theuser001.bsky.social)\n"
                f"{kofi_id} [theuser001](https://ko-fi.com/theuser001)\n"
                f"{derpi_id} [User001](https://derpibooru.org/profiles/User001)\n"
            ),
            color=await ctx.embed_color()
        )
        await ctx.send(embed=embed)
	
    @list.command(name="melassa")
    async def melassa(self, ctx: commands.Context):
        """
        Melassa's Links
        """
        guild_id = 1296779416088739873
        guild = self.bot.get_guild(guild_id)
        boosty_id = guild.get_emoji(1306595894639984650)
        lavatop_id = guild.get_emoji(1306595927192113155)
        x_id = guild.get_emoji(1306595956304908298)
        bsky_id = guild.get_emoji(1306595987833229343)
        derpi_id = guild.get_emoji(1306601999596392478)

        embed = discord.Embed(
            title="Melassa",
            description=(
                f"{x_id} [melassathepony](https://x.com/melassathepony)\n"
                f"{bsky_id} [@Melassa](https://bsky.app/profile/melassa.bsky.social)\n"
                f"{boosty_id} [melassathepony](https://boosty.to/melassathepony)\n"
                f"{lavatop_id} [melassathepony](https://app.lava.top/en/melassathepony)\n"
                f"{derpi_id} [Melassa](https://derpibooru.org/profiles/Melassa)\n"
            ),
            color=await ctx.embed_color()
        )
        await ctx.send(embed=embed)