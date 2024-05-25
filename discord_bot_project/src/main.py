# main.py

import discord
from discord.ext import commands
import os

# Import all command files
from commands.mute_command import MuteCommand
from commands.kick_command import KickCommand
from commands.log_command import LogCommand
from commands.warning_system import WarningSystem
from commands.clear_chat_command import ClearChatCommand
from commands.filter_command import FilterCommand

# Set up bot prefix
bot = commands.Bot(command_prefix='!')

# Add all command classes to the bot
bot.add_command(MuteCommand(bot))
bot.add_command(KickCommand(bot))
bot.add_command(LogCommand(bot))
bot.add_command(WarningSystem(bot))
bot.add_command(ClearChatCommand(bot))
bot.add_command(FilterCommand(bot))

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready')

# Run the bot with the Discord token
bot.run(os.getenv('DISCORD_TOKEN'))