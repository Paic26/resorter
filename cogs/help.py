import discord
import json
from discord.ext import commands, tasks
import random
import datetime


def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=">", case_insensitive=True)
Bot = discord.client
client = bot
client.remove_command('help')


class Help(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        # Events

        @commands.Cog.listener()
        async def on_ready(self):
            print('Help Cog is on')



    # HELP COMMANDS

    @commands.command()
    async def help(self, ctx):
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(
            colour=value,
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_author(name="Commands")
        embed.add_field(name="HelpF", value="Gives all the entertainment commands.", inline=False)
        embed.add_field(name="HelpM", value="Gives all the moderation commands.", inline=False)
        embed.set_footer(text=f"Just helped{ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['helpf','help_fun','help1'])
    async def helpfun(self, ctx):
        value1 = random.randint(0, 0xffffff)
        embed1 = discord.Embed(
            colour=value1,
            timestamp=datetime.datetime.utcnow()
        )

        embed1.set_author(name="Fun Commands")
        embed1.add_field(name="Coinflip", value="Heads or Tails", inline=False)
        embed1.add_field(name="8ball", value="Ask a question and the bot will give an answer", inline=False)
        embed1.add_field(name="WhoIs", value="Will give a certain user's info.", inline=False)
        embed1.add_field(name="Avatar", value="Shows the selected user's profile picture.", inline=False)
        embed1.add_field(name="Dm", value="Dm someone with the bot", inline=False)
        embed1.set_footer(text=f"Just helped{ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed1)

    @commands.command(aliases=['helpmod','helpM','helpstaff','help_staff'])
    async def helpmoderation(self, ctx):
        value2 = random.randint(0, 0xffffff)
        embed2 = discord.Embed(
            colour=value2,
            timestamp=datetime.datetime.utcnow()
        )

        embed2.set_author(name="Moderation Commands")
        embed2.add_field(name="Ban", value="Bans Users", inline=False)
        embed2.add_field(name="Unban", value="Unbans Users", inline=False)
        embed2.add_field(name="Kick", value="Kicks Users", inline=False)
        embed2.add_field(name="Mute", value="Mutes Users", inline=False)
        embed2.add_field(name="Unmute", value="Unmutes muted users", inline=False)
        embed2.add_field(name="Clear", value="Clears messages (clearall deletes all the messages from the channel)", inline=False)
        embed2.add_field(name="Warn", value="Warns users", inline=False)
        embed2.set_footer(text=f"Just helped{ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed2)

    @commands.command(aliases=['cryptocurrency'])
    async def crypto(self, ctx):
        value = random.randint(0, 0xffffff)
        crypto = discord.Embed(
            colour=value,
            timestamp=datetime.datetime.utcnow()
        )

        crypto.set_author(name="Crypto Commands")
        crypto.add_field(name="BTC", value="Bitcoin", inline=False)
        crypto.add_field(name="ETH", value="Ethereum", inline=False)
        crypto.add_field(name="BCH", value="Bitcoin Cash", inline=False)
        crypto.add_field(name="USDT", value="Tether", inline=False)
        crypto.add_field(name="CSPN", value="Crypto Sports",inline=False)
        crypto.set_footer(text=f"Just helped{ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=crypto)
        
def setup(bot):
    bot.add_cog(Help(bot))
    print('Help Loaded')
