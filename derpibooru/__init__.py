from .derpibooru import Derpibooru


async def setup(bot):
    await bot.add_cog(Derpibooru(bot))