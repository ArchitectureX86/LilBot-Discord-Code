from __future__ import annotations
import discord
from discord import app_commands
from discord.ext import commands

# class
class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="testagain", description="Thirty Calories.")
    @app_commands.describe(message="The message to echo.")
    async def echo(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

# setup
async def setup(bot):
    await bot.add_cog(TestCog(bot))