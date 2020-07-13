import discord
from discord.ext import commands
import  os


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
async def hey(ctx):
    await ctx.send('Welcome to the server!!')

bot.run(os.environ['TOKEN'])
