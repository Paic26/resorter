import discord
from discord.ext import commands
import  os
import random
from discord.utils import get

bot = commands.Bot(command_prefix = ".",  case_insensitive=True, owner_id=382947478422421516)
Bot = discord.client
client = bot


@bot.event
async def on_ready():
    print(f'{bot.user} has logged in.\n-----------------------------')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension((f'cogs.{filename[:-3]}'))


@bot.command()
async def welcome(ctx):
    await ctx.message.delete()
    await ctx.send('Welcome to the server!!')
    
@bot.command()
async def check(ctx):
    value = random.randint(0, 0xffffff)
    embed = discord.Embed(
        colour=value,
    )
    embed.add_field(name="'Bot online 🟩", value="\u200b")
    await ctx.send(embed=embed)
    
bot.run(os.environ['TOKEN'])
