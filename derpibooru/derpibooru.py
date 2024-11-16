from redbot.core import commands
import discord
import requests
import random

class Derpibooru(commands.Cog):
    """Looks for tags given on derpibooru and sends them into the channel"""

    def __init__(self, bot):
        self.bot = bot
        self.base_url = "https://derpibooru.org/api/v1/json/search"
        self.api_key = "v8n4xhhDSYwkyiwfDKSP"
		
    @commands.command(name="derpi", aliases=["db"])
    async def derpi(self, ctx, *, tags: str):
        """Searches Derpibooru for images based on tags, Separate tags with spaces. Use quotes for phrases"""
		
        tag_list = [tag.strip() for tag in tags.split(",")]
        query = ", ".join(tag_list)
        
        headers = {"User-Agent": "Dreambot/1.0"}
        params = {"q": tags, "key": self.api_key, "sf": "random", "per_page": 1}
		
        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            response.raise_for_status()
		
            data = response.json()
			
            if data.get("images"):
                image = data["images"][0]
                
                embed = discord.Embed(
                    title=f"search Result",
                    url=f"https://derpibooru.org/images/{image['id']}",
                    description=image.get("descritpion", "No description"),
                    color=await ctx.embed_color()
                )
                embed.set_image(url=image["representations"]["full"])
				
                await ctx.send(embed=embed)
            else:
                await ctx.send("No results found for those tags")
				
        except requests.exceptions.RequestException as e:
            await ctx.send(f"An error occured while contacting Derpibooru: {e}")
        except KeyError as e:
            await ctx.send("unexpected response format from Derpibooru.")