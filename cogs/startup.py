import discord
import json
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import traceback
import os

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
        self.change_status.start()
        print('Startup Cog is on')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel1 = discord.utils.get(member.guild.channels, name='➤❤rules')
        channel2 = discord.utils.get(member.guild.channels, name='➤❤information')
        channel = discord.utils.get(member.guild.channels, name='➤💙main-lobby')
        role = discord.utils.get(member.guild.roles, name='Member')
        memberCount = len(set(bot.get_all_members()))
        test= "name=f'Welcome {member.mention} to **Chill Resort** ', value="\u200b", inline=False"
        embed = discord.Embed(

            colour=value,

        )
        embed.set_author(name=f" {member}", icon_url=bot.user.avatar_url)
        await embed.add_field(name=test)
        embed.set_footer(text=f"Members, {memberCount}")
        await member.add_roles(role)
        
        print(f'{member} has joined a server')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,

        )
        embed.set_author(name=f" {member}", icon_url=bot.user.avatar_url)
        embed.add_field(name=f'{member} has left the server', value="\u200b", inline=False)
        embed.set_footer(text=f"Members, {memberCount}")
        await ctx.send(embed=embed)
        print(f'{member} has left a server')

def setup(bot):
    bot.add_cog(Startup(bot))
    print('Startup Loaded')
