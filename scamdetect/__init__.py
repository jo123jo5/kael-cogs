from .scamdetect import ScamDetect


async def setup(bot):
    await bot.add_cog(ScamDetect(bot))