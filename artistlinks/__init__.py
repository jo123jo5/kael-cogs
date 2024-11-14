from .artistlinks import ArtistLinks


async def setup(bot):
    await bot.add_cog(ArtistLinks(bot))