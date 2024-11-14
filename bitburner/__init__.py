from .bitburner import BitBurner


async def setup(bot):
    await bot.add_cog(BitBurner(bot))