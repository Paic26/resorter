import discord
import json
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import traceback
import os
import random

def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix, case_insensitive=True)
Bot = discord.client
client = bot
client.remove_command('help')

class Startup(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Startup Cog is on')

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        channel = discord.utils.get(member.guild.channels, name='➤💙main-lobby')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,

        )
        embed.set_author(name=f"{member}", icon_url=member.avatar_url)
        embed.add_field(name=f'Welcome {member} to **Chill Resort:island:** ', value="\u200b", inline=False)
        
        await channel.send(embed=embed)
        
        print(f'{member} has joined a server')

    @commands.Cog.listener()
    async def on_member_remove(self, member:discord.Member):
        channel = discord.utils.get(member.guild.channels, name='➤💔invite-logs')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(
            colour=value,
        )
        embed.set_author(name=f" {member}", icon_url=member.avatar_url)
        embed.add_field(name=f'{member} has left the server', value="\u200b", inline=False)

        await channel.send(embed=embed)
        print(f'{member} has left a server')

def setup(bot):
    bot.add_cog(Startup(bot))
    print('Startup Loaded')
