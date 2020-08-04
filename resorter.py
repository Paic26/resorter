import discord
from discord.ext import commands
import  os
import random
from discord.utils import get
import random
from random import choice
import json
import asyncio
import datetime
from datetime import datetime
import praw
import platform

bot = commands.Bot(command_prefix = ">",  case_insensitive=True, owner_id=382947478422421516)
Bot = discord.client
client = bot
client.remove_command('help')
bot.version='V1.5'
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over Chill Resort"))
    print(f'{bot.user} has logged in.\n-----------------------------')

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded')

for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension((f'cogs.{filename[:-3]}'))

@bot.command()
async def welcome(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    responses = [
        f'You have just been welcomed by {ctx.author} :heart::heart:',
        f'Well hello there buddy, {ctx.author} just welcomed you to Chill Resort!!']


    value = random.randint(0, 0xffffff)
    embed = discord.Embed(

          colour=value,

     )
    embed.add_field(name=f'{random.choice(responses)}', value="\u200b", inline=False)

    await ctx.send(embed=embed)
    
@bot.command()
async def check(ctx):
    value = random.randint(0, 0xffffff)
    embed = discord.Embed(
        colour=value,
    )
    embed.add_field(name="'Bot online 🟩", value="\u200b")
    await ctx.send(embed=embed)
      
@bot.command()
async def stats(ctx):

    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(bot.guilds)
    memberCount = len(set(bot.get_all_members()))

    embed = discord.Embed(title=f'{bot.user.name} Stats',
                          description='\uFEFF',
                          colour=ctx.author.colour,
                          timestamp=ctx.message.created_at)

    embed.add_field(name='Bot Version:', value=f"{bot.version}", inline=False)
    embed.add_field(name='Python Version:', value=f"{pythonVersion}", inline=False)
    embed.add_field(name='Discord.Py Version', value=f"{dpyVersion}", inline=False)
    embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
    embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
    embed.add_field(name='Bot Developers:', value="<@382947478422421516>")

    embed.set_footer(text=f"Yours truly, {bot.user.name}")
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

    await ctx.send(embed=embed)    
    
    
 
bot.run(os.environ['TOKEN'])
