from redbot.core import commands
import discord
from discord.ui import Button, Modal, TextInput, View

class BitBurner(commands.Cog):
    """BitBurner Game"""

    def __init__(self, bot):
        self.bot = bot

	
    @commands.group(name="bitburner", aliases=["bb"])
    async def bitburner(self, ctx):
        """BitBurner commands"""
        pass
	
	
	
    @bitburner.command(name="game")
    async def game(self, ctx):
        """
		Show the Link to the game
		"""
        embed = discord.Embed(
            title="BitBurner",
            description="A Hacking game simulator with real javascript programming",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url="http://hg-gaming.eu/app/icon.png")

        button = discord.ui.Button(label="play", style=discord.ButtonStyle.green, url="https://specs-hawaii-bless-donations.trycloudflare.com")
        view = discord.ui.View()
        view.add_item(button)
        await ctx.send(embed=embed, view=view)
		
		
    @bitburner.command(name="author")
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