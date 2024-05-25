# log_command.py

import discord
from discord.ext import commands

class LogCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send(f'An error occurred: {str(error)}')

    @commands.command(name='log', help='Log moderation actions for transparency')
    async def log_action(self, ctx, action, user):
        # Log the moderation action in the database
        try:
            # Code to log the action in the SQLite database
            await ctx.send(f'{action} logged for user {user}')
        except Exception as e:
            await ctx.send(f'Error logging the action: {str(e)}')

def setup(bot):
    bot.add_cog(LogCommand(bot))