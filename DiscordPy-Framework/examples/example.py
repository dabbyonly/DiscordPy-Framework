# Framework By dabbyonly
# Contact: dabbydiscord@gmail.com / server: discord.discord/dabbyonly

import discord
from discord.ext import commands

intents = discord.Intents.all() #<- Required!

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help') # <- If You Want to create Custom Help command It Is Required!

# --------- Bot Online Indicate Message -----------

@bot.event
async def on_ready():
    print("I am Online")

# --------- Bot Commands -----------

@bot.command()
async def ping(ctx):
    await ctx.reply('Pong!')

# ------------ Login ----------
bot.run(tocken)