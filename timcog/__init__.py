from .timcog import mycog


def setup(bot):
    bot.add_cog(MyCog(bot))
