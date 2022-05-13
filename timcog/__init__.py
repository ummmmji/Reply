from .timcog import timcog


def setup(bot):
    bot.add_cog(timcog(bot))
