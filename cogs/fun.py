import discord
from discord.ext import commands
import datetime
import requests
import random
from random import choice
import json

class Entertainment(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Entertainment Cog is on')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes.',
                     'Yes – definitely.',
                     'You may rely on it.']


        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,

        )
        embed.add_field(name=f'**Question:** {question}\n**Answer:** {random.choice(responses)}', value="hope you feel good with this answer.", inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def coinflip(self, ctx, *, toss):
        responses = ['Heads🤯',
                     'Tails🦨']

        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,

        )
        embed.add_field(name=f'**User Side:** {toss}\n**Result:** {random.choice(responses)}', value="Someone is gonna go cry to mommy.", inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=["aboutuser", "about_user", "userinfo", "user_info", "whoisme"])
    async def whois(self, ctx, member: discord.Member = None):
        member = member if member else ctx.author
        embed = discord.Embed(

            colour=member.colour,
            timestamp=ctx.message.created_at

        )

        roles = [role for role in member.roles]

        lenroles = len(roles) - 1

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="User Name", value=member.name, inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p EST"), inline=False)
        embed.add_field(name="Member Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p EST"), inline=False)
        embed.add_field(name=f"Roles ({lenroles})",
                        value=" ".join([r.mention for r in member.roles if r != ctx.guild.default_role]), inline=False)
        embed.add_field(name="Top Role", value=member.top_role.mention, inline=False)
        embed.add_field(name="Bot?", value=member.bot, inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=["avatar", "useravatar", "userpfp", "profilepicture", "profile_picture"])
    async def pfp(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(
            title=f"{member}'s Profile Picture",
            colour=member.colour
        )
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
        
        
    @commands.command(aliases=["pm"])
    async def dm(self, ctx, member: discord.Member, *, text):
        await ctx.message.delete()
        await member.send(f"{ctx.author} sent this dm:\n\n {text}")
        print(f"{ctx.author} DMed {member}: {text}")        


    #errors

    @whois.error
    async def whois_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('No user mentioned.')

    @coinflip.error
    async def coinflip_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please select a side.')

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please ask a question.')


def setup(bot):
    bot.add_cog(Entertainment(bot))
    print('Entertainment Loaded')
