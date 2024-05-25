# clear_chat_command.py

import discord
from discord.ext import commands

class ClearChatCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear', help='Clear a specified number of messages in the chat')
    async def clear_chat(self, ctx, amount=5):
        if amount <= 0:
            await ctx.send('Please provide a valid number of messages to clear.')
            return
        
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'{amount} messages cleared successfully.')

def setup(bot):
    bot.add_cog(ClearChatCommand(bot))