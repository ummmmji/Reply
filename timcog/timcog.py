from redbot.core import commands

class timcog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('笑死'):
            await message.reply('笑死', mention_author=False)
            
        if message.content.startswith('婆'):
            await message.reply('小浠我婆', mention_author=False)
