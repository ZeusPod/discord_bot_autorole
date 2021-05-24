import discord
from discord import role
from discord import client
from discord.client import Client
from discord.ext import commands
from discord.flags import Intents
import os



intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)


bot = discord.Client()
bot = commands.Bot(command_prefix='>', intents = intents)


@bot.event
async def on_ready():
    print("bot is ready...")

#autorole functions when new member join the server
@bot.event 
async def on_member_join(ctx):
    autorole = discord.utils.get(ctx.guild.roles, name = 'role name here')
    await ctx.add_roles(autorole)


#Run the bot 
bot.run('token to your bot from discord developer portal')




