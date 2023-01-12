from extensions.image.suit import SuitCog


class Image(SuitCog):
    pass


async def setup(bot):
    await bot.add_cog(Image(bot))