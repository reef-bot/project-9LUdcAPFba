# warning_system.py

import discord
from discord.ext import commands

class WarningSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='warn', help='Warn a user for violating server rules')
    async def warn(self, ctx, user: discord.Member, reason: str):
        # Logic to warn a user
        await ctx.send(f'{user.mention} has been warned for: {reason}')

    @commands.Cog.listener()
    async def on_message(self, message):
        # Logic to check for inappropriate content and issue warnings
        if 'bad_word' in message.content:
            await message.channel.send(f'{message.author.mention}, please refrain from using inappropriate language.')

def setup(bot):
    bot.add_cog(WarningSystem(bot))