from __future__ import annotations
import discord
from discord import app_commands
from discord.ext import commands
import datetime
from PIL import ImageGrab, Image
from io import BytesIO
import requests
import platform
import os
import socket
import traceback
import glob
import typing
import pathlib
from modules import line_break
import psutil
import random
from rule34Py import rule34Py

client = rule34Py()
client.api_key = "7462b31bb55e44794825fb17562c3089eb4336532192d8dae564c906db4c3bb347afc863199ba737fdf26c51b82af2dbd85c9247d60a4b42e5a2599038817d3e"
client.user_id = "6894854"

Git = "https://raw.githubusercontent.com/ArchitectureX86/Discord-Rich-Presence/refs/heads/main"
GitAss = f"{Git}/Presence%20py/assets"
PyPi = "https://pypi.org/project"
SysInfo = f"{platform.system()} {platform.release()} {os.name}"
SysPr = f"{platform.release()}"
SysName = f"{socket.gethostname()}"
SysUser = f"{os.environ.get("USERNAME", "Unknown user")}"
PyVer = f"🐍v{platform.python_version()}"
DpyVer = f"v{discord.__version__}"
PsuVer = f"v{psutil.__version__}"

# emoji list:
emo = {
"w11i": "<:11i:1555888881122021477>",
"w11q": "<:11q:1555888883428892672>",
"w10i": "<:10i:1555888876386517143>",
"w10q": "<:10q:1555888878152327193>",
"w7i": "<:7i:1555888871810793512>",
"w7q": "<:7q:1555888874071265420>",
"XPwifi": "<:XPwifi:1555888902827548693>",
"XPq": "<:XPq:1555888899853910096>",
"tf2": "<:tf2:1555904970610446366>",
"steam_circle": "<:steam_circle:1555905227809628244>",
"steam_style": "<:steam_style:1555905225133400094>",
"steam_tf2": "<:steam_tf2:1555905093537103933>",
"steam_west": "<:steam_west:1555905091058536458>",
"steam_square": "<:steam_square:1555905088755867648>",
"ps_icon": "<:ps_icon:1555904989245866104>",
"floppy": "<:floppy:1555904985651347456>",
"comp": "<:comp:1555904982077808660>",
"circuit": "<:circuit:1555904980194431137>",
"missing": "<:missing:1555904978311319593>",
"portal_rev": "<:portal_rev:1555904976520486982>",
"repo": "<:repo:1555904974217678890>",
"vector": "<:vector:1555904972229709825>",
"win7": "<:win7:1556152968657633310>",
"pin": "<:pin:1556152954644336710>",
"cd": "<:cd:1556152938668228628>",
"cdq": "<:cdq:1556152941403054100>",
"0warning": "<:0warning:1556152966405292132>",
"warning": "<:warning:1556153963286626325>",
"photo": "<:photo:1556152952723341399>",
"fragment": "<:fragment:1556152950340976791>",
"0check": "<:0check:1556152943655518278>",
"play": "<:play:1556152956733235261>",
"trash": "<:trash:1556152964068933782>",
"shortcut": "<:shortcut:1556152959715377193>",
"pin": "<:pin:1556152954644336710>",
"discordpy": "<:discordpy:1556219829583749212>",
"error": "<:error:1556152948009082960>",
"deny": "<:deny:1556152945819521075>"
}

mark = f"-# {emo['w7q']} Powered by Discord.py {DpyVer}."

ceo = "average_breadlover"

ineligible = f"You are not eligible to use this command.\n{mark}"

def cleanup(path, type):
    for file in pathlib.Path(f"{path}").rglob(f"*.{type}"):
        os.remove(file)

# button view class
class MyView(discord.ui.View):
    def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0) -> None:
        super().__init__(timeout=timeout)
        self.user = user
        self.message: discord.Message | None = None
        self.count = 0
        
    async def interaction_check(self, interaction: discord.Interaction[discord.Client]) -> bool:
        if interaction.user == self.user:
            return True
        await interaction.response.send_message(f"The command was initiated by {self.user.mention}", ephemeral=True)
        return False
    
    async def on_timeout(self) -> None:
        for button in self.children:
            button.disabled = True
        if self.message:
            await self.message.edit(view=self)
            
    @discord.ui.button(label="0", style=discord.ButtonStyle.green)
    async def counter(self, inter: discord.Interaction, button: discord.ui.Button[MyView]) -> None:
        self.count+=1
        button.label = str(self.count)
        await inter.response.edit_message(view=self)
        
    async def on_error(
        self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.any]
    ) -> None:
        tb = "".join(traceback.format_Exception(type(error), error, error.__traceback__))
        message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
        await interaction.response.send_message(message)

class SuperCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# normal commands
# commands
    @app_commands.command(name="screenshot", description="screenshot the dev's system.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def screenshot_grab(self, inter: discord.Interaction):
        if str(inter.user) == ceo :
            await inter.response.defer()
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')
            cleanup("screenshots", "webp")
            screenshot = ImageGrab.grab()
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/fullscreen_{timestamp}.webp"
            screenshot.save(filename, "webp")
            file = discord.File(f"{filename}")
            await inter.followup.send(file=file)
        else:
            await inter.response.send_message(f"{ineligible}", ephemeral=True)
            
    @app_commands.command(name="webp", description="Converts any image to Webp.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def imageconvert(self, inter: discord.Interaction, message: discord.Attachment):
        await inter.response.defer()
        if not os.path.exists('images'):
            os.makedirs('images')
        cleanup("images", "webp")
        response = requests.get(message)
        print(message)
        img = Image.open(BytesIO(response.content))
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"saved_{timestamp}.webp"
        img.save(f"images/{filename}", "webp")
        file = discord.File(f"images/{filename}")
        embed = discord.Embed(
            title="Submitted image redownloaded and sent as WebP.", color=discord.Color.from_rgb(33, 100, 166)
        )
        embed.set_image(url=f"attachment://{filename}")
        embed.add_field(name=f"{emo['XPwifi']} Powered by:",
                value=f"{emo['fragment']} Api wrapper: [`Discord.py {DpyVer}`{emo['shortcut']}]({PyPi}/discord.py)\n{emo['photo']} Pathlib, os & BytesIO.",
                inline=False)
        await inter.followup.send(file=file, embed=embed)

    @app_commands.command(name="test-emoji", description="Thirty Calories.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def echagaino(self, inter: discord.Interaction):
        await inter.response.defer(ephemeral=True)
        mlist = []
        for i in emo:
            mlist.append(emo[f"{i}"])
        message = f"Bot emoji test:\n{", ".join(mlist)}"
        await inter.followup.send(f"{message}\n{mark}", ephemeral=True)

    @app_commands.command(name="owner", description="Owner only.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ownertest(self, inter: discord.Interaction):
        if str(inter.user) == ceo:
            await inter.response.send_message(f"This was a test.")
        else:
            await inter.response.send_message(f"{ineligible}")

# psutil get pc stats
    @app_commands.command(name="server-stats", description="get current server stats")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def stats(self, inter: discord.Interaction) -> None:
        await inter.response.defer(ephemeral=True)
        cpu = int(psutil.cpu_percent(interval=None))
        mem = int(psutil.virtual_memory().percent)
        if cpu > 75:
            badge1 = f"{emo['0warning']}"
        else:
            badge1 = f"{emo['0check']}"
        if mem > 75:
            badge2 = f"{emo['0warning']}"
        else:
            badge2 = f"{emo['0check']}"
        embed = discord.Embed(
            color=discord.Color.from_rgb(33, 166, 100)
        )
        embed.set_author(name=f"Host information:",
                        icon_url=f"{GitAss}/Desktop/{platform.release()}.png"
                        )
        embed.add_field(name=f"Cpu usage:", value=f"`{cpu}% used.`",
                        inline=True)
        embed.add_field(name=f"Ram usage:", value=f"`{mem}% used.`",
                        inline=True)
        embed.add_field(name=f"Health score:", value=f"{badge1}{badge2}", inline=True)
        embed.add_field(name=f"{emo['XPwifi']} Powered by:",
                        value=f"{emo['fragment']} Api wrapper: [`Discord.py {DpyVer}`{emo['shortcut']}]({PyPi}/discord.py)\n{emo['photo']} Info & stats: [`Psutil {PsuVer}`{emo['shortcut']}]({PyPi}/psutil)",
                        inline=False)
        embed.set_footer(text=f"{SysInfo}, running {PyVer}.")
        await inter.followup.send(embed=embed, ephemeral=True)
        
# fuck it, we html.
    @app_commands.command(name="webcard", description="Generates a HTML card with given text and images.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def webcard(self, inter: discord.Interaction, header: str, paragraph: str, background: discord.Attachment):
        await inter.response.defer()
        if inter.user == ceo:
            ephemeral = False
        else:
            ephemeral = True
        embed = discord.Embed(
            color=discord.Color.from_rgb(200, 100, 50)
        )
        embed.set_author(name="Webcard Generator.",
                        icon_url = "attachment://assets/html5.webp"
                        )
        embed.add_field(name=f"Generated HTML:",
                        value=f'```<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8" />\n<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n<title>{inter.user}s card.</title>\n<link rel="stylesheet" href="styles.css" type="text/css" media="all" />\n<script src="script.js"></script>\n<style></style>\n</head>\n<body></body>\n</html>\n<div id="container">\n<img id="background" src={background}>\n<h id="header">{header}</h>\n<div class="fancy_underline"></div>\n<p class="paragraph">{paragraph}</p>\n</div>```',
                        inline=False)
        embed.add_field(name=f"{emo['XPq']} Background info:", value=f"'generated' does not {emo['deny']} mean generated by AI.\nThe bot owner highly recommends [`Phoenix Code`{emo['shortcut']}](https://phcode.io/) for efficient & assisted website creation.",
                        inline=True)
        await inter.followup.send(embed=embed, ephemeral=ephemeral)
        

# sam34 - rule34.xxx posts in discord chat
    @app_commands.command(name="sam34", description="sam34")
    @app_commands.describe(message="Search Rule34 posts.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def sam34get(self, inter: discord.Interaction, message: str, limit: int, ai: bool, ephemeral: bool) -> None:
        if str(inter.user) == ceo:
            await inter.response.defer(ephemeral=ephemeral)
            r34tags = message.split(", ")
            p_id=random.randint(2,99)
            r34limit = limit
            if ai == False:
                r34tags.append("-ai_generated")
            else:
                r34tags.append("ai_generated")
            result = client.search(r34tags, page_id = p_id, limit = r34limit)
            r34_id = ['']
            for result in result:
                r34_id.append(f"https://rule34.xxx/index.php?page=post&s=view&id={result.id}")
            if r34_id == ['']:
                await inter.followup.send("Rate limited!", ephemeral=ephemeral)
            else:
                await inter.followup.send(f"`tags: {message}, ai-generated:{ai}`{("\n".join(r34_id))}", ephemeral=ephemeral)
        else:
            await inter.response.send_message(f"{ineligible}")

# dev commands
# reload cog
    @app_commands.command(name="reload-cog", description="Reload the chosen cog")
    @app_commands.describe(extension="The chosen cog.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def reload_cog(self, inter: discord.Interaction, extension: str):
        if str(inter.user) == ceo:
            await inter.response.defer(ephemeral=True)
            try:
                await self.bot.reload_extension(f"cogs.{extension}")
            except commands.ExtensionError as error:
                await inter.followup.send(f"Could not reload {extension}: {error}", ephemeral=True)
            else:
                await self.bot.tree.sync()
                await inter.followup.send(f"Reloaded {extension}.", ephemeral=True)
        else:
            await inter.response.send_message(f"{ineligible}", ephemeral=True)

# unload cog
    @app_commands.command(name="unload-cog", description="Unload the chosen cog")
    @app_commands.describe(extension="The chosen cog.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)            
    async def unload_cog(self, inter: discord.Interaction, extension: str):
        if str(inter.user) == ceo:
            await inter.response.defer(ephemeral=True)
            try:
                await self.bot.unload_extension(f"cogs.{extension}")
            except commands.ExtensionError as error:
                await inter.followup.send(f"Could not unload {extension}: {error}", ephemeral=True)
            else:
                await self.bot.tree.sync()
                await inter.followup.send(f"Unloaded {extension}.", ephemeral=True)
        else:
            await inter.response.send_message(f"{ineligible}", ephemeral=True)

# load cog
    @app_commands.command(name="load-cog", description="Load the chosen cog")
    @app_commands.describe(extension="The chosen cog.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @commands.is_owner()
    async def load_cog(self, inter: discord.Interaction, extension: str):
        if str(inter.user) == ceo:
            await inter.response.defer(ephemeral=True)
            try:
                await self.bot.load_extension(f"cogs.{extension}")
            except commands.ExtensionError as error:
                await inter.followup.send(f"Could not load {extension}: {error}", ephemeral=True)
            else:
                await self.bot.tree.sync()
                await inter.followup.send(f"Loaded {extension}.", ephemeral=True)
        else:
            inter.response.send_message(f"{ineligible}", ephemeral=True)

# button test

        
    @app_commands.command(name="button-test", description="kill me.")
    async def buttontest(self, inter: discord.Interaction[commands.Bot]) -> None:
        if str(inter.user) == ceo:
            view = MyView(inter.user)
            await inter.response.send_message(
                embed=discord.Embed(
                    title="Button Counter", description="Click on the button to count", color=discord.Color.blurple(), ephemeral=True
                ),
                view=view
            )
            view.message = await inter.original_response()
        else:
            inter.response.send_message(f"{ineligible}", ephemeral=True)

# setup
async def setup(bot):
    await bot.add_cog(SuperCog(bot))