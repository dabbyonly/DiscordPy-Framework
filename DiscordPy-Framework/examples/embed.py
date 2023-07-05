# Framework By dabbyonly
# Contact: dabbydiscord@gmail.com / server: discord.discord/dabbyonly

import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("I am Online!")


#------------------ Embeds ------------

@bot.command()
async def embed(ctx):
    embed = discord.Embed(
        title="This Is The Title", 
        description="This Is The Description"
    )
    embed.add_field(
        name="It Is The Field Name",
        value="It Is The Field Description",
        inline=False # This Value Can Be True/False Only
    )
    embed.add_field(
        name="It Is The Field2 Name",
        value="It Is The Field2 Description",
        inline=False # This Value Can Be True/False Only
    )
    await ctx.send(embed=embed)


bot.run(tocken)