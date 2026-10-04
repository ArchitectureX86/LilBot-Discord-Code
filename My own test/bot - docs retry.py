import os
import pathlib
import discord
from discord.ext import commands
from dotenv import load_dotenv
from modules import line_break

line_break("Starting")

class MyBot(commands.Bot):
    async def on_ready(self):
        line_break("Bot is ready")
        print(f'Logged in as {self.user}!')
        line_break("Syncing?")
        await bot.tree.sync()
        print("Synced!")
        
    async def on_message(self, message):    
        line_break("New message received")
        print(f'Message from {message.author}: {message.content}')
        
    async def setup_hook(self):
        line_break("Ran setup_hook")
        for file in pathlib.Path("cogs").rglob("*.py"):
            if file.stem.startswith("_"):
                continue
            line_break("Loading extensions / cogs")
            await bot.load_extension(".".join(file.with_suffix("").parts))
            print(f"var file: {file}")
            print(f"join file suffix: {".".join(file.with_suffix("").parts)}")

load_dotenv()
token = os.getenv('TOKEN')
print("getenv TOKEN")

intents = discord.Intents.default()
intents.message_content = True
print("intents set")

bot = MyBot(command_prefix="!", intents=intents)
tree = bot.tree
print("bot / tree set")
bot.run(token)