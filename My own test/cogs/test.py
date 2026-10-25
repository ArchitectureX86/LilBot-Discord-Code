from __future__ import annotations
import discord
from discord import app_commands
from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
# commands
    '''@app_commands.command(name="send-receive", description="start the loop")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def test(self, inter: discord.Interaction):
        while True:
            await inter.response.defer()
            x = input()
            await inter.followup.send(f"{x}\n-# This message came from a command prompt input.",
                                    ephemeral=False)'''

# setup
async def setup(bot):
    await bot.add_cog(TestCog(bot))