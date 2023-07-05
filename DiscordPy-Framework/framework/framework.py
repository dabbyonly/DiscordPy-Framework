# Framework By dabbyonly
# Contact: dabbydiscord@gmail.com / server: discord.discord/dabbyonly

import discord
from discord.ext import commands

intents = discord.Intents.all()

bot_prefix= ''   # Put Bot Prefix Here!

bot = commands.Bot(command_prefix=bot_prefix, intents=intents)
bot.remove_command('help')

# ------- Online Event ---------

online_message = '' # Put Your Online Indicate Message Here 

@bot.event
async def on_ready():
    print(online_message)

# ---------- Bot Commands ---------

#------------------------------------------------------------
# Put Your Bot Commands Here
# Check Example Folder In It Example.py For Commands Examples
#------------------------------------------------------------




#---------------------------- End -------------------------------

tocken = '' #put your bot tocken here
bot.run(tocken)

