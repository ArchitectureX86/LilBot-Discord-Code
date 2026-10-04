from __future__ import annotations
import discord
from discord import app_commands
from discord.ext import commands
import datetime
import platform
import os
import sys
import socket
import pathlib
import psutil
import random
from rule34Py import rule34Py

client = rule34Py()
client.api_key = "93be47b937a43f8b8590cbc14dcbfd94a0b3ad867d5cfce119b6cf3c60927e6a4ac92699c176a42cc3899b61036c72e1c4e22715359a767559cb0031ddd7dcae"
client.user_id = "3803821"

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
"discordpy": "<:discordpy:1556219829583749212>"
}

# class
class SuperCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    mark = f"-# {emo['w7q']} Powered by Discord.py {DpyVer}."

# normal commands
# commands
    @app_commands.command(name="test-emoji", description="Thirty Calories.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @commands.is_owner()
    async def echagaino(self, inter: discord.Interaction):
        mark = f"-# {emo['w7q']} Powered by Discord.py {DpyVer}."
        mlist = []
        for i in emo:
            mlist.append(emo[f"{i}"])
        message = f"Bot emoji test:\n{", ".join(mlist)}"
        await inter.response.send_message(f"{message}\n{mark}")

    @app_commands.command(name="test", description="Thirty Calories.")
    @app_commands.describe(message="The message to echo.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @commands.is_owner()
    async def echo(self, inter: discord.Interaction, message: str):
        mark = f"-# {emo['w7q']} Powered by Discord.py {DpyVer}."
        await inter.response.send_message(f"{message}\n{mark}")

# sam34 - rule34.xxx posts in discord chat
    @app_commands.command(name="sam34", description="sam34")
    @app_commands.describe(message="Search for rule34 posts.")
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
    async def sam34get(self, inter: discord.Interaction, message: str, limit: int) -> None:
        r34tags = message.split(" ")
        p_id=random.randint(2,99)
        r34limit = limit
        loopwait = 0
        result = client.search(r34tags, page_id = p_id, limit = r34limit)
        r34_id = ['']
        for result in result:
            r34_id.append(f'https://rule34.xxx/index.php?page=post&s=view&id={result.id}')
            loopwait+=1
            if loopwait == r34limit:
                continue
        await inter.response.send_message(f"{('\n'.join(r34_id))}")

# psutil get pc stats
    @app_commands.command(name="server-stats", description="get current server stats")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def stats(self, inter: discord.Interaction) -> None:
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
        embed.add_field(name=f"Cpu usage:", value=f"`{cpu}% used.`",
                        inline=True)
        embed.add_field(name=f"Ram usage:", value=f"`{mem}% used.`",
                        inline=True)
        embed.set_author(name=f"Host information:",
                        icon_url=f"{GitAss}/Desktop/{platform.release()}.png"
                        )
        embed.add_field(name=f"{emo['missing']}", value=f"{emo['missing']}", inline=False)
        embed.add_field(name=f"{emo['XPwifi']} Powered by:",
                        value=f"{emo['fragment']} Api wrapper: [`Discord.py {DpyVer}`{emo['shortcut']}]({PyPi}/discord.py)\n{emo['pin']} Info & stats: [`Psutil {PsuVer}`{emo['shortcut']}]({PyPi}/psutil)",
                        inline=False)
        embed.set_footer(text=f"{SysInfo}, running {PyVer}.")
        await inter.response.send_message(embed=embed)

# dev commands
# reload cog
    @app_commands.command(name="reload-cog", description="Reload the chosen cog")
    @app_commands.describe(extension="The chosen cog.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @commands.is_owner()
    async def reload_cog(self, inter: discord.Interaction, extension: str):
        await inter.response.defer(ephemeral=True)
        try:
            await self.bot.reload_extension(f"cogs.{extension}")
        except commands.ExtensionError as error:
            await inter.followup.send(f"Could not reload {extension}: {error}", ephemeral=True)
        else:
            await self.bot.tree.sync()
            await inter.followup.send(f"Reloaded {extension}.", ephemeral=True)

# unload cog
    @app_commands.command(name="unload-cog", description="Unload the chosen cog")
    @app_commands.describe(extension="The chosen cog.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @commands.is_owner()
    async def unload_cog(self, inter: discord.Interaction, extension: str):
        await inter.response.defer(ephemeral=True)
        try:
            await self.bot.unload_extension(f"cogs.{extension}")
        except commands.ExtensionError as error:
            await inter.followup.send(f"Could not unload {extension}: {error}", ephemeral=True)
        else:
            await self.bot.tree.sync()
            await inter.followup.send(f"Unloaded {extension}.", ephemeral=True)

# load cog
    @app_commands.command(name="load-cog", description="Load the chosen cog")
    @app_commands.describe(extension="The chosen cog.")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @commands.is_owner()
    async def load_cog(self, inter: discord.Interaction, extension: str):
        await inter.response.defer(ephemeral=True)
        try:
            await self.bot.load_extension(f"cogs.{extension}")
        except commands.ExtensionError as error:
            await inter.followup.send(f"Could not load {extension}: {error}", ephemeral=True)
        else:
            await self.bot.tree.sync()
            await inter.followup.send(f"Loaded {extension}.", ephemeral=True)

# button test
'''
    class MyView(discord.ui.View):
        message: discord.Message | None = None
        count = 0
        
        def __init__(self, user: discord.User | discord.Member, timeout: float = 60.0) -> None:
            super().__init__(timeout=timeout)
            self.user = user
        
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
            self, interaction: discord.Interaction[discord.Client], error: Exception, item: discord.ui.Item[typing.Any]
            ):
            tb = "".join(
                traceback.format_exception(type(error), error, error.__traceback__)
                )
            message = f"An error occurred while processing the interaction for {str(item)}:\n```py\n{tb}\n```"
            await interaction.response.send_message(message)

    @bot.command()
    async def test(ctx: commands.Context[commands.Bot]) -> None:
        view = MyView(ctx.author)
        view.message = await ctx.send(
            embed=discord.Embed(
                title="Button Counter", description="Click on the button to count", color=discord.Color.blurple()
                ),
            view=view,
            )
'''

# setup
async def setup(bot):
    await bot.add_cog(SuperCog(bot))