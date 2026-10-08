import os
import pathlib
import random
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio
from modules import line_break
import platform

line_break("Starting")

class MyBot(commands.Bot):
    
    
    @tasks.loop(seconds = 15)
    async def statuschange():
        statuses = ["Driving in my car! right after a beer!",
                    "Hey catch me later and I'll buy you a beer!",
                    "Great scott! Gordon Freeman!",
                    f"🐍v{platform.python_version()}",
                    "Python is for fake programmers! (I'm made in Python)",
                    "Java or Javascript : Iunno, I don't use 'em.",
                    "Insert original status here.",
                    'Also play Terraria!',
                    'Also play Minecraft!',
                    'I wanna shower!']
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(statuses[random.randint(0, len(statuses)-1)]))
    
    async def on_ready(self):
        line_break("Bot is ready")
        print(f'Logged in as {self.user}!')
        await MyBot.statuschange.start()
        
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
        line_break("Syncing?")
        await bot.tree.sync()
        print("Synced!")

load_dotenv()
token = os.getenv('TOKEN')
print("getenv TOKEN")

intents = discord.Intents.default()
intents.message_content = True
print("intents set")

bot = MyBot(command_prefix="!", intents=intents, status=discord.Status.idle, activity=discord.Game("I wanna shower!"))

tree = bot.tree
print("bot / tree set")
bot.run(token)